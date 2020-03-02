'''
Demo data
------------------
Jim - Salesman
Dwight - Salesman
Pam - Receptionist
Michael - Manager
Oscar - Accounter

know the difference between:   a, w
'''
filename = "employees.txt"
try:
    # read information by the end
    fp = open(filename, "a")
    print("readable="+str(fp.readable()))
    print("writable="+str(fp.writable()))
    print(fp.name)

    fp.write("\nToby - Human Resource")
    fp.write("\nKelly - Customer Service")

    fp.seek(0)
    for employee in fp.readlines():
        print(employee)

    fp.close()
except FileNotFoundError as err:
    print("error: " + str(err))
except FileExistsError as err:
    print("error: " + str(err))
except:
    print("error unexpected")
