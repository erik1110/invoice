import asyncio
import logging
import os
from pymongo import MongoClient

class MongoDBDao:
    def __init__(self, collection_name):
        self.mongo_uri = os.environ["MONGO_URI"]
        self.collection_name = collection_name

    def connect(self):
        try:
            self.client = MongoClient(self.mongo_uri)
            self.db = self.client.get_database()
            self.collection = self.db[self.collection_name]
            logging.info("Connected to MongoDB")
        except Exception as e:
            logging.warning(f"Error connecting to MongoDB: {str(e)}")

    def close(self):
        if self.client:
            self.client.close()
            logging.info("Closed MongoDB connection")

    def insert_one(self, document):
        try:
            result = self.collection.insert_one(document)
            return result.inserted_id
        except Exception as e:
            logging.warning(f"Error inserting document into MongoDB: {str(e)}")
            return None

    def update_one(self, query, update_data):
        try:
            result = self.collection.update_one(query, {'$set': update_data})
            if result.modified_count > 0:
                logging.info(f"Updated document in MongoDB with ID: {query['_id']}")
                return True
            else:
                logging.info(f"No document found matching query: {query}")
                return False
        except Exception as e:
            logging.warning(f"Error updating document in MongoDB: {str(e)}")
            return False

    async def find_all_async(self, query={}):
        try:
            documents = await asyncio.to_thread(self.collection.find, query)
            return list(documents)
        except Exception as e:
            logging.warning(f"Error finding documents in MongoDB: {str(e)}")
            return []

    def find_all(self, query={}):
        try:
            documents = self.collection.find(query)
            return list(documents)
        except Exception as e:
            logging.warning(f"Error finding documents in MongoDB: {str(e)}")
            return []

    def find_one(self, query={}):
        try:
            document = self.collection.find_one(query)
            return document
        except Exception as e:
            logging.warning(f"Error finding document in MongoDB: {str(e)}")
            return None

    def insert_many(self, documents):
        try:
            result = self.collection.insert_many(documents)
            return result.inserted_ids
        except Exception as e:
            logging.warning(f"Error inserting multiple documents into MongoDB: {str(e)}")
            return None

class DataDao:

    def __init__(self):
        self.conn = MongoDBDao(collection_name="Data")
        self.conn.connect()

    def close(self):
        if self.conn:
            self.conn.close()
