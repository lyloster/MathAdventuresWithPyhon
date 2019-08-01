#average of 2 numbers
def average(num1, num2):
    return (num1+num2)/2

#summation
def mySum(num):
    running_sum = 0
    for i in range(1, num+1):
        running_sum += i
    return running_sum

#summation n^2
def nSquareSum(num):
    running_sum = 0
    for i in range(num+1):
        running_sum += i**2 
    return running_sum


    

