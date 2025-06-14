import logging
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from config.database_config import PaymentDatabaseConfig

logging.basicConfig(level=logging.ERROR)

class PaymentServiceDatabase:
    def __init__(self):
        """Initialize MongoDB connection and setup collections."""
        try:
            print("trying ...")
            print("mongo connection string:", PaymentDatabaseConfig.MONGO_CONN_STR)
            self.client = MongoClient(PaymentDatabaseConfig.MONGO_CONN_STR)
            self.client.admin.command('ping')  # Ensures MongoDB is reachable
            print("connected")
            self.db = self.client[PaymentDatabaseConfig.MONGO_DB]

            # Create collections and indexes
            self._create_collections_and_indexes()

        except ConnectionFailure as e:
            logging.error(f"Could not connect to MongoDB: {e}")
            raise ConnectionFailure(f"Could not connect to MongoDB: {e}")


    def _create_collections_and_indexes(self):
        """Ensure collections exist and create necessary indexes."""
        for collection, indexes in PaymentDatabaseConfig.COLLECTIONS.items():
            if collection not in self.db.list_collection_names():
                self.db.create_collection(collection)

            # Optimize index creation
            existing_indexes = {index["name"] for index in self.db[collection].list_indexes()}
            for field, order in indexes:
                index_name = f"{field}_index"
                if index_name not in existing_indexes:
                    self.db[collection].create_index([(field, order)], name=index_name, background=True)


    def get_database(self):
        """Returns the database instance."""
        return self.db
    

    def close_connection(self):
        """Close the MongoDB connection."""
        self.client.close()