class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # 用哈希表统计magazine字符，检查是否足够ransomNote
        letter_map = {}
        for letter in magazine:
            letter_map[letter] = letter_map.get(letter, 0) + 1
        for letter in ransomNote:
            letter_map[letter] = letter_map.get(letter, 0) - 1
            if letter_map[letter] < 0:
                return False
        return True

    # def canConstruct(self, ransomNote, magazine):
    #     return not collections.Counter(ransomNote) - collections.Counter(magazine)
