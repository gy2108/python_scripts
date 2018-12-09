# import os

# os.chdir('/Users/gopal/Documents/code')

# for file in os.listdir():
#     file_name, fil_ext = os.path.splitext(file)
#     n1,n2,n3 = file_name.split(' ')
#     n3 = n3[1:].zfill(2)
#     new_name = '{}-{} {}'.format(n3,n1,n2)
#     os.replace(file,new_name)
import tkinter as tk 

class App: 
        def __init__(self,master): 
                self.tboard=tk.Text(master,height=40,width=50) 
                self.tboard.grid(row=1,column=1,sticky="nsew") 
                self.tboard.grid_rowconfigure(1,weight=1) 
                self.tboard.grid_columnconfigure(1,weight=1) 
root=tk.Tk() 
app=App(root) 

root.mainloop() 