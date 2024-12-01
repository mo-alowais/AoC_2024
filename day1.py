import sys
import numpy as np

input = open(r'input1.txt','r')

arr1 = []
arr2 = []
for line in input:
    
    arr1.append(int(line.split()[0]))
    arr2.append(int(line.split()[1]))

arr1 = np.array(arr1)
arr2 = np.array(arr2)

arr1 = np.sort(arr1)
arr2 = np.sort(arr2)
total = abs(arr1-arr2)
total = total.sum()
print(total)

input.close()


# part 2

# remove duplicates in list 1 (if any)
newArr1 = set(arr1)
arr1 = np.array(list(newArr1))

count_dict = dict()
for i in arr2:
    if i in arr1:
        if i in count_dict.keys():
            count_dict[i] += i
        else:
            count_dict[i] = i


sim_score = sum(count_dict.values())

print("Similarity Score: ",sim_score)

