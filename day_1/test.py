a = [1,2,3,4,10,20,30]

[3,5,7,14,30,50]

[8,12,21,48,98]

[20,43,69,146]

[63,112,215]

[175,7]

def sum_shift(a):
    if len(a)==1:
        return a[-1]
    elif len(a)==0:
        return 0
    else:
        for num in range(len(a)):
            if num > 0:
                a[num-1] = a[num] + a[num-1]
            if  num == len(a)-1:
                a.pop(num)
        print(a)
        return sum_shift(a)

print(sum_shift(a))

