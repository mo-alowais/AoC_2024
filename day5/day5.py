import functools
input = open('input5.txt', 'r')

def check(mappingDict, line) -> bool:
    for i in range(1, len(line)):
        if line[i] in mappingDict.keys():
            for j in line[i:]:
                if j in mappingDict[line[i]]: 
                    return False
    return True
mapping = dict()
sum = 0
flag = False
for line in input:
    if len(line) <= 1:flag=True
    else:
        if not flag:
            arr = list(map(int,line.strip('\n').split('|')))
            if arr[1] not in mapping.keys():
                mapping[arr[1]] = [arr[0]]
            else:
                mapping[arr[1]].append(arr[0])
        else:
            arr = list(map(int,line.strip('\n').split(',')))
            if check(mapping, arr) == True:
                sum += arr[int((len(arr)-1)//2)]
            
print(sum)

# part 2
input = open('input5.txt', 'r')

def check(mappingDict, line) -> bool:
    for i in range(1, len(line)):
        if line[i] in mappingDict.keys():
            for j in line[i:]:
                if j in mappingDict[line[i]]: 
                    return False
    return True

def cmp(x,y):
    if y in mapping[x]:
        return -1
    elif x in mapping[y]:
        return 1
    else:
        return 0

mapping = dict()
sum = 0
flag = False
for line in input:
    if len(line) <= 1:flag=True
    else:
        if not flag:
            arr = list(map(int,line.strip('\n').split('|')))
            if arr[1] not in mapping.keys():
                mapping[arr[1]] = [arr[0]]
            else:
                mapping[arr[1]].append(arr[0])
        else:
            arr = list(map(int,line.strip('\n').split(',')))
            if check(mapping, arr) == True:continue
            
            arr.sort(key=functools.cmp_to_key(cmp))
            sum += arr[int((len(arr))//2)]
print(sum)

