from collections import deque


class HtmlParser(object):
    def getUrls(self, url):
        pass


class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> list[str]:
        domain = self.get_domain(startUrl)
        queue = deque([startUrl])
        visited = {startUrl}
        res = [startUrl]

        while queue:
            url = queue.popleft()
            for next_url in htmlParser.getUrls(url):
                if next_url not in visited and self.get_domain(next_url) == domain:
                    visited.add(next_url)
                    queue.append(next_url)
                    res.append(next_url)

        return res

    def get_domain(self, url):
        return url.split('http://')[1].split('/')[0]
