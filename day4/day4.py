input = open('input4.txt','r')
arr = []
for line in input:
    arr.append(list(line.strip('\n')))

xmasCount = 0
# part 1

def isValid(inputRow, idxToCheck : int, rev = False) -> bool:
    strToCheck = list("XMAS")

    if not strToCheck == arr[idxToCheck:idxToCheck+4] and rev:
        return False
    return strToCheck == arr[idxToCheck:idxToCheck+4] or isValid(inputRow[::-1], len(inputRow) - idxToCheck, True) 

# check rows
for i in range(len(arr)):
    if arr[i] == 'X'
    if isValid(arr[i], i):
        xmasCount += 1
# check columns
for i in range(len(arr[0])):
    if isValid([row[i] for row in arr], i):
        xmasCount += 1
# check diagonals
for i in range(len(arr)):
    if isValid([arr[j][j] for j in range(len(arr))], i):
        xmasCount += 1
    if isValid([arr[j][len(arr) - j - 1] for j in range(len(arr))], i):
        xmasCount += 1
print(xmasCount)
# part 2