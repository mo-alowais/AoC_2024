import re
input = open(r'input3.txt','r')

# part 1
pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
total = 0
for i, line in enumerate(input):
    for match in re.finditer(pattern,line):
        total += int(match.group(1)) * int(match.group(2))
print("Total: %i" % total)

# part 2
# add "do()" and "don't()" enablers
input = open(r'input3.txt','r')
pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))")
total = 0
do = True
for i, line in enumerate(input):
    for match in re.finditer(pattern,line):
        if match.group(1) and match.group(2) and do:
            total += int(match.group(1)) * int(match.group(2))
        elif match.group(3):
            do = True
        elif match.group(4):
            do = False
print("Total: %i" % total)