num = ['one','two','three','four','five','six','seven','eight','nine']
num2 = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
num3 = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
num4 = ['hundred']
num5 = ['thousand']

ans=0

# from 1 to 9
cnt1=0
for i in range(len(num)):
    cnt1+=len(num[i])

# from 10 to 19
cnt2=0
for i in range(len(num2)):
    cnt2+=len(num2[i])

# from 20 to 99
cnt3=0
for i in range(len(num3)):
    cnt3+=len(num3[i])
    for j in range(len(num)):
        cnt3+=len(num[j])
        cnt3+=len(num3[i])

# from 100 to 999
cnt4 = 0
for i in range(len(num)):
    cnt4+=100*(len(num[i])+len(num4[0]))
    cnt4+=cnt1+cnt2+cnt3
    cnt4+=3*99

# 1000
cnt5 = len(num5[0])
cnt5+=3

ans = cnt1+cnt2+cnt3+cnt4+cnt5

print ans
