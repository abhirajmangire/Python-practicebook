# to print the length of a list
subjects = ["OS", "DSA", "SE" ,"EvS","DBMS"]
days = ["monday","tuesday","wednesday","thrusday","friday","saturday","sunday"]

def Print_len(list):
    print(len(list))

Print_len(subjects)
Print_len(days)


#to print the elements of a list in a single line
def print_el(list):
    for i in range(len(list)):
        print(list[i])
print_el(subjects)
print_el(days)