import os, time
def GetPath():
    path = input('Enter file directory: ')
    isdir = os.path.isdir(path)  
    if isdir == True:
        time.sleep(1)
        print('Directory found')
        FileName = input('Please enter the name of the file you wish to create: ')
        FilePath = os.path.join(path, FileName+".txt")
        f = open(FilePath, 'a')
        print('Please Enter: ')
        Name = input('Name: ')
        Address = input('Address: ')
        Phone = input ('Phone: ')
        print(
            '\n','Name: ',Name, '\n',
            'Address: ',Address, '\n',
            'Phone: ',Phone, '\n',
            '------------------------------------------------------------',
            file = f
            )
        f.close()
        time.sleep(1)
        print('\n','\033[4m','Opening File Contents','\033[0m','\n',)
        time.sleep(1)
        f = open(FilePath,'r')
        print(f.read())
    else:
        print('Incorrect Path')
        ReadWrite.GetPath(self)
GetPath()
