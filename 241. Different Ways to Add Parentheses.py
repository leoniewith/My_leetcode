'''
Given a string of numbers and operators, return all possible results
from computing all the different possible ways to group numbers and operators.
The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
( 2 * (3- (4*5) ) ) = -34
( (2*3) - (4*5) ) = -14
( ( 2 * (3-4) ) *5 ) = -10
( 2 * ( (3-4) * 5) ) = -10
( ( (2*3) - 4 ) *5 ) = 10
'''


# 符号都存在奇数位， (1, 3, 5, 7, ...)
# 按符号的位置递归

class Solution:


    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        # input = list(input)
        #
        # res = []
        # operator_idx = [i for i in range(1, len(input), 2)]
        #
        # if operator_idx.__len__() == 1:
        #     res.append(eval(''.join(input)))
        #
        # for i in operator_idx:
        #     temp_calculate_result = str(eval(''.join(input[i-1: i+2])))
        #     input = input[i+2:]
        #     input.insert(i-1, temp_calculate_result)
        #     self.diffWaysToCompute(input)
        # return res

        res = []
        input = list(input)

        def recursive(l):
            operator_idx = [i for i in range(1, len(l), 2)]

            if operator_idx.__len__() == 1:
                res.append(eval(''.join(l)))
                return

            for i in operator_idx:
                temp_calculate_result = str(eval(''.join(l[i-1: i+2])))
                l = l[i+2:]
                l.insert(i-1, temp_calculate_result)
                recursive(l)

        for i in range(1, len(input), 2):
            recursive(input)

        return res

i = '2*3-4*5'
s = Solution()
print(s.diffWaysToCompute(i))



