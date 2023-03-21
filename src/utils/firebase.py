import firebase_admin
from firebase_admin import credentials, firestore
import os

CERT = {
    "type": os.getenv('TYPE'),
    "project_id": os.getenv('PROJECT_ID'),
    "private_key_id": os.getenv('PRIVATE_KEY_ID'),
    "private_key": os.getenv('PRIVATE_KEY'),
    "client_email": os.getenv('CLIENT_EMAIL'),
    "client_id": os.getenv('CLIENT_ID'),
    "auth_uri": os.getenv('AUTH_URI'),
    "token_uri": os.getenv('TOKEN_URI'),
    "auth_provider_x509_cert_url": os.getenv('AUTH_PROVIDER_X509_CERT_URL'),
    "client_x509_cert_url": os.getenv('CLIENT_X509_CERT_URL')
}

cred = credentials.Certificate(CERT)
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