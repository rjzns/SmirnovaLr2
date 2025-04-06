from bottle import post, request
import re
from datetime import datetime
import json
import os

EMAIL_PATTERN = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
JSON_FILE = 'user_data.json'

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    username = request.forms.get('USERNAME')
    user_question = request.forms.get('QUEST')
    
    if not mail or not username or not user_question:
        return "Error: All fields must be filled!"
    
    if not re.match(EMAIL_PATTERN, mail):
        return "Error: Invalid email format!"
    
    if len(user_question) <= 3 or user_question.isdigit():
        return "Error: Question must be >3 chars and not only digits!"
    
    # Чтение текущих данных
    user_data = {}
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r') as f:
            user_data = json.load(f)
    
    # Добавление новых данных
    if mail in user_data:
        if user_question not in [q for _, q in user_data[mail]]:
            user_data[mail].append([username, user_question])
    else:
        user_data[mail] = [[username, user_question]]
    
    # Перезапись файла с обновлёнными данными
    with open(JSON_FILE, 'w') as f:  
        json.dump(user_data, f, indent=4)
    
    access_date = datetime.now().strftime('%Y-%m-%d')
    return "Thanks, %s! The answer will be sent to %s. Date: %s" % (username, mail, access_date)




