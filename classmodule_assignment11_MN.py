# Megan Noel
# CPDM 120
# Assignment 11 Class Module

# This module contains 3 classes ( Person, Student and Graduate ) and demonstrates use of inheritance, encapsulation and polymorphism

class Person():
    intPersons = 0

    def __init__(self, firstname, lastname, age, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        Person.intPersons += 1
    
    @property
    def firstname(self):
        return self.__firstname
    
    @firstname.setter
    def firstname(self, firstname):
        if not firstname.isalpha():
            raise Exception("First name cannot contain numbers")
        else:
            self.__firstname = firstname
   
    @property
    def lastname(self):
        return self.__lastname
    
    @lastname.setter
    def lastname(self, lastname):
        if not lastname.isalpha():
            raise Exception("Last name cannot contain numbers")
        else:
            self.__lastname = lastname

    @property
    def age(self):
        return self.__age 
    
    @age.setter
    def age(self, age):
        try:
            age = int(age) 
            if age > 0:
                self.__age = age
            else:
                raise Exception("Age must be greater than 0")
        except:
            raise Exception("Age must be a positive integer")
        
    @property
    def gender(self):
        return self.__gender
    
    @gender.setter
    def gender(self, gender):
            if gender in ["Male", "Female"]:
                self.__gender = gender
            else:
                raise Exception("Gender must either be 'Male' or 'Female'")


class Student(Person):

    intFemaleStudents = 0
    intMaleStudents = 0
    dblTotalGPA = 0.0
    intTotalMaleAge = 0
    intTotalFemaleAge = 0

    def __init__(self, firstname, lastname, age, gender, gpa):
        Person.__init__(self, firstname, lastname, age, gender)
        self.gpa = gpa
        Student.dblTotalGPA += self.gpa
    
    @property
    def gpa(self):
        return self.__gpa
    
    @gpa.setter
    def gpa(self, gpa):
        try:
            gpa = float(gpa)  
            if gpa > 0 and gpa <= 4.0:
                self.__gpa = gpa
            else:
                raise Exception("GPA must be between 0 and 4.0")
        except:
            raise Exception("GPA must be numerical")

    def TotalStudentByGender(self):
        if self.gender == "Male":
            Student.intMaleStudents += 1
        elif self.gender == "Female":
            Student.intFemaleStudents += 1

    def AccumulateAgeByGender(self):
        if self.gender == "Male":
            Student.intTotalMaleAge += self.age
        elif self.gender == "Female":
            Student.intTotalFemaleAge += self.age

    def AverageGPA():
        dblAvgGPA =  Student.dblTotalGPA / Student.intPersons
        return '{:2,.2f}'.format(dblAvgGPA)
    
    def AverageAgeOfMales():
         if Student.intMaleStudents > 0:
            dblAvgMaleAge = Student.intTotalMaleAge / Student.intMaleStudents
         else:
            dblAvgMaleAge = 0
         return '{:2,.2f}'.format(dblAvgMaleAge)
    
    def AverageAgeOfFemales():
        if Student.intFemaleStudents > 0:
            dblAvgFemaleAge = Student.intTotalFemaleAge / Student.intFemaleStudents
        else:
            dblAvgFemaleAge = 0
        return '{:2,.2f}'.format(dblAvgFemaleAge)
    
    def OverallGPA(self, gpa1, creditHours1, gpa2 = 0.0, creditHours2 = 0, gpa3 = 0.0, creditHours3 = 0, gpa4 = 0.0, creditHours4 = 0, gpa5 = 0.0, creditHours5 = 0):
        if gpa2 > 0:
            if creditHours2 == 0:
                raise Exception("Credit Hours for all classes must be entered")
        if gpa3 > 0:
            if creditHours3 == 0:
                raise Exception("Credit Hours for all classes must be entered")
        if gpa4 > 0:
            if creditHours4 == 0:
                raise Exception("Credit Hours for all classes must be entered")
        if gpa5 > 0:
            if creditHours5 == 0:
                raise Exception("Credit Hours for all classes must be entered")
            
        
        dlbOverallGPA = ((gpa1 * creditHours1) + (gpa2 * creditHours2) + (gpa3 * creditHours3) + (gpa4 * creditHours4) + (gpa5 * creditHours5)) / (creditHours1 + creditHours2 + creditHours3 + creditHours4 +creditHours5)
        strOverallGPA = "{:.2f}".format(dlbOverallGPA)
        print("Overall GPA is: ", strOverallGPA)

class Graduate(Student):

    intFemalesWithJobs = 0
    intMalesWithJobs = 0
    
    def __init__(self, firstname, lastname, age, gender, gpa, gradyear, jobstatus):  
        self.gradyear = gradyear
        self.jobstatus = jobstatus   
        super().__init__(firstname, lastname, age, gender, gpa)
        self.TotalStudentByGender()
        self.AccumulateAgeByGender()
        self.strTotalGrads = "Total number of graduates: " + str(Graduate.intPersons)

    @property 
    def jobstatus(self):
        return self.__jobstatus

    @jobstatus.setter
    def jobstatus(self, jobstatus):
           if jobstatus in ["Y", "N"]:
                self.__jobstatus = jobstatus
           else:
                raise Exception("Please enter either 'Y' or 'N' for job status")
           
    @property
    def gradyear(self):
        return self.__gradyear
    
    @gradyear.setter
    def gradyear(self, gradyear):
        try:
            gradyear = int(gradyear)
            if 1930 <= gradyear <= 2050:
                self.__gradyear = gradyear
            else:
                raise Exception("Grad year must be between 1930 and 2050")
        except ValueError:
            raise Exception("Grad year must be a numerical value")
                
    def TotalStudentByGender(self):
         if self.jobstatus == "Y":
            if self.gender == "Male":
                Graduate.intMalesWithJobs += 1
            elif self.gender == "Female":
                Graduate.intFemalesWithJobs += 1

         if self.gender == "Male":
             Student.intMaleStudents += 1
         elif self.gender == "Female":
             Student.intFemaleStudents += 1

    def __str__(self):
        return self.strTotalGrads
    

