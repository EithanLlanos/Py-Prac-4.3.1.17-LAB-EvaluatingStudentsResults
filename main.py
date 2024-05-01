# Scenario
# Prof. Jekyll conducts classes with students and regularly makes notes in a text file. Each line of the file contains three elements: the student's first name, the student's last name, and the number of point the student received during certain classes.

# The elements are separated with white spaces. Each student may appear more than once inside Prof. Jekyll's file.

# The file may look as follows:

# John	Smith	5
# Anna	Boleyn	4.5
# John	Smith	2
# Anna	Boleyn	11
# Andrew	Cox	1.5
# samplefile.txt

# Your task is to write a program which:

# asks the user for Prof. Jekyll's file name;
# reads the file contents and counts the sum of the received points for each student;
# prints a simple (but sorted) report, just like this one:
# Andrew Cox 	 1.5
# Anna Boleyn 	 15.5
# John Smith 	 7.0
# output

# Note:

# your program must be fully protected against all possible failures: the file's non-existence, the file's emptiness, or any input data failures; encountering any data error should cause immediate program termination, and the erroneous should be presented to the user;
# implement and use your own exceptions hierarchy - we've presented it in the editor; the second exception should be raised when a bad line is detect, and the third when the source file exists but is empty.
# Tip: Use a dictionary to store the students' data.


##########################################################################################


# class StudentsDataException(Exception):
#     pass


# class BadLine(StudentsDataException):
#     # Write your code here.


# class FileEmpty(StudentsDataException):
#     # Write your code here.

##########################################################################################

class StudentsDataException(Exception):
    def __init__ (self, message = "An error with the student's data has occured "):
        self.message = message
        super().__init__(self.message)


class BadLine(StudentsDataException):
    def __init__(self,message = "Invalid line in the student's data "):
        self.message = message
        super().__init__(self.message)


class FileEmpty(StudentsDataException):
    def __init__(self,message = "Student's data file is empty "):
        self.message = message
        super().__init__(self.message)
        

try:
    file = open(input("Please enter the file's name:"), "rt", encoding = "utf-8")
    rl = file.readline()
    if not rl:
        raise FileEmpty()
except IOError as e:
    print(IOError)
    exit()
except FileEmpty as e:
    print(e.message + f' "{file.name}"' )
    exit()

dic = {}
try:
    ct = 1
    while rl:
        lis = rl.split(maxsplit=2)
        dic[f"{lis[0]} {lis[1]}"] = round(dic.get(f"{lis[0]} {lis[1]}",0) + float(lis[2]),3)
        rl = file.readline()
        ct+=1
except Exception:
    error = BadLine().message
    print(error + f" : {ct}")
    exit()

for k , v in dic.items():
    print(f"{k:<15} {v}")