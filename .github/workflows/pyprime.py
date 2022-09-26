import sys

first_num = int(sys.argv[1])
second_num = int(sys.argv[2])

for num in range(first_num, second_num+1):
    if num > 1:
        for i in range(2, num):
            if(num%i==0):
                break
        else:
            print("prime numbers: ", num)
            