print("enter marks obtained in 5 subjects:  ")
math=int(input())
ELA=int(input())
Science=int(input())
SS=int(input())
PE=int(input())

tot=math+ELA+Science+SS+PE
avg=tot/5

if avg>=91 and avg<=100:
    print("Your grade is an A")

elif avg>=81 and avg<=90:
    print("Your grade is an B")

elif avg>=71 and avg<=80:
    print("Your grade is an C")

elif avg>=61 and avg<=70:
    print("Your grade is an D")

elif avg>=51 and avg<=60:
    print("Your grade is an F")

else:
    print("its an invalid input")