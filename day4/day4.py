input = open('input4.txt')
arr = []
for line in input:
    arr.append(list(line.strip('\n')))

xmasCount = 0
# part 1
for r in range(len(arr)):
    for c in range(len(arr[0])):
        if arr[r][c] != "X": continue
        for dr, dc in [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]:
            if not(0 <= r + 3 * dr < len(arr) and 0 <= c + 3*dc < len(arr[0])): continue
            if arr[r + dr][c + dc] == 'M' and arr[r + 2*dr][c + 2*dc] == 'A' and arr[r + 3*dr][c + 3*dc] == 'S':
                xmasCount += 1                
                
print(xmasCount)

xmasCount = 0
# part 2
for r in range(1,len(arr)-1):
    for c in range(1,len(arr[0])-1):
        if arr[r][c] != "A": continue
        corners = [arr[r-1][c-1], arr[r-1][c+1], arr[r+1][c-1], arr[r+1][c+1]]
        if "".join(corners) in ["MMSS", "MSSM", "SSMM", "SMMS"]:
            xmasCount += 1

print(xmasCount)