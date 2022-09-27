def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if (arr1[min] > arr1[j]):
                min = j
        arr[i], arr[min] = arr[min], arr[i]


#===========main==========#
arr1 = []

num = int(input("Enter the Number of students :-  "))
for i in range(num):
    per = float(input("Enter the percentage :- "))
    arr1.append(per)

selection_sort(arr1)

print("sorted array is :- ")
for i in range(num):
    print(arr1[i])
