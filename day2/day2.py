import itertools
lines = []

while True:
    s = input()
    if len(s.strip())==0:
        break
    else:
        lines.append(s)

iters = zip(*(itertools.cycle(x) for x in lines))
count=0
while(i<height):
    if(next(iters)[i]=='#'):
        count+=1
    next(iters)
    next(iters)
    i+=1
count11 = count

iters = zip(*(itertools.cycle(x) for x in lines))
i=0
count11=0
while(i<height):
    if(next(iters)[i]=='#'):
        count11+=1
    i+=1

iters = zip(*(itertools.cycle(x) for x in lines))
i=0
count51=0
while(i<height):
    if(next(iters)[i]=='#'):
        count51+=1
    i+=1
    next(iters)
    next(iters)
    next(iters)
    next(iters)

iters = zip(*(itertools.cycle(x) for x in lines))
i=0
count71=0
while(i<height):
    if(next(iters)[i]=='#'):
        count71+=1
    i+=1
    next(iters)
    next(iters)
    next(iters)
    next(iters)
    next(iters)
    next(iters)

iters = zip(*(itertools.cycle(x) for x in lines))
i=0
count12=0
while(i<height):
    if(next(iters)[i]=='#'):
        count12+=1
    i+=2

print(count11*count12*count31*count51*count71)
