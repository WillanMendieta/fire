#from weakref import ref

from numpy import product
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#Carego el certifiocado
firebase_sdk = credentials.Certificate("firebace-2c864-firebase-adminsdk-1bhrq-6ee7ccdfc0.json")

#se hace referencia a la base de datos 
firebase_admin.initialize_app(firebase_sdk,{'databaseURL':'https://firebace-2c864-default-rtdb.firebaseio.com/'})
#Creo una coleccionde el nombre de productos 
#ref = db.reference('/productos')
#ref.push({'nombre': 'Arroz', 'cantidad': '5'})

#Modificar un Dato
ref = db.reference('productos')
producto_ref = ref.child('-N4BaVYV8COW403ZNZD2')
producto_ref.update({'nombre': 'Coca cola', 'cantidad': '5'})

#leer datos 

leer = ref.get('productos')
print(leer)

#metodo eliminar 

ref.delete('productos', '-N4BaVYV8COW403ZNZD2')