def main():
    sales_file = open('employees.txt','r')

    line = sales_file.readline()

    while line != '':
        amount = str(line)

        print(format(amount))

        line = sales_file.readline()

    sales_file.close

main()