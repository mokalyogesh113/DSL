FDS=[]
print("Enter the Marks of the students \n(press A for Absent Student) \n(press N for end) \n")
temp=input()
while (temp!='N'):
    if temp.isnumeric():
        FDS.append(int(temp))
    else:
        FDS.append(temp)
    temp=input()
    
sum=0
ab=0
max=FDS[0]
min=FDS[0]
n=0
freq=0
for marks in FDS:
    n+=1
    if(marks!='A'):
        sum+=marks
        if marks>max:   #to calc. maximum marks
            freq=1
            max=marks
        elif(marks==max):   #to find the frequency of maximum marks
            freq+=1

        if marks<min:   #to calc. minimum marks
            min=marks
    else:
        ab+=1
    
avg=sum/n

print("Absent students are: " ,ab)
print("max highest marks of the student is : ",max)
print("The frequency of students scored maximum marks is ",freq)
print("minimum marks of student is ",min)
print("the average marks of all students is ",avg)
