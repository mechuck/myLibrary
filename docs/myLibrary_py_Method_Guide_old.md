# myLibrary.py Method Guide

### Table of Contents

# Description

# Methods / Functions

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

```
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

### Template

Parameters:

Return Values:

Use: 

Code: