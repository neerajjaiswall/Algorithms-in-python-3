# TODO: FFT implementation for MlogM algo

def three_sum(nums):
    res = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                # found three sum
                res.append([nums[i], nums[l], nums[r]])
                # remove duplicates
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return res


if __name__ == "__main__":
    x = [-1, 0, 1, 2, -1, -4]
    print("input: ", x)
    print("output should be: ", [[-1, -1, 2], [-1, 0, 1]])
    print("output: ", three_sum(x))
