import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore

cred = credentials.Certificate("C:\\Users\\Marcos Josué Cruz\\Documents\\ARQUI2\\ARQUI2B_2S2024_G1\\Fase 2\\BACKEND\\arqui2-db-firebase-adminsdk-137on-dbfa694095.json")
firebase_admin.initialize_app(cred)

# Obtén una referencia a la base de datos
db = firestore.client()

# Ahora puedes hacer consultas, por ejemplo:
users_ref = db.collection('co2-collection')
docs = users_ref.get()
for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')

'''
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Autenticación con Firebase
cred = credentials.Certificate("C:\\Users\\Marcos Josué Cruz\\Documents\\ARQUI2\\ARQUI2B_2S2024_G1\\Fase 2\\BACKEND\\arqui2-db-firebase-adminsdk-137on-dbfa694095.json")
firebase_admin.initialize_app(cred)

# Obtén una referencia a Firestore
db = firestore.client()

# Listar las colecciones en la raíz
collections = db.collections()
for collection in collections:
    print(f'Colección encontrada: {collection.id}') '''
