keep_going = 'y'

while keep_going == 'y' :
    sales = float(input('Enter the amount of seles: '))
    comm_rate = float(input('Enter the commisstion rate: '))

    commission = sales * comm_rate

    print('The commission is $', \
    format(commission, ',.2f'), sep='')

    keep_going = input('Do you want to calculate another' + \
                       'commission (Enter y for yes): ')