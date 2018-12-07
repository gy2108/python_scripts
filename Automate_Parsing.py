import os

os.chdir('/Users/gopal/Documents/code')

for file in os.listdir():
    file_name, fil_ext = os.path.splitext(file)
    n1,n2,n3 = file_name.split(' ')
    n3 = n3[1:].zfill(2)
    new_name = '{}-{} {}'.format(n3,n1,n2)
    os.replace(file,new_name)