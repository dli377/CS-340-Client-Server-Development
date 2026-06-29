# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username, password, HOST, PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Create method to implement the C in CRUD. 
    def create(self, data):
        """
        Inserts a document into the specified MongoDB database and collection.
        Input argument is a set of key/value pairs (dictionary).
        """
        if data is not None:
            try:
                # Insert the dictionary object into the collection
                insert_result = self.collection.insert_one(data)
                # Return True if successful insert, else False
                return True if insert_result.acknowledged else False
            except Exception as e:
                print(f"An exception occurred during creation: {e}")
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty") 

    # Create method to implement the R in CRUD.
    def read(self, query):
        """
        Queries for documents from the specified MongoDB database and collection.
        Input argument is the key/value lookup pair.
        """
        if query is not None:
            try:
                # Use find() instead of find_one() to work with the cursor
                cursor = self.collection.find(query)
                # Return result in a list if the command is successful
                return list(cursor)
            except Exception as e:
                print(f"An exception occurred during read: {e}")
                # Return an empty list if not successful
                return []
        else:
            raise Exception("Nothing to search, because query parameter is empty")
    
    # Create method to implement the U in CRUD.
    def update(self, query, update_data):
        """
        Updates document(s) in the specified MongoDB database and collection.
        Inputs: 
            query (dict): The key/value lookup pair to find the document(s).
            update_data (dict): The key/value pairs to update.
        Returns:
            The number of documents modified.
        """
        if query is not None and update_data is not None:
            try:
                # Use update_many to update all documents matching the query
                # The $set operator replaces the value of a field with the specified value
                result = self.collection.update_many(query, {"$set": update_data})
                return result.modified_count
            except Exception as e:
                print(f"An exception occurred during update: {e}")
                return 0
        else:
            raise Exception("Search query or update data is empty")
    
    # Create method to implement the D in CRUD
    def delete(self, query):
        """
        Deletes document(s) from the specified MongoDB database and collection.
        Input:
            query (dict): The key/value lookup pair to find the document(s) to delete.
        Returns:
            The number of documents deleted.
        """
        if query is not None:
            try:
                # Use delete_many to remove all documents matching the query
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print(f"An exception occurred during delete: {e}")
                return 0
        else:
            raise Exception("Delete query parameter is empty")
