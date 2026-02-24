class Solution:
    def findCommonResponse(self, responses: list[list[str]]) -> str:
        count = defaultdict(int)

        for i in responses:
            for response in set(i):
                count[response] += 1

        max_count = max(count.values())
        most_common = min(response for response, cnt in count.items() if cnt == max_count)

        return most_common

                    


        