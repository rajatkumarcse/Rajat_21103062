# Question ---> 1

# To find average of three numbers

a = input("Enter your first number :")
b = input("Enter your second number :")
c = input("Enter your third number :")
d = (int(a) + int(b) + int(c))/3

print("The average of three numbers is :")
print(float(d))




# Question ---> 2

# To compute a person's income tax
# All the values are in $

Standard_Deduction = 10000
Dependent_Deduction = 3000
Tax_Rate = 0.2
Gross_Income = input("Enter your gross income :")
Number_of_Dependents = input("Enter your number of dependents :")

Taxable_Income = int(Gross_Income) - int(Standard_Deduction) - (int(Dependent_Deduction) * int(Number_of_Dependents))

Tax = (float(Taxable_Income) * 0.2)

print("Your income tax is :")
print(float(Tax))




# Question ---> 3

# Student's general data

SID = input("Enter your SID :")
Name = input("Enter your name :")
Gender = input("Enter your gender :")
Course_Name = input("Enter your course_name :")
CGPA = input("Enter your CGPA :")

Student = (int(SID), Name, Gender, Course_Name, float(CGPA))
print(Student)





# Question ---> 4

# Making list of marks of 5 different students

marks = []
for i in range(5):
    marks.append(input("Enter marks of student :"))
marks.sort()
print(marks)





# Question ---> 5

# Making the list of colors

# Part (a)
colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

for color in colors:
    if color == 'Black':
        continue;
    print(color)


# Part (b)
colors[3:5] = ['Purple']
print(colors)

