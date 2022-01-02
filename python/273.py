class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return 'Zero'

        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000
        res = ''

        if billion:
            res += self.three(billion) + ' Billion'
        if million:
            res += ' ' if res else ''
            res += self.three(million) + ' Million'
        if thousand:
            res += ' ' if res else ''
            res += self.three(thousand) + ' Thousand'
        if rest:
            res += ' ' if res else ''
            res += self.three(rest)

        return res

    def one(self, num):
        switcher = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'
        }
        return switcher.get(num)

    def two_less_20(self, num):
        switcher = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }
        return switcher.get(num)

    def ten(self, num):
        switcher = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }
        return switcher.get(num)

    def two(self, num):
        if not num:
            return ''
        if num < 10:
            return self.one(num)
        if num < 20:
            return self.two_less_20(num)
        tenner = num // 10
        rest = num - tenner * 10
        if rest:
            return self.ten(tenner) + ' ' + self.one(rest)
        return self.ten(tenner)

    def three(self, num):
        hundred = num // 100
        rest = num - hundred * 100
        if hundred and rest:
            return self.one(hundred) + ' Hundred ' + self.two(rest)
        if not hundred and rest:
            return self.two(rest)
        if hundred and not rest:
            return self.one(hundred) + ' Hundred'
