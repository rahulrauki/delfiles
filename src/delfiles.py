import os, re
import argparse

def create_parser(): # We are not using any positional arguments so no need to set any params
    '''
    Creates a parser object that has the user set values.
    '''
    parser = argparse.ArgumentParser(description="Simple CLI to delete files in a folder")
    parser.add_argument('-F', '--folder', dest="folder_path", help="Path of the folder where files will be deleted", required=True)
    parser.add_argument('-D', '--dictionary', dest="dict_path", help="Path of the dictionary files containing the file names or partial matching names", required=True)
    parser.add_argument("-E", '--exclude', action="store_true", default=False, help="Use this flag to delete everything except the ones mentioned in dictionary file")
    return parser.parse_args()

def main():
    try:
        parser_options = create_parser()
        folder_path = os.path.abspath(path=parser_options.folder_path)
        dict_path =  os.path.abspath(path=parser_options.dict_path)

        # Get the list of files in the folder
        file_list = os.listdir(path=folder_path)

        # Get the names of the files from the dictionary and add it to a list as a regex pattern
        pattern_list = []
        with open(dict_path, "r") as fhand:
            pattern_list = [re.compile(line.strip()) for line in fhand]

        initial_files = len(file_list)
        removed_files = matched_files = 0

        # Loop through the file list and check if the file name matches any pattern in the list
        if parser_options.exclude is True: # we skip the file names that match and delete others
            for filename in file_list:
                match_count = 0
                for pattern in pattern_list:
                    if re.match(pattern=pattern, string=filename): 
                        match_count += 1 # if the pattern match the file name we increment the match count
                matched_files += match_count
                if match_count == 0: # If any pattern had matched then we skip that file, if no matches then we delete the file
                    file_path = os.path.join(folder_path, filename)
                    if os.path.exists(path=file_path): 
                        os.remove(path=file_path)
                        removed_files += 1
        else: # Default is False, (when no --exclude flag is provided)
            for filename in file_list:
                for pattern in pattern_list:
                    if re.match(pattern=pattern, string=filename): # If any one pattern matches from the list we remove it and skip to next iteration
                        file_path = os.path.join(folder_path, filename)
                        if os.path.exists(path=file_path): 
                            os.remove(path=file_path)
                            removed_files += 1
                        matched_files += 1
                        break # So that we needn't check the rest of the patterns
        
        if parser_options.exclude is True:
            print(f'{matched_files}/{initial_files} files matched, and {removed_files}/{initial_files - matched_files} files in non-matched files removed successfully !!!')
        else: 
            print(f'{matched_files}/{initial_files} files matched, and {removed_files}/{matched_files} files in matched files removed successfully !!!')

    except Exception as error:
        print(f"An error occured : {error}")
                        

if __name__ == '__main__':
  main()