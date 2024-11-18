import unittest
from pymongo import MongoClient
from dotenv import load_dotenv
import os

class TestDatabaseOperations(unittest.TestCase):
    """Test MongoDB database operations."""

    @classmethod
    def setUpClass(cls):
        load_dotenv()
        cls.client = MongoClient(os.getenv('MONGODB_URI'))

    def test_ping(self):
        """Test the connection to MongoDB by using the ping command."""
        response = self.client.admin.command('ping')
        self.assertEqual(response['ok'], 1.0)

    def test_insert_document(self):
        """Test inserting a document into MongoDB."""
        db = self.client.get_database('shop_db')
        test_collection = db.test_collection
        test_doc = {'name': 'Test Product', 'price': 99.99}
        
        # Insert the document
        result = test_collection.insert_one(test_doc)
        self.assertIsNotNone(result.inserted_id)

        # Query the document
        queried_doc = test_collection.find_one({'name': 'Test Product'})
        self.assertEqual(queried_doc['name'], 'Test Product')

        # Clean up
        test_collection.delete_one({'_id': result.inserted_id})


if __name__ == '__main__':
    unittest.main()
