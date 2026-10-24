from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for index1, val1 in enumerate(nums):
        for index2, val2 in enumerate(nums):
            if val1 + val2 == target and index1 != index2:
                return [index1, index2]
    return []


if __name__ == "__main__":
    testList = [1, 3, 4, 3, 5]
    target = 5
    print(twoSum(testList, target))