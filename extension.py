filename = input("Input the filename:")
name,extension = filename.split(".")
if extension == "py":
    extension = "python"
    print("The extension of the file is:"+ repr(extension))
