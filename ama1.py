class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        res = []
        pipes = []
        stars = []
        for i in range(len(s)):
            k = s[i]
            if k == '*':
                stars.append(i)
            else:
                pipes.append(i)
        for query in queries:
            stars_count = 0
            pipel_low = pipel_low =0
            for val in pipes:
                if val >= query[0]:
                    pipel_low = val
            for val in stars:
                if query[0] <= val <= query[1]:
                    stars_count +=1
            res.append(stars_count)

        return res



# Write your code here

if __name__ == '__main__':
    print(numberOfItems("*|*|*|", [1], [6]))
