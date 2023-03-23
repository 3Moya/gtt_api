import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('test-bd-gtt-firebase-adminsdk-f5483-1e3464f92e.json')
firebase_admin.initialize_app(cred)

def set_input(user_input: dict, nearest_neighbor: str, completion: str):
    """
    Guarda los datos de entrada del usuario en la colección 'input' de 
    Firestore.

    Args:
        user_input (str): Información ingresada por el usuario.
        nearest_neighbor (str): Una cadena que representa la pregunta más 
        cercana a la pregunta dada.
        completion (str): Respuesta dada por el modelo utilizado.
    """

    input_ref = firestore.client().collection('input').document()

    input_ref.set({
        "user_input": user_input,
        "nearest_neighbor": nearest_neighbor,
        "completion": completion
    })
        
def get_questions_answers():
    """
    Obtiene los documentos de la colección 'questions_answers' de Firestore y 
    los convierte en una lista de diccionarios.

    Returns:
        list: Lista de diccionarios que contienen la información de cada documento.
    """

    questions_answers_ref = firestore.client().collection('questions_answers')

    return [doc.to_dict() for doc in questions_answers_ref.get()]

def get_articles():
    """
    Obtiene los documentos de la colección 'articles' de Firestore y los 
    convierte en una lista de diccionarios.

    Returns:
        list: Lista de diccionarios que contienen la información de cada documento.
    """

    articles_ref = firestore.client().collection('articles')

    return [doc.to_dict() for doc in articles_ref.get()]