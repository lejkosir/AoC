import numpy
import math


def remake(filename):
    with open(filename, 'r') as f:
        l = []
        for line in f:
            line_split = line.split(":")
            nums = line_split[1][1:-1].split(" ")
            nums_int = []
            for x in nums:
                nums_int.append(int(x))
            l.append((int(line_split[0]), nums_int))
    return l


# narejeno v binarnim zapisom
def first(filename):
    l = remake(filename)
    summed = 0
    for line in l:
        total, nums = line
        print(total, nums)
        binary = int(math.pow(2, len(nums)-1)) - 1
        for i in range(int(math.pow(2, len(nums)-1))):
            tots = 0
            binned = (bin(binary))[2:].rjust(int(len(nums)-1), "0")
            for j, x in enumerate(binned):
                if j == 0:
                    tots = nums[0]
                if x == "0":
                    tots += nums[j + 1]
                else:
                    tots *= nums[j + 1]
            if tots == total:
                summed += total
                break
            binary = binary - 1
    print(summed)


# narejeno v terciarnem zapisu :)
def second(filename):
    l = remake(filename)
    summed = 0
    for line in l:
        total, nums = line
        tert = int(math.pow(3, len(nums)-1)) - 1
        for i in range(int(math.pow(3, len(nums)-1))):
            tots = 0
            terred = numpy.base_repr(tert, 3, 0).rjust(int(len(nums)-1), "0")
            for j, x in enumerate(terred):
                if j == 0:
                    tots = nums[0]
                if x == "0":
                    tots += nums[j+1]
                elif x == "1":
                    tots *= nums[j+1]
                else:
                    tots = int(str(tots) + str(nums[j+1]))
            if tots == total:
                summed += total
                break
            tert -= 1
    print(summed)

first("files/7")
second("files/7")