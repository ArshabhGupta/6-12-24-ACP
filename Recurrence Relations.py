#Q. Print the recurrence relation of the following recursive functions given.
 
def Func1(n):
    if n <= 0:
        return
        print("The output is:", n / 2)
    
def array(a):
    sum = 0
    for i in a:
        sum = sum + i
    return (sum)

arr = eval(input("Enter an array: "))
num = int(input("Enter a number: "))
print("The sum of the array is:", array(arr))