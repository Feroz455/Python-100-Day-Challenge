student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56, 76, 98]
}
#looping through dictionaries

for (key , value) in student_dict.items():
    print(value)
import pandas 
student_data = pandas.DataFrame(student_dict)
print(student_data)