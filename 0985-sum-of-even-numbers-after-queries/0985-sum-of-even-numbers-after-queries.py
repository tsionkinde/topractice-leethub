class Solution:
    def sumEvenAfterQueries(self, nums, queries):
        even_sum = 0
        for x in nums:
            if x % 2 == 0:
                even_sum += x

        result = []

        for val, index in queries:
            if nums[index] % 2 == 0:
                even_sum -= nums[index]

            nums[index] += val

            if nums[index] % 2 == 0:
                even_sum += nums[index]

            result.append(even_sum)

        return result
        