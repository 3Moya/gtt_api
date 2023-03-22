import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('test-bd-gtt-firebase-adminsdk-f5483-1e3464f92e.json')
firebase_admin.initialize_app(cred)

def set_input(user_input: dict, nearest_neighbor: str, completion: str):
    input_ref = firestore.client().collection('input').document()

    input_ref.set({
        "user_input": user_input,
        "nearest_neighbor": nearest_neighbor,
        "completion": completion
    })
        
def get_questions_answers():
    questions_answers_ref = firestore.client().collection('questions_answers')

    return [doc.to_dict() for doc in questions_answers_ref.get()]

def get_articles():
    articles_ref = firestore.client().collection('articles')

    return [doc.to_dict() for doc in articles_ref.get()]