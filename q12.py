#to count the number of students 
#with the "A grade in the following 
# tuple" and to store the value in 
# list  and sort them in "a" to "d" 
# order

grades = ("A", "B", "C", "D", "A", "B", "A", "C")
count=grades.count("A")
final_grades = list(grades)
final_grades.sort()
print(final_grades)