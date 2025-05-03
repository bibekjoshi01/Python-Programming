class ManageFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("enter")
        self.file = open(self.filename, "w")
        return self.file
    
    def __exit__(self, exec_type, exec_value, exec_traceback):
        if self.file:
            self.file.close()
        print('exit')
    

with ManageFile('notex.txt') as file:
    print("doing some stuufff")
    file.write("some stuffs....")