""""x" - Create - will create a file, returns an error if the file exist
    
    "a" - Append - will create a file if the specified file does not exist
    
    "w" - Write - will create a file if the specified file does not exist"""
    
try:
    file = raw_input("What is the file path?    ")
    f = open(file)       #DIRECT FILE PATH NEEDS TO BE INCLUDED
    
    for x in f:
        print(x)
    
        if "Ye Digg" in x:
            print("Found it")

    r = readline(2)
    print(r)

    f.close()
except:
    print("File Did Not Open")
finally:
    print("---Try Block Is Done---")
