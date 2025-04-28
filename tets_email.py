import unittest
import re
from myform import EMAIL_PATTERN

class TestEmailPattern(unittest.TestCase):
    
    def test_invalid_emails(self):
        invalid_emails = [
            "",
            "plain",
            "@domain.com",
            "user@.com",
            "user@domain",
            "user@domain..com",
            "user..name@domain.com",
            "user@domain@domain.com",
            "user name@domain.com",
            "user@domain com",
            "user#@domain.com",
            ".user@domain.com",
            "user.@domain.com",
            "user@domain-.com",
            "user@domain,com"
        ]
        
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(bool(re.match(EMAIL_PATTERN, email)), f"Expected {email} to be invalid")

    def test_valid_emails(self):
        valid_emails = [
            "simple@example.com",
            "user.name@domain.co",
            "user+tag@subdomain.org",
            "first-last@domain.net",
            "123user@domain.info",
            "user@sub.sub.domain.com",
            "a@b.co",
            "user_name@domain.edu",
            "test.email@domain.travel",
            "user123@domain.club",
            "name@domain.io",
            "user@123domain.com",
            "x.y.z@domain.biz",
            "user-abc@domain.shop",
            "email@domain.museum"
        ]
        
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(bool(re.match(EMAIL_PATTERN, email)), f"Expected {email} to be valid")

if __name__ == '__main__':
    unittest.main()