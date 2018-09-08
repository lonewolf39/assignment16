#Q.1- Take students name and marks
import pymongo
client=pymongo.MongoClient()
database=client['Students']
collection=database['student']
#Q.2- Append the values in 2 columns
for i in range(10):
    try:
        name = input("Enter the name: ") 
        marks = int(input('Enter your Marks: '))
        if(marks<0 or marks >100):  
            raise ValueError('Invalid entry of marks')
            i=i-1
        else:#Q.3- Create a Database of students
            collection.insert_one({'Name':name,'Marks':marks})  
            i=i+1
    except  ValueError as msg:
        print(msg)
#Q.4- Print the names of all students who scored more than 80 marks
db=collection.find({"Marks":{"$gt":80}})
for data in db:
    print(data)
