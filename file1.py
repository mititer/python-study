
filename = "employees.txt"
try:
    # read information by the end
    fp = open(filename, "r")
    print("readable="+str(fp.readable()))
    print("writable="+str(fp.writable()))
    print(fp.name)

    for employee in fp.readlines():
        print(employee)

    fp.close()
except FileNotFoundError as err:
    print("error: " + str(err))
except FileExistsError as err:
    print("error: " + str(err))
except:
    print("error unexpected")
