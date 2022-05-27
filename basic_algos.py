# 1.
# Print 1-255
# print1To255()
# Print all the integers from 1 to 255. 
def Counter():
    for i in range(1, 256):
        print(i)
# Counter()

# 2. 
# Print Odds 1-255
# printOdds1To255()
# Print all odd integers from 1 to 255. 
def printOdds():
    for i in range(1, 256):
        if i % 2 != 0:
            print(i)
# printOdds()

# 3. 
# Print Ints and Sum 0-255
# printIntsAndSum0To255()
# Print integers from 0 to 255, and with each 
# integer print the sum so far. 
def printIntsAndSums():
    sum = 0
    for i in range(1, 256):
        sum += i 
        print(str(i) + ', ' + str(sum))
# printIntsAndSums()

# 4. 
# Iterate and Print Array
# printArrayVals(arr)
# Iterate through a given array, printing each value. 
def printArrayVals(arr):
    for i in range(0, len(arr)):
        print(arr[i])
# IterateAndPrintArr([1, 4, '4,', 3, [1,2,3]])

# 5. 
# Find and Print Max
# printMaxOfArray(arr)
# Given an array, find and print its largest element. 
def printMaxOfArray(arr):
    max = None
    for i in range(0, len(arr)):
        if not max:
            max = arr[i]
        if arr[i] > max:
            max = arr[i]
    print(max)
# x = [1, 3, 2, 5, 7]
# y = [12, 2, 3, 8]
# printMaxOfArray(x)
# printMaxOfArray(y)

# 6. 
# Get and Print Average
# printAverageOfArray(arr)
# Analyze an array’s values and print the average. 
def printAvg(arr):
    sum = 0 
    for i in range(0, len(arr)):
        sum += arr[i]
    avg = sum / len(arr)
    print(avg)

# y = [12, 2, 3, 8]
# printAvg(y)

# 7. Array with Odds
# returnOddsArray1To255()
# Create an array with all the odd integers between 1 and 255 (inclusive).  
def printOddsArr():
    arr = []
    for i in range(1, 256):
        if i % 2 != 0:
            arr.append(i)
    print(arr)

# printOddsArr()

# 8. Square the Values
# squareArrayVals(arr)
# Square each value in a given array, returning that same array with changed values. 
def squareArrayVals(arr):
    for i in range(0, len(arr)):
        arr[i] = arr[i] ** 2 
    print(arr)

# squareArrayVals([3, 2, 10, 34, 7])

# 9. Greater than Y
# printArrayCountGreaterThanY(arr, y)
# Given an array and a value Y, count and print the number of array values greater than Y. 
def printArrayCountGreaterThanY(arr, y):
    count = 0
    for i in range(0, len(arr)):
        if arr[i] > y:
            count += 1
    print(count)

# array = [12, 2, 3, 11, 16]
# array2 = [14, 10, 20, 1, 50]
# array3 = [1, 2, 0, 1, 4, 5]
# printArrayCountGreaterThanY(array, 4)
# printArrayCountGreaterThanY(array2, 4)
# printArrayCountGreaterThanY(array3, 4)

# 10. 
# Zero Out Negative Numbers
# zeroOutArrayNegativeVals(arr)
# Return the given array, after setting any negative values to zero. 
def zeroOutArrayNegativeVals(arr):
    for i in range(0, len(arr)):
        if arr[i] < 0:
            arr[i] = 0
    return arr 

# print(zeroOutArrayNegativeVals([-5, 2, 15, -15, 11]))


# 11. Max, Min, Average
# printMaxMinAverageArrayVals(arr)
# Given an array, print the max, min and average values for that array.
def printMaxMinAverageArrayVals(arr):
    min = arr[0]
    max = arr[0]
    sum = 0

    for i in range(0, len(arr)):
        if arr[i] < min:
            min = arr[i]
        if arr[i] > max:
            max = arr[i]
        sum += arr[i]
    avg = sum / len(arr)
    print('min: ' + str(min) + ', max: ' + str(max) + ', avg: ' + str(avg))

# printMaxMinAverageArrayVals([12, 22, -5, 16, 11, 2, 5, -3])

# 12. Shift Array Values
# shiftArrayValsLeft(arr)
# Given an array, move all values forward (to the left) by 
# one index, dropping the first value and leaving a 0 (zero) 
# value at the end of the array.
def shiftArrayValsLeft(arr):
    for i in range(0, len(arr)):
        if i != (len(arr) -1):
            arr[i] = arr[i+1]
        if i == (len(arr) - 1):
            arr[i] = 0
    return arr

# print(shiftArrayValsLeft([2, 4, 6, 5, 7]))

# 13. Swap String For Array Negative Values
# swapStringForArrayNegativeVals(arr)
# Given an array of numbers, replace any negative values with the string 'NegValue'.
def swapStringForArrayNegativeVals(arr):
    for i in range(0, len(arr)):
        if arr[i] < 0:
            arr[i] = 'NegValue'
    return arr 

# print(swapStringForArrayNegativeVals([12, 11, -5, 4, 2, 0, -2]))
