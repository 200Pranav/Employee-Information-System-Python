import pickle

def viewsingleEmp():
    #Get records in list
    records = []
    with open("D:\\Dubey Pranav\\Dubey Pranav\\Employee.info","rb") as fp:
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    #display the records
    res = False
    empID = int(input("Enter Employee ID to view the Detail: "))
    for index in range(len(records)):
        if(records[index][0] == empID):
            recindex = index
            res= True
            break
        # View the Record
    print("-" * 50)
    if (res):
        print("\tEmployee Number:{}".format(records[recindex][0]))
        print("\tEmployee Name:{}".format(records[recindex][1]))
        print("\tEmployee Salary:{}".format(records[recindex][2]))
        print("\tEmployee Company Name:{}".format(records[recindex][3]))
        print("-"*50)
    else:
        print("\tEmployee Number {} Does Not Exist ".format(empID))
        print("-" * 50)




def viewallEmp():
    with open("D:\\Dubey Pranav\\Dubey Pranav\\Employee.info","rb") as fp:
        print("----------------------------------------------")
        while (True):
            try:
                record = pickle.load(fp)
                for val in record:
                    print("\t{}".format(val), end="\t")
                print()
            except EOFError:
                print("------------------------------------------")
                break
