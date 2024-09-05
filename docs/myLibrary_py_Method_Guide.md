# myLibrary.py Method Guide

## Table of Contents

## Description

## Methods / Functions

The functions are broken down into categories within the code. These are categories like Date time function or File functions.

## General Functions

### isBoolFromText(string)

```python
result = isBoolFromText("True")
```

The purpose of this function is to take in a string pulled from a file that may be a Boolean value saved into text. Like from a configuration “INI” file. It will test if the string is “True” or “False” and return a python Boolean.  

Note:

It’s use should be to test string values that are either True or False.

Parameters:

This function takes in one string value.  

strValue ⇒ STRING ⇒ “True”

strValue ⇒ STRING ⇒ “False”

Return Values:

The function will only return BOOL of True if the supplied string = “true” or “True” everything else will be returned as BOOL False.

Use:  

This function sole purpose is to convert a text string “True” or a “False” to a python boolean.

Code:

```python
def isBoolFromText(strValue):
    # Returns BOOL True if the string value = "True".
    if strValue.lower() == "true": return True
    else: return False
```

## Date / Time Functions

### getTimeStamp()

```python
stamp = getTimeStamp()
```

This function returns a string with the current date / time text.  

Parameters:

There are no parameters for this function.

Return Values:

Returns a formatted string with the date and time in the following format:

```PlainText
09/04/2024 @ 09:20::13 PM
```

Use:  

Use this function to get a date / time stamp to use as formatted. If you’re wanting one that can be used in a file name use the getTimeStampFile() which returns a formatted stamp for file names.

Code:

```python
def getTimeStamp():
    # Returns date in format: mm-dd-YYYY @ HH:MM::SS [AM/PM]
    dt = datetime.datetime.now()
    fullDate = f"{dt.strftime("%m")}/{dt.strftime("%d")}/{dt.strftime("%Y")}"
    time = f"{dt.strftime("%I")}:{dt.strftime("%M")}::{dt.strftime("%S")} "
    period = f"{dt.strftime("%p")}"
    return fullDate + " @ " + time + period
```

### getTimeStampFile()

```python
stampfile = getTimeStampFile()
```

This function returns string with a current date / time text formatted for use in file names

Parameters:

This function takes no parameters

Return Values:

This function returns a python string with the current date / time formatted for use in file names.

Use:  

Use this if you need a date / time stamp to use in a file name. For one to display on screen use the function getTimeStamp().

Code:

```python
def getTimeStampFile():
    # Returns date in format: mm-dd-YYYY_@_HH:MM—SS-[AM/PM]
    # This returns a stamp which can be used in a file name.
    dt = datetime.datetime.now()
    fullDate = f"{dt.strftime("%m")}-{dt.strftime("%d")}-{dt.strftime("%Y")}"
    time = f"{dt.strftime("%I")}-{dt.strftime("%M")}--{dt.strftime("%S")}-"
    period = f"{dt.strftime("%p")}"
    return fullDate + "_@_" + time + period
```

## File Functions

The functions in this section relate to files.  

### saveFile(string, string, int)

Note:

All files are opened for writing in text mode.

```python
result = saveFile("filename.txt", "My Text", 2)
```

This function will save a file to disk. This function has options to append, write, create.

Here is an example of calling the function from another file:

```python
import myLibrary as ml

def main():
    text = "Testing File Writes\n"
    testfile = "log_09-05-2024.log"
    result, msg = ml.saveFile(testfile, text, 2)
    if not result:
        exit(msg)

main()
```

Parameters:

There are three parameters this function takes. The first is a parameter for the file and path to save the file. The second is the text of what will be saved. The third and last parameter is the mode for saving.

“strPathFile”

Python Data Type: String

Description: This parameter contains the path and file name of the file to be saved.

Example String: “logs/log_08-05-2024.log”

Error: If there is nothing passed the error "Error: No path and file name defined” will be returned.

“strText”

Python Data Type: String

Description: This parameter will contain the text that needs to be saved.

Example: “Some text to save to a file”

Error:  If an empty string is passed the following error will be returned: "Error: There is no text to save!”

“intMode”

Python Data Type: Integer

Description: The value of the integer will define the mode of saving a file (i.e. Append).

Values:

1 ⇒ Append mode. Appends to a file or creates a new file if none exists.

2 ⇒ Write mode. Opens a file and writes over existing data, creates a new file if none exists.

3 ⇒ Create a file. Error if the file already exists.

ERROR NOTE: any other value not listed above will generate a return error with the text: "Error: Mode not set correctly!”

Return Values:

The function returns two values, the first is the BOOL result of the function and STRING value for error or success message.

Result ⇒ BOOL ⇒ False ⇒ Failed (see error message)

Result ⇒ BOOL ⇒ True ⇒ File written!

msg ⇒ STRING = Error Message

msg ⇒ STRING ⇒ Success message ⇒ “File Written!”

Errors that can be returned are as follows:

Error: No path and file name defined! ⇒ The path and file name parameter was empty.

Error: There is no text to save! ⇒ The text string is empty.

Error: Mode not set correctly! ⇒ Integer value outside expected results. See parameters values for “intMode”.

Error: File already exists! ⇒ If the mode is set to 3, and a file already exists.

Use:  

This function is used to write a text file to disk. See the following code for an example code to call the “saveFile()” function.

```python
import myLibrary as ml

def main():
    text = "Testing File Writes\n"
    testfile = "log_09-05-2024.log"
    result, msg = ml.saveFile(testfile, text, 2)
    if not result:
        exit(msg)

main()
```

Code:

```python
def saveFile(strPathFile, strText, intMode):
    # Check for errors
    if strPathFile == "": return False, "Error: No path and file name defined"
    if strText == "": return False, "Error: There is no text to save!"
    if intMode not in range(1, 4): return False, "Error: Mode not set correctly!"

    if intMode in range(1, 4):
        if intMode == 1: file = open(strPathFile, "at")
        elif intMode == 2: file = open(strPathFile, "wt")
        elif intMode == 3: 
            try:
                file = open(strPathFile, "xt")
            except FileExistsError:
                return False, "Error: File already exists!"

    file.write(strText)
    file.close()
    return True, "File Written!"
```

### Template

Parameters:

Return Values:

Use:  

Code:  
