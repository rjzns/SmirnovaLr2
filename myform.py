from bottle import post, request
import re
from datetime import datetime
import json
import os

EMAIL_PATTERN = r'^(?!\.)[a-zA-Z0-9_!#$%&\'*+/=?`{|}~^.-]{1,64}(?<!\.)(?=.*[a-zA-Z0-9])@(?![-.])[a-zA-Z0-9-]{1,255}(?<!-)\.[a-zA-Z]{2,63}$'
JSON_FILE = 'user_data.json'

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    username = request.forms.get('USERNAME')
    user_question = request.forms.get('QUEST')
    
    # Проверка на пустые поля
    if not mail or not username or not user_question:
        return "Error: All fields must be filled!"
    
    # Проверка email
    if not re.match(EMAIL_PATTERN, mail):
        return "Error: Invalid email format!"
    
    # Проверка имени
    username = username.strip()
    if (len(username) <= 3 or 
        not any(c.isalpha() for c in username) or 
        re.match(r'^[?!.,\-\s]+$', username)):
        return "Error: Username must be >3 chars and contain letters!"
    
    # Проверка вопроса
    user_question = user_question.strip()
    if (len(user_question) <= 3 or 
        user_question.isdigit() or 
        re.match(r'^[?!.,\-\s]+$', user_question)):
        return "Error: Question must be >3 chars and not only digits/special chars!"
    
    # Чтение текущих данных
    user_data = {}
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r') as f:
            user_data = json.load(f)
    
    # Проверка имени при повторном вопросе
    if mail in user_data:
        existing_username = user_data[mail][0][0]
        if username != existing_username:
            return "Error: Username must match previous one for this email!"
        if user_question not in [q for _, q in user_data[mail]]:
            user_data[mail].append([username, user_question])
    else:
        user_data[mail] = [[username, user_question]]
    
    # Перезапись файла
    with open(JSON_FILE, 'w') as f:  
        json.dump(user_data, f, indent=4)
    
    access_date = datetime.now().strftime('%Y-%m-%d')
    return "Thanks, %s! The answer will be sent to %s. Date: %s" % (username, mail, access_date)




