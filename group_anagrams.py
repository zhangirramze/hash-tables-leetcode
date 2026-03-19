# Группировка анаграмм

class Solution:
    def groupAnagrams(self, strs):
        hashmap = {}

        for word in strs:
            count = [0] * 26  # частоты букв

            for c in word:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)

            if key not in hashmap:
                hashmap[key] = []

            hashmap[key].append(word)

        return list(hashmap.values())
