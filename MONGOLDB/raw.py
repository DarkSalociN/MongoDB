from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# Replace the placeholder with your Atlas connection string
uri = "mongodb+srv://NicolasPdosSantos:Santos*123456@cluster0.pkw8zg7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Set the Stable API version when creating a new client
client = MongoClient(uri, server_api=ServerApi('1'))
                          
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)