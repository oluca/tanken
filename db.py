import firebase_admin
from firebase_admin import firestore
import calendar, time

class Db():
    
    def __init__(self):

        pass

    def connect(self):
        
        cred_obj = firebase_admin.credentials.Certificate(self.firebaseAuth)
        default_app = firebase_admin.initialize_app(cred_obj)

        return firestore.client()

    def insert(self, diesel, e10, e5):

        doc_ref = self.connect().collection('Prices').document(f'{calendar.timegm(time.gmtime())}')
        
        doc_ref.set({

            'diesel':float(diesel),
            'e10':float(e10),
            'e5':float(e5)

        })