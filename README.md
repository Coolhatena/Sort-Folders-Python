# Sort-Folders-Python
A useful script to sort the files of any folder, fully customizable and compatible with any extension

## How use it
The use of this tool is pretty simple, just run the file and introduce the path to the folder you want to sort on the input, everything else its automatic!

## How customize it
On the script file, find a variable named `file_categories`, this is a matrix that contains arrays with two values:
  * The name of the category, this is a string value and will be the name of the folder for the files that match the category
  * The extensions of the category, this is a list of all the extension names that belong to the category

Eventually, i'll add a config file (Most likely a JSON) to make the configuration process easier
