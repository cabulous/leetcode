# https://leetcode.com/problems/license-key-formatting/discuss/131978/beats-100-python3-submission
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = s.replace('-', '').upper()[::-1]
        return '-'.join(chars[i:i + k] for i in range(0, len(chars), k))[::-1]
