def maxsubarray(nums):

    maxmun = max(nums)
    if maxmun < 0:
        return maxmun

    maxmun = 0
    temp = 0

    for i in nums:
        if temp + i < 0:
            temp = 0

        if temp + i >= 0:
            temp = temp + i
            if temp > maxmun:
                maxmun = temp

    return maxmun


def main():
    x = []
    x.append(maxsubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    x.append(maxsubarray([1]))
    x.append(maxsubarray([5, 4, -1, 7, 8]))
    print(x)


if __name__ == "__main__":
    main()
