
A simple python script to be used with Automation Anywhere to update set data points in a word document.

This script works similarly to the find and replace feature in word. It acts here as a supplement to the word actions package automation anywhere control room which currently does not have a working package for this function.

The script opens a csv file and reads the values saved here and saves them to two variables. 

The script then opens the word document  using the DocxTemplate module and using the the values saved in the context loops through the document and updates the data points that match the variables name.

Once all data points are updated the file is closed and saved to an output folder with the appropriate naming convention.
