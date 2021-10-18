from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for email in emails:
            name, domain = email.split('@')
            local = name.split('+')[0].replace('.', '')
            unique_emails.add(local + '@' + domain)

        return len(unique_emails)
