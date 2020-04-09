#open function opens file
#in open first argument is file's full path and second argument is modei.e w for write 
#if we open file with "with" then no need to close otherwise close it
# with open("abc.txt","w") as file_handle:
file_handle2=open("greet.txt","w")
file_handle2.write("Hi python")
file_handle2.write("Hi python")
file_handle2.write("Hi python")
file_handle2.close()  #close is used when there are 2 or more file like here

    # file_handle1=open("abcd.txt","w")
    # file_handle1.write("Hello World")
    # file_handle1.write("Hello World")
    # file_handle1.write("Hello World")
    # file_handle1.write("Hello World")
    # file_handle1.write("Hello World")
    # with open("abcd.txt","r") as f:
    #     a=f.read()
    #     print(a) 