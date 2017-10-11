# File-Splitter-Python
Python implementation, creates .txt files from delimited file.

This is a command line utility for taking a single input file and splitting it apart into multiple children files based on a single column. It takes in arguments in order to determine input file, delimiter, column to split on and any lines to skip in the file.

Arguments:

	--help : Lists all arguments and definitions.
  
	--input: File Path for file to split (e.g. C:\ProjectData\FileSplitter\SamplePipeFile.txt)
 	
	--delim: Input file delimiter (e.g. \t or | or ,)
  
	--column: Column index to split on, indexed at 0.
  
	--skip: Number of lines to skip (e.g. set to 1 if headers exist)
	
  
 Example execution:
  
	C:\Users\MyUser\AppData\Local\Programs\Python\Python36-32\python.exe C:/Users/MyUser/PythonProjects/FileSplitter/FileSplitter.py --input "C:\ProjectData\FileSplitter\SamplePipeFile.txt" --delim "|" --column 0 --skip 1
