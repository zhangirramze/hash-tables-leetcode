# Проверка на наличие дубликатов

class Solution:
    def containsDuplicate(self, nums):
        seen = set()  # множество

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
