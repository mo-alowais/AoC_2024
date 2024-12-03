input = open(r'input2.txt','r')

def check(inputArr):
    for idx in range(len(inputArr) - 1): # check difference
            diff = inputArr[idx] - inputArr[idx + 1]
            if not 1 <= diff <= 3: 
                return False
    return True

arr1 = []
safeCount = 0
for line in input:
    arr1 = [int(item) for item in line.split()]
    if check(arr1) == True or check(arr1[::-1]) == True:
        safeCount +=1
input.close()
print("There are ", safeCount, " safe reports.")

# part 2
# difference: can tolerate one bad level
input = open(r'input2.txt','r')

def check(inputArr, tolOne = False):
    for idx in range(len(inputArr) - 1): # check difference
            diff = inputArr[idx] - inputArr[idx + 1]
            if not 1 <= diff <= 3: 
                return tolerateFun(inputArr,idx) and  not tolOne
    return True

# indirect recursion
def tolerateFun(inputArr, idx : int):
    return check(inputArr[idx-1:idx] + inputArr[idx + 1:],True) or check(inputArr[idx:idx + 1] + inputArr[idx + 2:],True)

   
safeCount = 0
for line in input:
    arr1 = [int(item) for item in line.split()]
    if check(arr1) == True or check(arr1[::-1]) == True:
        safeCount +=1
input.close()
print("There are ", safeCount, " safe reports if you tolerate one bad level.")
