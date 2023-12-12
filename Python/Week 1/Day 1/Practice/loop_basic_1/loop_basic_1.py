for i in range  (0,151):
    print(i)

for i  in range (5,1001):
    if i %5 == 0:
        print(i)

for i in range (1,101):
    if i % 5 == 0 and i % 10 != 0:
        i = "coding"
    elif i % 10 == 0 and i % 5 == 0 :
        i = "coding dojo"
    print(i)

x=0
for i in range (0,500001):
    x += i
    if i % 2 ==1 :
        print(i)
print(x) 

for i in range (2018 , 0 , -4):
    print(i) 

def low_high_mult (low , high , mult):
    for i in range (low , high + 1):
        if i % mult == 0 :
            print(i)


