import math
import itertools

nums = [4, 1, 8, 7]


def judgePoint24(nums):
    print(nums)
    if len(nums) == 1:
        return math.isclose(nums[0], 24)

    return any(judgePoint24([x] + rest)

                for a, b, *rest in itertools.permutations(nums)
                for x in { a+b, a-b, a*b, b and a/b}
    )


print(judgePoint24(nums))
