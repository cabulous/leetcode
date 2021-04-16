import random
import string


# https://leetcode.com/problems/encode-and-decode-tinyurl/discuss/100268/Two-solutions-and-thoughts
class Codec:
    prefix = 'http://tinyurl.com/'
    alphabet = string.ascii_letters + '0123456789'
    code_len = 6

    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl: str) -> str:
        while longUrl not in self.url2code:
            code = ''.join(random.choice(Codec.alphabet) for _ in range(Codec.code_len))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return Codec.prefix + self.url2code[longUrl]

    def decode(self, shortUrl: str) -> str:
        return self.code2url[shortUrl[-Codec.code_len:]]
