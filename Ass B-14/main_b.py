def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(n-i-1):
            if (arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


#===========main==========#
arr1 = []

num = int(input("Enter the Number of students :-  "))
for i in range(num):
    per = float(input("Enter the percentage :- "))
    arr1.append(per)

bubble_sort(arr1)

print("sorted array is :- ")
for i in range(num):
    print(arr1[i])
