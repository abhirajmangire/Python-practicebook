#to enter marks of 3 subject from the user and store them in a dictionary . start with an empty dictionary And add one by one .use subject names as key and marks as value
marks ={}

x= int(input("Enter marks for phy: "))
marks.update({"phy": x})

x= int(input("Enter marks for chem: "))
marks.update({"chem":x})

x= int(input("Enter marks for maths: "))
marks.update({"maths":x})

print(marks)
 