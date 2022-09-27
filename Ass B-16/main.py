def partition(Array, low, up):
    i = low
    j = up
    pivot = Array[low]
    while (i <= j):
        while (Array[i] < pivot and i < up):
            i += 1
        while (Array[j] > pivot):
            j -= 1
        if (i < j):
            Array[i], Array[j] = Array[j], Array[i]
            i += 1
            j -= 1
        else:
            i += 1
            Array[low] = Array[j]
            Array[j] = pivot
    return j


def quick(Array, low, up):
    if (low >= up):
        return 0
    pivot = partition(Array, low, up)
    quick(Array, low, pivot-1)  # Left Subarray
    quick(Array, pivot+1, up)  # Right Subarray


n = int(input("Enter the Number of Students "))
Array = []
for i in range(1, n+1):
    ele = int(input("Enter the Percentage of student :-"))
    Array.append(ele)

low = 0
up = len(Array)-1
quick(Array, low, up)
print("\n\nPercentage of students in Ascending order is ")
for i in Array:
    print(i, end="  ")

print("\nTop students are:- ")
for i in range(min(5, len(Array))):
    print(Array[i], end=" ")
