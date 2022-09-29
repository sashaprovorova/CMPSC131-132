"""
In this program you are going to implement higher order functions. Create a function which is capable of tracking
how long code executes (the You Tube video in this lesson will be very helpful).

Next create two identical lists of random numbers. Make sure the lists are long. I would recommend you write a small
function using the random number generator to quickly generate several thousand numbers. Then implement any two
sorting algorithms. For example, the selection sort and the bubble sort. You are free to choose any two algorithms.

Finally, sort the lists with each function and use your timer function to show which algorithm is more efficient.
"""
#imports random and time functions
import random
import time

#quickly generates numbers
def listOfNum():
    createdList=[]
    for i in range (10000):
        createdList.append(random.randint(1,1000))
    return createdList

# sorts the elements in the list by using Selection Sorting method
def selection(data):
    for i in range(len(data)):
        min = 1
        for j in range(i + 1, len(data)):
            if (data[min] > data[j]):
                min = j
        temp = data[i]
        data[i] = data[min]
        data[min] = temp

# sorts the elements in the list by using Bubble Sorting method
def bubbleSort(data):
    for i in range(len(data) - 1, 0, -1):
        for j in range(i):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp

# tracks the runtime
def timer(list):

    list2 = list

    ##tracks how long selection sort code executes
    startSelection = time.time()
    selection(list)
    endSelection = time.time()
    timeTaken = endSelection - startSelection
    print("Selection sort runtime:", timeTaken)

    #tracks how long bubble sort code executes
    startBubble = time.time()
    bubbleSort(list2)
    endBubble = time.time()
    timeTaken2 = endBubble - startBubble
    print("Bubble sort runtime:", timeTaken2)

    difference = timeTaken2 - timeTaken
    print("The difference in runtime between bubble sort and selection sort:", difference)

# main function calls other functions
def main():
    givenList = listOfNum()
    timer(givenList)
main()