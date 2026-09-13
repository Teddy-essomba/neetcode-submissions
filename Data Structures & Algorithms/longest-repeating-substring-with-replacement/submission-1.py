class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        count = {}
        l = 0
        max_freq = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_freq = max(max_freq, count[s[r]])

            window_size = r - l + 1

            if window_size - max_freq > k:
                count[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
        return longest 



        

         



        