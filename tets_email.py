import unittest
import re
from myform import EMAIL_PATTERN

class TestEmailPattern(unittest.TestCase):
    
    def test_invalid_emails(self):
        invalid_emails = [
            "",                              # Empty string
            "plain",                         # No @ or domain
            "@domain.com",                   # No local part
            "user@.com",                     # No domain name
            "user@domain",                   # No TLD
            "user@domain..com",              # Double dot in domain
            "user..name@domain.com",         # Double dot in local part
            "user@domain@domain.com",        # Multiple @ symbols
            "user name@domain.com",          # Space in local part
            "user@domain com",               # Space in domain
            "user#@domain.com",              # Invalid special character
            ".user@domain.com",              # Local part starts with dot
            "user.@domain.com",              # Local part ends with dot
            "user@domain-.com",              # Domain ends with hyphen
            "user@domain,com",               # Comma instead of dot
            "user@-domain.com",              # Domain starts with hyphen
            "user@domain.",                  # Missing TLD
            "user@.",                        # Only dot after @
            "user@domain.c",                 # TLD too short
            "user@domain.123",               # Numeric TLD
            "a" * 65 + "@domain.com",        # Local part too long
            "user@" + "a" * 255 + ".com",    # Domain too long
            "user@domain.c0m",               # Number in TLD
            "<user>@domain.com",             # Invalid character
            "user@domain!.com",              # Invalid character in domain
            "user@domain/com",               # Slash in domain
            "user@[192.168.1.1]",            # IP address instead of domain
        ]
        
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(bool(re.match(EMAIL_PATTERN, email)), f"Expected {email} to be invalid")

    def test_valid_emails(self):
        valid_emails = [
            "simple@example.com",             # Basic email
            "user.name@domain.co",           # Dot in local part
            "user+tag@subdomain.org",        # Plus in local part
            "first-last@domain.net",         # Hyphen in local part
            "123user@domain.info",           # Numbers in local part
            "user@sub.sub.domain.com",       # Multiple subdomains
            "a@b.co",                        # Minimal email
            "user_name@domain.edu",          # Underscore in local part
            "test.email@domain.travel",      # Multiple dots in local part
            "user123@domain.club",           # Numbers in local part
            "name@domain.io",                # Two-letter TLD
            "user@123domain.com",            # Numbers in domain
            "x.y.z@domain.biz",              # Multiple dots in local part
            "user-abc@domain.shop",          # Hyphen in local part
            "email@domain.museum",           # Longer TLD
            "user@domain.co.uk",             # Country code TLD
            "user@sub-domain.com",           # Hyphen in domain
            "a" * 64 + "@domain.com",        # Max length local part
            "user@" + "a" * 63 + ".com",     # Max length domain part
            "user-123.name+tag@domain.com",  # Complex local part
        ]
        
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(bool(re.match(EMAIL_PATTERN, email)), f"Expected {email} to be valid")

if __name__ == '__main__':
    unittest.main()