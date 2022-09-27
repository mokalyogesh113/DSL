def binary_search(arr,key):
    
    start=0
    end=len(arr)-1
    while start <=end:
        mid=(start+end)//2;
        if(arr[mid]>key):
            end=mid-1
        elif(arr[mid]<key):
            start=mid+1
        else:
            return mid
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

index=binary_search(arr,key)

if(index<0):
    print("\n",key," was not found")
else:
    print("\nThe name of the person is ",dict1[key])