import re
import os
import streamlit as st
from utils import extract_first_name
import traceback
import requests
from pathlib import Path
import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Set level of logger
logger.setLevel(logging.ERROR)

# Create handlers
f_handler = logging.FileHandler('error_type_2.log', encoding='utf-8')

# Set level of handlers
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
f_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(f_handler)

def main():
    try:
        # Code that may raise an error
        st.title('Welcome to The Buggy App')
        st.write('Why do programmers prefer dark mode? Because light attracts bugs!')
        
        full_name = st.text_input('Enter your full name:')
        phone_number = st.text_input('Enter your phone number:')
        email_address = st.text_input('Enter your email address:')
        
        def is_phone_number(text):
            # This pattern is now for an international phone number format
            pattern = re.compile(r'(\+\d{1,3}[- ]?)?\d{10}$')
            return pattern.match(text) is not None
        
        def is_email(text):
            # This is a simple email pattern - for more complex patterns
            # you might need to refine this regex
            pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
            return pattern.match(text) is not None
        
        if any(char.isdigit() for char in full_name):
            st.write('You have entered digits in your name. Please use alphabetic characters for your name.')
        else:
            first_name = extract_first_name(full_name)
            if first_name and phone_number and email_address:
                assert is_phone_number(phone_number), f'{phone_number} should be a valid phone number.'
                assert is_email(email_address), f'{email_address} should be a valid email address.'
                st.write(f'Hello {first_name}! Thank you for sharing details.')
    except Exception as e:
        logger.error('Exception occurred', exc_info=True)
        st.write('Oops! Something went wrong. Do not worry; The Bugger GPT is on the case!')
        traceback_error = traceback.format_exc()
        data = {
            'traceback': traceback_error,
            'path': str(Path(os.path.abspath(__file__)).parent)
        }
        response = requests.post('http://localhost:8001', json=data)

if __name__ == '__main__':
    main()
