from utils.extract_data import extract_data
from core.usecases.create_note import create_note

def handle_note(form_column):
    """
    Handler:
    1. Extract form data
    2. Call Core
    """
    form_data = extract_data(form_column)
    create_note(form_data)