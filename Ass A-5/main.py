
# Display Word With Longest Length
def longestWord():
    print("\tProgram to display word with longest length\n")
    str1 = input("Enter the String :- ")
    slist = str1.split()
    large = ''
    for word in slist:
        if len(large) < len(word):
            large = word
    print("the word with largest length is :- ", large, "\n")


# frequency of occurance of particular character
def freqOfChar():
    print("\tProgram to Find frequency of occurance of particular character\n")
    str1 = input("Enter the String :- ")
    key = input("Enter the character ")
    count = 0
    for i in str1:
        if i == key:
            count += 1
    print("The Occurance of '", key,
          "' in the given string is ", count, " times\n")


# Check Whether Given string is palindrom or not
def isPalindrome():
    print("\tProgram to Check whether the given string is palindrome or not\n")

    str1 = input("\nEnter the Sting :- ")
    if (str1 == str1[::-1]):
        print("String is palindrome")
    else:
        print("string is not palindrome")


# to display index of first appearance of substring
def findSubstr():
    print("\tProgram to display index of first appearance of substring\n")
    str1 = input("Enter the String :- ")
    str2 = input("Enter the Substring:-  ")
    index = -1
    for i in range(len(str1)-len(str2)):
        if str1[i:i+len(str2)] == str2:
            index = i
            break
    print("The index of first appearance of ' ", str2, "' is ", index)


# to Count occurance of each word in a given string
def countOfWords():
    print("\tProgram to Count occurance of each word in a given string\n")
    str1 = input("Enter the String :- ")
    slist = str1.split()

    sdict = {}

    for word in slist:
        if word in sdict:
            sdict[word] += 1
        else:
            sdict[word] = 1

    print(sdict)


#===========main==========#

while (1):
    print("\n\n****************** M e n u ******************\n")
    print("1. Display the word with the longest length ")
    print("2. Determine the frequency of occurance of particular character in string ")
    print("3. Check whether given string is palindrome or not ")
    print("4. Display index of first appearance of the substring ")
    print("5. count the occurrences of each word in a given string")
    print("0. Exit")
    choice = int(input("Enter Choice:- "))
    print("\n******************************************************")
    if choice == 1:
        longestWord()
    elif choice == 2:
        freqOfChar()
    elif choice == 3:
        isPalindrome()
    elif choice == 4:
        findSubstr()
    elif choice == 5:
        countOfWords()
    elif choice == 0:
        break
    else:
        print("Wrong Choice")
