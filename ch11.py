import random

avto_driver = ['анвар','шер','азиз']
avto_driverA = len(avto_driver)
avto_driverAn = avto_driver[avto_driverA - 3]

avto_driverSh = len(avto_driver)
avto_driverSher = avto_driver[avto_driverSh - 2]

avto_driverAz = len(avto_driver)
avto_driverAziz = avto_driver[avto_driverAz - 1]

question_driver = input('какой номер автомобиля принадлежит водителю? ')

avto_number = ['01 286 GA','01 860 VA','01 298 PA']
avto_numberGa = len(avto_number)
avto_numberga = avto_number[avto_numberGa - 3]

avto_numberVa = len(avto_number)
avto_numberva = avto_number[avto_numberVa - 2]

avto_numberPa = len(avto_number)
avto_numberpa = avto_number[avto_numberPa - 1]

if avto_driverAn == question_driver:
    print(avto_numberga)
elif avto_driverSher == question_driver:
    print(avto_numberva)
elif avto_driverAziz == question_driver:
    print(avto_numberpa)
else:
    print('попробуй еще раз')