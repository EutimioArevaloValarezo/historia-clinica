import os
import dotenv
import pymongo


dotenv.load_dotenv(override=True)

user = str(os.getenv("MONGODB_USER"))
password = str(os.getenv("MONGODB_PASSWORD"))
try:
    client = pymongo.MongoClient('mongodb+srv://'+user+':'+password+'@cluster0.2q8xe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    print(os.getenv('MONGODB_DB'))
    db = client[os.getenv('MONGODB_DB')]
except Exception as e:
    print("ERROR AL CONECTAR LA BASE DE DATOS")