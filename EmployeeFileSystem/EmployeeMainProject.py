from EmpAdd import addemployee
from EmployeeDelete import deleteemployee
from EmployeeUpdate import updateemployee
from EmployeeVie import viewallEmp,viewsingleEmp
from EmployeeSearch import searchemployee
from EmpMenu import menu
while(True):
    menu()
    try:
        ch = int(input("Enter your choice: "))
        match(ch):
            case 1:
                addemployee()
            case 2:
                deleteemployee()
            case 3:
                updateemployee()
            case 4:
                viewsingleEmp()
            case 5:
                viewallEmp()
            case 6:
                searchemployee()
            case 7:
                print("\tThanks for Using : ")
                break
            case _:
                print("\t Your Choose of selection is wrong --- try again")
    except ValueError:
        print("\t Don't Enter alphanumeric, string, symbols value for Numbers")
