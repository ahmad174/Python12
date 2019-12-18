# Python Project Two
""" 
	Done by:
		Ahmad Taha
		Ayham Zaid
"""
import json
from functools import reduce
from tkinter import *
from tkinter.scrolledtext import ScrolledText
# Classes
class Person:
	def __init__(self, name, address):
		self._name = str(name)
		self._address = str(address)
		
	def getName(self):
		return self._name
	
	def setName(self, name):
		self._name = str(name)
		
	def getAddress(self):
		return self._address
	
	def setAddress(self, address):
		self._address = address
#==============================================================================
class Employee(Person):
	def __init__(self, name, address, number, salary, jobTitle, loans):
		super().__init__(name, address)
		self.number = int(number)
		self.__salary = float(salary)
		self.__jobTitle = str(jobTitle)
		self.__loans = list(loans)
		
	def getSalary(self):
		return self.__salary
	
	def setSalary(self, salary):
		self.__salary = float(salary)
		
	def getJobTitle(self):
		return self.__jobTitle
		
	def setJobTitle(self, jobTitle):
		self.__jobTitle = jobTitle
		
	def getLoans(self):
		return self.__loans
		
	def getTotalLoans(self):
		totalLoans = sum(self.__loans)
		return totalLoans
		
	def getMaxLoan(self):
		length = len(self.__loans)
		maxLoan = max(self.__loans) if length > 0 else 0
		return maxLoan  
		
	def getMinLoan(self):
		length = len(self.__loans)
		minLoan = min(self.__loans) if length > 0 else 0 
		return minLoan 
		
	def setLoans(self, loans):
		self.__loans = list(loans)
		
	def setNewLoan(self, loan):
		self.__loans.append(int(loan))
		
	def printInfo(self):
		return f"""EMPLOYEE NUMBER {self.number}
Name: {self._name}
Job Title: {self.__jobTitle}
Salary = {self.__salary}JOD
Loans: {self.__loans}
	Total Loans = {self.getTotalLoans()}
Address: {self._address}
"""
#==============================================================================
class Student(Person):
	def __init__(self, name, address, number, subject, marks):
		super().__init__(name, address)
		self.number = number
		self.__subject = str(subject)
		self.__marks = dict(marks)
		
	def getSubject(self):
		return self.__subject
	
	def setSubject(self, subject):
		self.__subject = str(subject)
		
	def getMarks(self):
		return self.__marks
	
	def getMarksFormatted(self):
		result = ''
		for subject, mark in self.__marks.items():
			result = result + '   ' + subject + ' : ' + str(mark) + '\n' 
		return result
	
	def setMarks(self, marks):
		self.__marks = dict(marks)
		
	def setNewMark(self, subject, mark):
		self.__marks[str(subject)] = int(mark)
		
	def getAvg(self):
		numberOfSubjects = len(self.__marks)
		summation = sum(self.__marks.values())
		avg = round(summation / numberOfSubjects, 2)
		return avg
		
	def getAMarks(self):
		aces = list(filter(lambda mark: mark[1] >= 90, self.__marks.items()))
		return aces
	
	def printInfo(self):
		return f"""STUDENT NUMBER {self.number}
Name: {self._name}
Subject: {self.__subject}
Marks:
	{self.getMarksFormatted()}
Average = {self.getAvg()}/100
"""		
#==============================================================================
#==============================================================================
#==============================================================================
# Functions
def information(array, title):
	result = 'ALL ' + str(title).upper() + ' INFORMATION:\n'
	for item in array:
		result = result + item.printInfo()
		
	return result + '\n\n'
#==============================================================================		
def loansInformation(employees):
	result = 'LOANS INFORMATION:\n'
	grandTotal = 0
	for employee in employees:
		result = result + 'Employee Name: ' + employee.getName() + '\n' + 'Loans: ' + str(employee.getLoans()) + '\n'
		grandTotal = grandTotal + employee.getTotalLoans()
		result = result + 'Total Loans = ' + str(employee.getTotalLoans()) + '\n\n'
		
	result = result + 'Grand Total = ' + str(grandTotal) + '\n\n'
	return result
#==============================================================================
def loansDictionary(employees):
	loansDic = {}
	for employee in employees:
		loansDic[str(employee.number)] = employee.getLoans()
		
	return loansDic 
#==============================================================================
def highestLoan(loans):
	if(len(loans) == 0): 
		return 0
	
	highest = reduce(lambda highest, loan: 
		highest if highest > loan else loan, loans)
		
	return highest
#==============================================================================
def lowestLoan(loans):
	if(len(loans) == 0): 
		return 0
	
	lowest = reduce(lambda lowest, loan: 
		lowest if lowest < loan else loan, loans)
		
	return lowest
#==============================================================================
def AStudents(students):
	result = 'A STUDENTS ARE:\n'
	for student in students:
		if(len(student.getAMarks()) > 0):
			result = result + 'Name: ' + student.getName() + '\n' + 'Subject: ' + student.getSubject() + '\nMarks:\n' 
			for subject, mark in student.getMarks().items():
				result = result + '   ' + subject + ' : ' + str(mark) + '\n\n'
			
	return result
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
#WINDOWS
def report():
	global employees, students
	reportWindow = Toplevel(company)
	reportWindow.title('Report')
	reportWindow.geometry('800x600')
	
	data = ScrolledText(reportWindow, width=111, height=54)
	
	numOfEmployees = str(len(employees))
	numOfStudents = str(len(students))
	data.insert(END, 'Number of Employees = ' + numOfEmployees + '\n')
	data.insert(END, 'Number of Students = ' + numOfStudents + '\n\n\n')
	
	data.insert(END, information(employees, 'employees') + '\n\n\n')
	data.insert(END, information(students, 'students') + '\n\n\n')
	
	highestAvg = reduce(lambda avg, student: avg if(avg > student.getAvg()) else student.getAvg(), students, 0)
	data.insert(END, 'The Highest Average = ' + str(highestAvg) + '\n\n\n' )
	
	maximumLoan = reduce(lambda loan, employee: loan if(loan > employee.getMaxLoan()) else employee.getMaxLoan(), employees, 0)
	minimumLoan = reduce(lambda loan, employee: loan if(loan < employee.getMinLoan()) else loan if(employee.getMinLoan() == 0) else employee.getMinLoan(), employees, maximumLoan)
	data.insert(END, 'The Maximum Loan = ' + str(maximumLoan) + '\n\n\n' )
	data.insert(END, 'The Minimum Loan = ' + str(minimumLoan) + '\n\n\n' )
	
	data.insert(END, loansInformation(employees) + '\n\n\n')
	
	loansData = loansDictionary(employees)
	data.insert(END, str(loansDictionary(employees)) + '\n\n\n')
	
	for number, loans in loansData.items():
		highest = highestLoan(loans)
		lowest = lowestLoan(loans)
		data.insert(END, 'The Highest Loan for Employee Number' + str(number) + ' = ' + str(highest) + '\n\n')
		data.insert(END, 'The Lowest Loan for Employee Number' + str(number) + ' = ' + str(lowest) + '\n\n')
		
	data.insert(END, AStudents(students) + '\n\n')
	
	highestSalary = reduce(lambda salary, employee: salary if (salary > employee.getSalary()) else employee.getSalary(), employees, 0)
	lowestSalary = reduce(lambda salary, employee: salary if (salary < employee.getSalary()) else salary if (employee.getSalary() == 0) else employee.getSalary(), employees, highestSalary)
	totalSalaries = reduce(lambda salary, employee: salary + employee.getSalary(), employees, 0)
	salariesData = f"""SALARIES:
The Highest Salary = {highestSalary}JOD
The Lowest Salary = {lowestSalary}JOD
Total Salaries = {totalSalaries}JOD
""" 
	data.insert(END, salariesData +'\n')
	
	data.grid(column=0,row=0)
#==============================================================================
#==============================================================================
def addEmployee():
	def add():
		global employees
		number = int(numberValue.get()); numberValue.set('')
		name = nameValue.get(); nameValue.set('')
		jobTitle = jobTitleValue.get(); jobTitleValue.set('')
		salary = salaryValue.get(); salaryValue.set('')
		
		if len(loansValue.get()) == 0:
			loans = []
		else:
			loans = [int(loan) for loan in loansValue.get().split(' ')]; loansValue.set('')
		
		address = addressValue.get(); addressValue.set('')
		
		employees.append(Employee(name, address, number, salary,jobTitle, loans))
		msgValue.set('Employee '+ str(number) +' has been added successfully.')
		
	addEmployeeWindow = Toplevel(company)
	addEmployeeWindow.title('Add Employee')
	addEmployeeWindow.geometry('800x600')

	xLabel = 250
	xInput = xLabel + 125
	
	yLabel = 200
	yInput = yLabel + 7
	
	numberLabel = Label(addEmployeeWindow, text = 'Number: ', font=('arial', 12, 'bold')).place(x=xLabel ,y=yLabel)
	numberValue = StringVar()
	numberInput = Entry(addEmployeeWindow, textvariable=numberValue).place(x=xInput ,y=yInput)
	
	nameLabel = Label(addEmployeeWindow, text = 'Name: ', font=('arial', 12, 'bold')).place(x=xLabel ,y=yLabel+25)
	nameValue = StringVar()
	nameInput = Entry(addEmployeeWindow, textvariable=nameValue).place(x=xInput ,y=yInput+25)
	
	jobTitleLabel = Label(addEmployeeWindow, text = 'Job Title: ', font=('arial', 12, 'bold')).place(x=xLabel ,y=yLabel+50)
	jobTitleValue = StringVar()
	jobTitleInput = Entry(addEmployeeWindow, textvariable=jobTitleValue).place(x=xInput ,y=yInput+50)
	
	salary = Label(addEmployeeWindow, text = 'Salary: ', font=('arial', 12, 'bold')).place(x=xLabel ,y=yLabel+75)
	salaryValue = StringVar()
	salaryInput = Entry(addEmployeeWindow, textvariable=salaryValue).place(x=xInput ,y=yInput+75)
	
	loansLabel =Label(addEmployeeWindow, text = 'Loans: ', font=('arial', 12, 'bold')).place(x=xLabel ,y=yLabel+100)
	loansValue = StringVar()
	loansInput = Entry(addEmployeeWindow, textvariable=loansValue).place(x=xInput ,y=yInput+100)
	
	addressLabel = Label(addEmployeeWindow, text = 'Address: ', font=('arial', 12, 'bold')).place(x=xLabel ,y=yLabel+125)
	addressValue = StringVar()
	addressInput = Entry(addEmployeeWindow, textvariable=addressValue).place(x=xInput ,y=yInput+125)
	
	addEmployeeButton = Button(addEmployeeWindow, text='Add Employee', command=add).place(x=xLabel+75 ,y=yLabel+175)

	msgValue = StringVar()
	msg = Label(addEmployeeWindow, textvariable=msgValue).place(x=xLabel+17 ,y=yLabel+200)
#==============================================================================		
def viewEmployees():
	global employees
	viewEmployeeWindow = Toplevel(company)
	viewEmployeeWindow.title('View Employees')
	viewEmployeeWindow.geometry('800x600')
	
	data = ScrolledText(viewEmployeeWindow, width=111, height=54)
	
	for employee in employees:
		data.insert(END, employee.printInfo() + '\n\n')
		
	data.grid(column=0,row=0)
#==============================================================================		
def deleteEmployee():
	def delete():
		global employees
		number = int(numberValue.get()); numberValue.set('')
		if len(employees) == 0: messagebox.showinfo('Message','This Employee Number DOES NOT EXIST')
		for index in range(len(employees)):
			if(employees[index].number == number):
				employees.pop(index)
				msgValue.set('Employee '+ str(number) +' has been deleted successfully.')
				break
			else: messagebox.showinfo('Message','This Employee Number DOES NOT EXIST')
	
	xLabel = 250
	xInput = xLabel + 125
	
	yLabel = 265
	yInput = yLabel + 7
	
	deleteEmployeeWindow = Toplevel(company)
	deleteEmployeeWindow.title('Delete Employee')
	deleteEmployeeWindow.geometry('800x600')
	
	numberLabel = Label(deleteEmployeeWindow, text = 'Number: ', font=('arial', 12, 'bold')).place(x=xLabel ,y=yLabel)
	numberValue = StringVar()
	numberInput = Entry(deleteEmployeeWindow, textvariable=numberValue).place(x=xInput ,y=yInput)
	
	deleteEmployeeButton = Button(deleteEmployeeWindow, text='Delete Employee', command=delete).place(x=xLabel+75 ,y=yLabel+35)

	msgValue = StringVar()
	msg = Label(deleteEmployeeWindow, textvariable=msgValue).place(x=xLabel+17 ,y=yLabel+70)
#==============================================================================
#==============================================================================		
def addStudent():
	def add():
		global students
		number = int(numberValue.get()); numberValue.set('')
		name = nameValue.get(); nameValue.set('')
		subject = subjectValue.get(); subjectValue.set('')
		marks = json.loads(marksValue.get()); marksValue.set('')
		address = addressValue.get(); addressValue.set('')
		students.append(Student(name, address, number,subject, marks))
		msgValue.set('Student '+ str(number) +' has been added successfully.')
		
	addStudentWindow = Toplevel(company)
	addStudentWindow.title('Add Student')
	addStudentWindow.geometry('800x600')
	
	xLabel = 250
	xInput = xLabel + 125
	
	yLabel = 225
	yInput = yLabel + 7
	
	numberLabel = Label(addStudentWindow, text = 'Number: ', font=('arial', 12, 'bold')).place(x=xLabel ,y=yLabel)
	numberValue = StringVar()
	numberInput = Entry(addStudentWindow, textvariable=numberValue).place(x=xInput ,y=yInput)
	
	nameLabel = Label(addStudentWindow, text = 'Name: ', font=('arial', 12, 'bold')).place(x=xLabel ,y=yLabel+25)
	nameValue = StringVar()
	nameInput = Entry(addStudentWindow, textvariable=nameValue).place(x=xInput ,y=yInput+25)
	
	subjectLabel = Label(addStudentWindow, text = 'Subject: ', font=('arial', 12, 'bold')).place(x=xLabel ,y=yLabel+50)
	subjectValue = StringVar()
	subjectInput = Entry(addStudentWindow, textvariable=subjectValue).place(x=xInput ,y=yInput+50)
	
	marksLabel =Label(addStudentWindow, text = 'Marks: ', font=('arial', 12, 'bold')).place(x=xLabel ,y=yLabel+75)
	marksValue = StringVar()
	marksInput = Entry(addStudentWindow, textvariable=marksValue).place(x=xInput ,y=yInput+75)
	
	addressLabel = Label(addStudentWindow, text = 'Address: ', font=('arial', 12, 'bold')).place(x=xLabel ,y=yLabel+100)
	addressValue = StringVar()
	addressInput = Entry(addStudentWindow, textvariable=addressValue).place(x=xInput ,y=yInput+100)
	
	addStudentButton = Button(addStudentWindow, text='Add Student', command=add).place(x=xLabel+75 ,y=yLabel+150)

	msgValue = StringVar()
	msg = Label(addStudentWindow, textvariable=msgValue).place(x=xLabel+17 ,y=yLabel+175)
#==============================================================================
def viewStudents():
	global students
	viewStudentWindow = Toplevel(company)
	viewStudentWindow.title('View Students')
	viewStudentWindow.geometry('800x600')

	data = ScrolledText(viewStudentWindow, width=111, height=54)
	
	for student in students:
		data.insert(END, student.printInfo() + '\n\n\n')
		
	data.grid(column=0,row=0)
#==============================================================================
def deleteStudent():
	def delete():
		global students
		number = int(numberValue.get()); numberValue.set('')
		if len(students) == 0: messagebox.showinfo('Message','This Student Number DOES NOT EXIST')
		for index in range(len(students)):
			if(students[index].number == number):
				students.pop(index)
				msgValue.set('Student '+ str(number) +' has been deleted successfully.')
				break
			else: messagebox.showinfo('Message','This Student Number DOES NOT EXIST')

	deleteStudentWindow = Toplevel(company)
	deleteStudentWindow.title('Delete Student')
	deleteStudentWindow.geometry('800x600')
	
	xLabel = 250
	xInput = xLabel + 125
	
	yLabel = 265
	yInput = yLabel + 7
		
	numberLabel = Label(deleteStudentWindow, text = 'Number: ', font=('arial', 12, 'bold')).place(x=xLabel ,y=yLabel)
	numberValue = StringVar()
	numberInput = Entry(deleteStudentWindow, textvariable=numberValue).place(x=xInput ,y=yInput)
	
	deleteStudentButton = Button(deleteStudentWindow, text='Delete Student', command=delete).place(x=xLabel+75 ,y=yLabel+35)

	msgValue = StringVar()
	msg = Label(deleteStudentWindow, textvariable=msgValue).place(x=xLabel+17 ,y=yLabel+70)
#==============================================================================
#==============================================================================
def about():
	messagebox.showinfo('Message','OOP Second Project')
#==============================================================================
#==============================================================================
#==============================================================================
#MAIN LOOP
employees=[]
students=[]

company = Tk()
company.title('Company Profiles')
company.geometry('1920x1800')

top = Menu(company)
top.config(background='white')
company.config(menu=top)

file = Menu(top, tearoff=0)
file.add_command(label='Report', command=report)
file.add_separator()
file.add_command(label='Exit', command=company.destroy)

employeesMenu = Menu(top, tearoff=0)
employeesMenu.add_command(label='Add', command=addEmployee)
employeesMenu.add_command(label='View', command=viewEmployees)
employeesMenu.add_command(label='Delete', command=deleteEmployee)

studentsMenu = Menu(top, tearoff=0)
studentsMenu.add_command(label='Add', command=addStudent)
studentsMenu.add_command(label='View', command=viewStudents)
studentsMenu.add_command(label='Delete', command=deleteStudent)

helpMenu = Menu(top, tearoff=0)
helpMenu.add_command(label='About', command=about)

top.add_cascade(label='File', menu=file)
top.add_cascade(label='Employees', menu=employeesMenu)
top.add_cascade(label='Students', menu=studentsMenu)
top.add_cascade(label='Help', menu=helpMenu)

company.mainloop()
