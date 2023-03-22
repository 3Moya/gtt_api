import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('test-bd-gtt-firebase-adminsdk-f5483-1e3464f92e.json')
firebase_admin.initialize_app(cred)

def set_chat(data: dict, completion: str):
    chat_ref = firestore.client().collection('chats').document(data['id'])
    messages_ref = chat_ref.collection('messages')
    messages = data['messages']

    for i, message in enumerate(messages):
        messages_ref.document(str(i)).set(message)
        messages_ref.document(str(len(messages))).set({
            "role": "assistant",
            "content": completion})
        
def get_questions_answers():
    questions_answers_ref = firestore.client().collection('questions_answers')

    return [doc.to_dict() for doc in questions_answers_ref.get()]

def get_articles():
    articles_ref = firestore.client().collection('articles')

    return [doc.to_dict() for doc in articles_ref.get()]