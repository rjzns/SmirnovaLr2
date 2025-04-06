from bottle import post, request
import re
from datetime import datetime
import pdb

# Регулярное выражение для проверки email
EMAIL_PATTERN = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# Словарь для хранения данных
user_data = {}

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    username = request.forms.get('USERNAME')
    user_question = request.forms.get('QUEST')  # Добавлено поле QUESTION
    
    # Проверка заполненности полей
    if not mail or not username or not user_question:
        return "Error: All fields must be filled!"
    
    # Проверка формата email
    if not re.match(EMAIL_PATTERN, mail):
        return "Error: Invalid email format!"
    
    # Получение текущей даты в сокращённом формате
    access_date = datetime.now().strftime('%Y-%m-%d')
    
    # Сохранение данных в словарь (email как ключ, список [username, question] как значение)
    user_data[mail] = [username, user_question]
    
    # Отладочная печать словаря
    pdb.set_trace()
    print("Current user_data dictionary:", user_data)
    
    return "Thanks, %s! The answer will be sent to the mail %s. Access Date: %s" % (username, mail, access_date)



