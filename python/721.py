from collections import defaultdict
from typing import List


class Solution:

    def __init__(self):
        self.accounts = []
        self.emails_accounts_map = defaultdict(list)
        self.visited = []

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.accounts = accounts
        self.visited = [False] * len(accounts)
        res = []

        for i, account in enumerate(accounts):
            for email in account[1:]:
                self.emails_accounts_map[email].append(i)

        for i, account in enumerate(accounts):
            if self.visited[i]:
                continue
            name, emails = account[0], set()
            self.dfs(i, emails)
            res.append([name] + sorted(emails))

        return res

    def dfs(self, i, emails):
        if self.visited[i]:
            return

        self.visited[i] = True

        for email in self.accounts[i][1:]:
            emails.add(email)
            for nei in self.emails_accounts_map[email]:
                self.dfs(nei, emails)
