class Solution:
    def similarRGB(self, color: str) -> str:
        res = '#'
        for i in range(1, 6, 2):
            res += self.find_similar(color[i:i + 2])
        return res

    def find_similar(self, color_section):
        num = int(color_section, 16)
        res = round(num / 17)
        return hex(res)[-1] * 2
