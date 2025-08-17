from pymongo import MongoClient
import pandas as pd

class MongoOperation:
    def __init__(self, client_url: str, database_name: str):
        """
        Initialize client & database.
        """
        self.client = MongoClient(client_url)
        self.db = self.client[database_name]
        print("✅ Connected with Atlas")

    def bulk_insert(self, df: pd.DataFrame, collection_name: str):
        """
        Insert multiple rows from DataFrame into a collection.
        """
        collection = self.db[collection_name]
        records = df.to_dict("records")
        if records:
            collection.insert_many(records)
            print(f"Inserted {len(records)} records into collection: {collection_name}")

    def insert_data(self, data: dict, collection_name: str):
        """
        Insert a single document into a given collection.
        """
        collection = self.db[collection_name]
        collection.insert_one(data)
        print(f"Inserted 1 record into collection: {collection_name}")

    def find(self, collection_name: str):
        """
        Fetch all documents from the given collection.
        """
        collection = self.db[collection_name]
        return list(collection.find())
