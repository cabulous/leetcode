class Solution:
    def arrayStringsAreEqual(self, word1: [str], word2: [str]) -> bool:
        return ''.join(word1) == ''.join(word2)


class Solution:
    def arrayStringsAreEqual(self, word1: [str], word2: [str]) -> bool:
        list2 = []
        for s in word2:
            for c in s:
                list2.append(c)
        index = 0
        list2_len = len(list2)
        for s in word1:
            for c in s:
                if index >= list2_len or c != list2[index]:
                    return False
                index += 1
        if index <= (list2_len - 1):
            return False
        return True
