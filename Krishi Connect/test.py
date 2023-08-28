f = open('test.txt', 'r')
l = [[]]
x=0
y=0
for i in f.readlines():
    if len(i.strip())==2:
        l.append([i.strip(),])
        x+=1
    else:
        l[y].append(i.strip())
        y+=1
print(l)