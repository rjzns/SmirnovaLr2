from bottle import post, request
import re
from datetime import datetime
import pdb

# ���������� ��������� ��� �������� email
EMAIL_PATTERN = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# ������� ��� �������� ������
user_data = {}

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    username = request.forms.get('USERNAME')
    user_question = request.forms.get('QUEST')  # ��������� ���� QUESTION
    
    # �������� ������������� �����
    if not mail or not username or not user_question:
        return "Error: All fields must be filled!"
    
    # �������� ������� email
    if not re.match(EMAIL_PATTERN, mail):
        return "Error: Invalid email format!"
    
    # ��������� ������� ���� � ����������� �������
    access_date = datetime.now().strftime('%Y-%m-%d')
    
    # ���������� ������ � ������� (email ��� ����, ������ [username, question] ��� ��������)
    user_data[mail] = [username, user_question]
    
    # ���������� ������ �������
    pdb.set_trace()
    print("Current user_data dictionary:", user_data)
    
    return "Thanks, %s! The answer will be sent to the mail %s. Access Date: %s" % (username, mail, access_date)



