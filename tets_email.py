import unittest
import re
from myform import EMAIL_PATTERN  

class TestEmailValidation(unittest.TestCase):
    
    def test_invalid_emails(self):
  
        list_mail_uncor = [
            "",                   
            "1",                   
            "m1@",                 
            "@mail",               
            "m1@mail",            
            "m1@.ru",              
            "m1.mail.ru",          
            "m@ma@il.ru",          
            "m1#mail.ru",          
            " m1@mail.ru",         
            "m1@mail.ru ",         
            "m1@ma il.ru"          
        ]
        
  
        for email in list_mail_uncor:
            with self.subTest(email=email):
                self.assertFalse(re.match(EMAIL_PATTERN, email), f"Email {email} uncorrect")

    def test_valid_emails(self):

        list_mail_cor = [
            "m.m@mail.ru",
            "m1@gmail.com",
            "user123@domain.co.uk",
            "test.email@subdomain.example.com",
            "name+tag@domain.org"
        ]
        

        for email in list_mail_cor:
            with self.subTest(email=email):
                self.assertTrue(re.match(EMAIL_PATTERN, email), f"Email {email} correct")

if __name__ == '__main__':
    unittest.main()