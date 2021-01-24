lines = []
while True:
    s = input()
    if len(s.strip())==0:
        break
    else:
        lines.append(s)

count = 0
for i in lines:
    low,high = (int(x) for x in i[0].split('-'))
    if low <= i[2].count(i[1]) <= high:
        count +=1
print(count)
