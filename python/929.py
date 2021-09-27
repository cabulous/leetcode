from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_email = set()

        for email in emails:
            name, domain = email.split('@')
            local = name.split('+')[0].replace('.', '')
            unique_email.add(local + '@' + domain)

        return len(unique_email)


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for email in emails:
            clean_mail = []
            for c in email:
                if c == '+' or c == '@':
                    break
                if c != '.':
                    clean_mail.append(c)

            domain_name = []
            for c in reversed(email):
                domain_name.append(c)
                if c == '@':
                    break

            domain_name = ''.join(domain_name[::-1])
            clean_mail = ''.join(clean_mail)
            unique_emails.add(clean_mail + domain_name)

        return len(unique_emails)
