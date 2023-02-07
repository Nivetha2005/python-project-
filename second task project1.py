f=input("Input the filename:")
ext=f.split(".",1)
if ext[1]=="txt":
    x="text"
elif ext[1]=="py":
    x="python"
elif ext[1]=="jpg":
    x="jpeg"
else:
    x="unknown"
print("The extension of the file is:'{}'".format(x))
    
