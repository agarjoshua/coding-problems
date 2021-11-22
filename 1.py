# 1. You are given two string arrays words1 and words2.
# A string b is a subset of string a if every letter in b occurs in a including multiplicity.
# For example, "wrr" is a subset of "warrior" but is not a subset of "world".
# A string a from words1 is universal if for every string b in words2, b is a subset of a.
# Return an array of all the universal strings in words1. You may return the answer in any order.
 
# Example 1:
# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
# Output: ["facebook","google","leetcode"]

# Example 2:
# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
# Output: ["apple","google","leetcode"]

# Example 3:
# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","oo"]
# Output: ["facebook","google"]

# Example 4:
# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["lo","eo"]
# Output: ["google","leetcode"]

# Example 5:
# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["ec","oc","ceo"]
# Output: ["facebook","leetcode"]

from typing import Counter, List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        totalword = {}

        for b in words2:
            tmp = Counter(b)
            for k,v in tmp.items():
                totalword[k] = v if k not in totalword else max(v, totalword[k])
        output = []

        for a in words1:
            tmp = Counter(a)
            if all(k in tmp and v <= tmp[k] for k, v in totalword.items()):
                output.append(a)
        return output


# Notes:
# 1. A brute force solution would include an implementation of O(A*B) but a more efficient way would be to use the algorithm O(A+B) 