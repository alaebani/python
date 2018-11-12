student = int(input('Enter the number of students in the class:'))
lab = int(input('Enter the number of PCs in the lab:'))

full=student//lab
remain=student%lab

if remain > 0:
    full+=1

if full==1 :
    print('you need 1 lab for all student')
else:
    print('you need',full, 'labs for all the student.')


