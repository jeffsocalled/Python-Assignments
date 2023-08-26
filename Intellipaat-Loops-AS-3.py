def check_prime(num):
    #num=int(input("Enter the number:"))
    flag = True
    if num == 1:
        flag = False
    elif num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if number is divisible by other number
                flag = False
                # break out of loop
                break
    return flag

array=[]
n= int(input("Enter the number of elements to be included in your array: "))
while (n > 0):
    print("Enter the element no.",len(array)+1,": ")
    array.append(int(input()))
    n-=1
print("Array with following elements has been created:\n",array)

print("The Prime numbers in your array are:")
for num in array:
    if check_prime(num):
        print(num)