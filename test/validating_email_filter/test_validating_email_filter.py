import unittest
from src.validating_email_filter.util import filter_mail

class test_email_validate_filter(unittest.TestCase):
    def test_valid_emails(self):
        emails = [
            "aaaa@aaaa.com",
            "bbbb-26@bbb.com",
            "ggggg_54@gggg.com"
        ]
        result = filter_mail(emails)
        self.assertEqual(sorted(result), sorted(emails))

    def test_invalid_emails(self):
        emails = [
            "invalid@.com",
            "noatsymbol.com",
            "user@site.c0m",
            "user@site.comm"
        ]
        result = filter_mail(emails)
        self.assertEqual(result, [])

    def test_mixed_emails(self):
        emails = [
            "good_user@domain.org",
            "bad@web.123",
        ]
        result = filter_mail(emails)
        self.assertEqual(sorted(result), ["good_user@domain.org"])

if __name__ == "__main__":
    unittest.main()