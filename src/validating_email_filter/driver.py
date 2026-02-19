from util import filter_mail

if __name__ == "__main__":
    print("Enter the number of email addresses:")
    n = int(input().strip())
    emails = []
    print("Enter the email addresses one per line:")
    for _ in range(n):
        emails.append(input().strip())
    valid_emails = filter_mail(emails)
    valid_emails.sort()
    print(valid_emails)