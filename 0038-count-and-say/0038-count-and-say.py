class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"

        for _ in range(n - 1):
            cur = ""
            count = 1

            for i in range(1, len(res)):
                if res[i] == res[i - 1]:
                    count += 1
                else:
                    cur += str(count) + res[i - 1]
                    count = 1

            cur += str(count) + res[-1]
            res = cur

        return res