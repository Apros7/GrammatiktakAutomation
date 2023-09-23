from google.cloud import datastore
import json
import os
from tqdm import tqdm

os.chdir("/Users/lucasvilsen/Desktop/GrammatiktakAutomation/usage_analytics")

class FirestoreClient():
    def __init__(self):
        key_path = "Keys/serviceAccountKey.json"
        self.client = datastore.Client.from_service_account_json(key_path)
        self.kinds = ["Backend-alltext", "Feedback"]
        self.KIND = ""
    
    def check_kind(self, kind):
        if self.KIND: 
            if self.KIND not in self.kinds: raise ValueError(f"Kind {kind} not in {self.kinds}")
        if kind not in self.kinds: raise ValueError(f"Kind {kind} not in {self.kinds}")
        if not self.KIND: self.KIND = kind

    def get_all_text(self, kind):
        self.check_kind(kind)
        query = self.client.query(kind=kind)
        entities = query.fetch()
        print(f"Number of entities in {kind}: {len(entities)}")
        return entities

    def remove_duplicates(self, lst):
        cleaned_lst = []
        for dict in lst:
            if dict not in cleaned_lst:
                cleaned_lst.append(dict)
        return cleaned_lst

    def add_keys_if_does_not_exist(self, lst):
        keys = ["feedback", "text"]
        for dict in lst:
            for key in keys:
                if key not in dict:
                    dict[key] = ""
        return lst

    def clean_entities(self, entities):
        cleaned_entities = []
        for entity in tqdm(entities):
            cleaned_entity = {}
            for key, value in sorted(entity.items()):
                true_key = key[:-1] if key[-1].isdigit() else key
                if not any([true_key == kind for kind in ["feedback", "text", "state", "time"]]):
                    continue
                if true_key in cleaned_entity:
                    cleaned_entity[true_key] += value
                else:
                    cleaned_entity[true_key] = value
            cleaned_entities.append(cleaned_entity)
        no_duplicates = self.remove_duplicates(cleaned_entities)
        no_empty_dicts = self.add_keys_if_does_not_exist(no_duplicates)
        return no_empty_dicts

    def tag_entities(self, entities, kind):
        for entity in entities:
            if kind == "Backend-alltext":
                if "time" not in entity: entity["time"] = "unknown"
                if "state" in entity: del entity['time']
            elif kind == "Feedback": entity["state"] = "new"
        return entities

    def save_entities_to_csv(self, kind):
        entities = self.get_all_text(kind)
        self.check_kind(kind)
        filepath = "datastore/" + kind + ".json"
        if os.path.exists(filepath):
            earlier_entities = list(json.load(open("datastore/" + kind + ".json")))
            print("Reading file...")
            all_entities = list(entities) + earlier_entities
        else: 
            all_entities = entities
        cleaned_entities = self.clean_entities(all_entities)
        tagged_entities = self.tag_entities(cleaned_entities, kind)
        json.dump(tagged_entities, open("datastore/" + kind + ".json", "w"), indent=4, ensure_ascii=False)
        
    def delete_all_entries(self, kind):
        self.check_kind(kind)
        query = self.client.query(kind=kind)
        entities = query.fetch()
        keys = [entity.key for entity in entities]
        self.client.delete_multi(keys)
    
    def save_and_delete(self, kind):
        self.check_kind(kind)
        self.save_entities_to_csv(kind)
        self.delete_all_entries(kind)
    
    def update(self):
        self.save_and_delete("Feedback")
        self.save_and_delete("Backend-alltext")