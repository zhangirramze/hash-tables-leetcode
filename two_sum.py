# Задача: Two Sum
# Находим два числа, сумма которых равна target

class Solution:
    def twoSum(self, nums, target):
        seen = {}  # словарь: число -> индекс

        for i in range(len(nums)):
            diff = target - nums[i]

            # если нужное число уже было
            if diff in seen:
                return [seen[diff], i]

            seen[nums[i]] = i
