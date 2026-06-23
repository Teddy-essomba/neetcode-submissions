class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        L = 0
        maxFreq = 0
        longest = 0

        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            maxFreq = max(maxFreq, count[s[R]])

            window_size = R - L + 1

            if window_size - maxFreq > k:
                count[s[L]] -= 1
                L += 1

            longest = max(longest, R - L + 1)

        return longest



            




        
        

        