def Fib_search(arr,key):
    n=len(arr)
    fibMM2= 0
    fibMM1=1
    fibM=fibMM2 + fibMM1
    while(fibM < n):
        fibMM2=fibMM1
        fibMM1=fibM
        fibM = fibMM2 + fibMM1
    offset=-1
    while(fibM > 1):
        i=min(offset+fibMM2 , n-1)
        if(arr[i] < key):
            fibM=fibMM1
            fibMM1 = fibMM2
            fibMM2 = fibM - fibMM1
            offset = i
        elif(arr[i]>key) :
            fibM=fibMM2
            fibMM1 = fibMM1 - fibMM2
            fibMM2 = fibM - fibMM1
        else:
            return i
        
    if(fibMM1 and arr[n-1] == key):
        return n-1
        
    return -1
        
    
#===========main==========#
dict1={}
print("\n\n(NOTE:-Type 'Exit' to end the data entry)")
while True:
    data=input("Enter name and mobile number seperated by comma  ")
    if(data=='Exit'):
        break;
    name,num=data.split(",")
    num=int(num)
    dict1[num]=name
list1=dict1.keys()
arr=list(list1)
arr.sort()

key=int(input("\nEnter the number to search for "))

index=Fib_search(arr,key)

if(index<0):
    print("\n",key," was not found")
else:
    print("\nThe name of the person is ",dict1[key])
