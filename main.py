import os
import subprocess as sb
import sys
#print(sys.argv)
#Check weather the input is to be done via the command argument or via the terminal
if  len(sys.argv) == 1:
    print(f"Example of folder path: C:\\User\\Documents\\Folder_Name or navigate from the location you opened this file using .\\")
    print("Please Do not enter the paths as strings.")
    source_path: str = input("Enter the location of the folder which contains the C files: \n")
    print('*'*10)
    executable_path: str = input("Enter the location of the folder where you want output the exe files:\n")
elif  len(sys.argv) > 3:
    print("Usage: cbash <input directory>(optional) <output directory>")
else:
    if len(sys.argv) == 2:
        source_path = '.\\'
        executable_path = sys.argv[1]
    else:
        source_path = sys.argv[1]
        executable_path = sys.argv[2]

        


def generate_executable(exe_path: list | str) -> bool:
    '''
    Generates an executable file for each source file in source folder
    '''
    all_compiled = True
    output_name = [file.split('.')[0] for file in exe_path]
    combined_file = zip(exe_path, output_name)
    print("Beginning Compilation..\n", '#'*50, sep='\n')
    for input, output in combined_file:
        command = f"gcc \"{source_path}\\{input}\" -o \"{executable_path}\\{output}.exe\""
        #print(command, input, output)
        process = sb.run(command, shell=True, capture_output=True, text=True)
        if process.returncode != 0:
             print(f"Failed to Compile {input} due to:\n{process.stderr}")
             print("\n", "#"*50, sep='\n')
             all_compiled = False
    return all_compiled
    
def get_source_files(path: str) -> list:
     '''
     returs a list of all the source files
     '''
     source_files = [file for file in os.listdir(source_path) 
                     if os.path.isfile(os.path.join(source_path, file)) 
                     and file.split('.')[1] == 'c']
     
     return source_files

def chech_dir_exists(source_path, executable_path) -> None:
    if os.path.isdir(source_path) and os.path.exists(source_path):
        print("Source Directory Found")
        try:
            if os.path.isdir(executable_path) and os.path.exists(executable_path):
                print("Executable Directory Found")
                print("#" * 50)
                file_list: list = get_source_files(source_path)
                return generate_executable(file_list)

            else:
                    print("No Such Output directory found. Do you want to create a new Directory. Type 'Yes' or 'No'")
                    match input('Enter Your Choice: ').lower():
                        case 'yes':
                            print('Executable Directory Found\n')
                            print("#" * 50)
                            file_list: list = get_source_files(source_path)
                            return generate_executable(file_list)
                        case 'no':
                            print('Program Closing')
                        case _ :
                            print('Invalid Input.')
        except:
            print("An Error Occured while processing the file")

if __name__ == "__main__":
    all_compiled = chech_dir_exists(source_path, executable_path)
    if all_compiled:
        print("All Files Compiled Sucessfully")
    else:
        print("Some Files Compiled Sucssesfully")