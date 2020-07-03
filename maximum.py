def find_maximum(numbers):
    max_num=numbers[0]
    for i in range(0,len(numbers)):
        if (numbers[i]>max_num):
            max_num=numbers[i]
    return max_num

import random
numbers= random. sample(range(-10000,10000), 1000)]
max_num=find_maximum(numbers)
print(max_num)
