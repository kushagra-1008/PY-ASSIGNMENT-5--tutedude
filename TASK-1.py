dictionary = {'Alice':85 , 'Bob': 82 , 'Charlie':89 , 'Daniel': 54}

name = input("Enter student's name: ")
marks = dictionary.get(name)
# print(marks)

if marks==None:
    print("Student not found")

else :
    print(marks)    