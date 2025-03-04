# C-Batch-Compiler
An automation script that takes all the C files in folder and generates an executable file for each C file in a given directory.
How to use:
	* Run the  main.py file from anywhere
	* Enter the source file dir(Folder):
	    Ex: C:\User\Diddy\Epstein_Island_Generator\Code\
	* Similarly enter the output file dir(Folder)
	    Ex: C:\User\Diddy\Epstein_Island_Generator\Bin\
	* Wait for the program to compile and link the files and create an executable for each, the output file will have the same name as the source file.
	* If a Source file is found to have errors, then a gcc error for that file will display and the file will not compile.
	* If all files compile sucsesfully then a sucsses message will display.
 	* The File is ready to be set up as batch file or can also accept command line arguments while invoking the file via python.
	* Note:
	    * Do Not Enter The File Path As A String with quotation mark!
	    * This program only works for the GNU GCC C compiler but can be modified to work with clang/other compilers.
	    * It is advised to have the executable\output folder ready and not use the program to generate dir.  
     * If you running on a system running linux kernel/ Mac OS then upadate the main.py file by omitting the .exe part in line 18.
