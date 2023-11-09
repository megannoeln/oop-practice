# Megan Noel
# CPDM 120
# Assignment 11

# OOP Inheritance, Encapsulation, and Polymorphism


from classmodule_assignment11_MN import Person, Student, Graduate


objGrad1 = Graduate("Megan", "Nicole", 26, "Female", 4.0, 2016, "Y")
objGrad2 = Graduate("Wasabi", "Green", 28, "Male", 3.0, 2019, "N")
objGrad3 = Graduate("Jade", "Joy", 30, "Female", 2.0, 2014, "Y")
objGrad4 = Graduate("Jasper", "Noel", 34, "Male", 3.5, 2016, "Y")
objGrad5 = Graduate("Ophelia", "White", 40, "Female", 4.0, 2020, "N")


print(objGrad5)
print("Average GPA of Grads: ",  str(Graduate.AverageGPA()))
print("Total Male Graduated Students:",  str(Graduate.intMaleStudents))
print("Total Female Graduated Students:",  str(Graduate.intFemaleStudents))
print("Average Age of Graduated Male Students: ",  str(Graduate.AverageAgeOfMales()))
print("Average Age of Graduated Female Students: ",  str(Graduate.AverageAgeOfFemales()))
print(str(Graduate.intMalesWithJobs),  " Male Graduates have jobs")
print(str(Graduate.intFemalesWithJobs), " Female Graduates have jobs")

objGrad5.OverallGPA(4.0, 3, 3.0, 4)