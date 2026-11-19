def print2Largest(a,a_size):
    largest=secondLargest = -2147483648
    for i in range(a_size):

    #if the current element of the array is greater than our currnet largest number, then replace
        if (a[i] > largest):
            secondLargest=largest
            largest=a[i]

            #IF current elemnt is less than current largest but greater than second largest then replace the number
        elif (a[i] > secondLargest and a[i] != largest):
            secondLargest=a[i]

    print(secondLargest)

a=[1,89,100,45,78,234,23,36,342]
a_size=len(a)
print2Largest(a,a_size)