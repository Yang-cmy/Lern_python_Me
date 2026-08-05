# Python File Open

The open() function takes two parameters; filename, and mode.

## There are four different methods (modes) for opening a file:

```python
"r" # Read - Default value. Opens a file for reading, error if the file does not exist

"a" # Append - Opens a file for appending, creates the file if it does not exist

"w" # Write - Opens a file for writing, creates the file if it does not exist

"x" # Create - Creates the specified file, returns an error if the file exists

```

## In addition you can specify if the file should be handled as binary or text mode:

```python
"t" # Text - Default value. Text mode

"b" # Binary - Binary mode (e.g. images)
```
# Syntax

To open a file for reading it is enough to specify the name of the file:

```python
f = open("demofile.txt")
```
The code above is the same as:

```python
f = open("demofile.txt", "rt")
```
Because "r" for read, and "t" for text are the default values, you do not need to specify them.

to close files when you are done with it : f.close

```python
f = open("demofile.txt")
print(f.readline())
f.close()
```
use with statement when opening a file, then you dont have to care about closing it with statement take care of that:

```python
with open("demofile.txt") as f:
  print(f.read())
```

you can also spetify how many character you want to return

```python
with open("demofile.txt") as f:
  print(f.read(5))
```

you can return one line by using ` readline() ` method:

```python
with open("demofile.txt") as f:
    print(f.readline())
```

By calling **readline()** two times, you can read the two first lines:

```python
with open("demofile.txt") as f:
    print(f.readline())
    print(f.readline())
```

By **looping** through the lines of the file, you can read the whole file, line by line:

```python
with open("demofile.txt") as f:
    for x in f
        print(x)
```

```python
with open("demofile.txt") as f:
    while true: #cant we use while and readline method anyway
        print(f.readline()) 
```

# Python File Write, Delete

we are entering write and append zone now huh?

## Write to an Existing File

To write to an existing file, you must add a parameter to the `open()` function:

`"a"` - Append - will append to the end of the file

`"w"` - Write - will overwrite any existing content

```python
with open("demofile.txt") as f:
    f.write("Now this file have more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
    print(f.read())
```
## Overwrite Existing Content

To overwrite the existing content to the file, use the w parameter:

```python
with open("demofile.txt", "w") as f:
    f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
    print(f.read())
```

## Create New file

To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exists

"a" - Append - will create a file if the specified file does not exists

"w" - Write - will create a file if the specified file does not exists

```python
f = open("myfile.txt", "x")
```
## Delete a File

To delete a file, you must import the OS module, and run its `os.remove(` function:

```python
import os
    os.remove("demofile.txt") #Remove the file "demofile.txt":
```

## Check if File exist:

To avoid getting an error, you might want to check if the file exists before you try to delete it:

```python
import os
if os.path.exists("demofile.txt"): # Check if file exists, then delete it:
    os.remove("demofile.txt")
else:
    print("The file does not exist")
```
## Delete Folder

To delete an entire folder, use the `os.rmdir()` method:

```python
import os
    os.rmdir("myfolder") # Remove the folder "myfolder":
```