import os
print(os.getcwd())

confirmation = str(input('Are you sure you want to rename all files in the existing directory  [n / y] ?:'))

if confirmation =='y':
    for count, f in enumerate(os.listdir()):
     
        f_name, f_ext = os.path.splitext(f)

        if f_name != 'rename' and f_ext != '.py':
             f_name = "File720" + str(count)
             new_name = f'{f_name}{f_ext}'
             os.rename(f, new_name)
    print('Done !')
else :
    print('you are not sure !!')

        
       

 

        
    