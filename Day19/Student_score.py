"""
Problem:
The provided code stub will read in a dictionary containing key/value pairs of name:[marks]
 for a list of students. Print the average of the marks array for the student name provided,
   showing 2 places after the decimal."""

"""Input Format:

The first line contains the integer , 
the number of students' records. 
The next  lines contain the names and marks obtained by a student,
 each value separated by a space. The final line contains query_name, 
 the name of a student to query."""

"""Sample input:
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
"""

# if __name__ == '__main__':
#     n = int(input("Number of students"))  
#     student_data = {} 
    
  
#     for _ in range(n):
#       data = input("Enter you marks: ").split()

#       name=data[0]
#       marks=[float(data[1]),float(data[2]),float(data[3])]
#       student_data[name]=marks
    
# search_name = input("Enter name to see average: ")

# student_marks = student_data[search_name]

# average= sum(student_marks)/3

# print(f"Average: {average}")

# I put the above code on chat gpt and they ask why they not work on they hackerrank
# they tell i write in custom way and also not take exactly after .2 values    
if __name__ == '__main__':
    n = int(input())  
    student_data = {} 
    
    for _ in range(n):
        data = input().split()
        name = data[0]
        marks = [float(data[1]), float(data[2]), float(data[3])]
        student_data[name] = marks
    
    search_name = input()
    student_marks = student_data[search_name]
    average = sum(student_marks) / 3
    print("{:.2f}".format(average))  # Print average with 2 decimal places
