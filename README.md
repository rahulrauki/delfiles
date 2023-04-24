# delfiles
Simple CLI to delete files from a folder

## How to build:
`delfiles.py` is the main script that needs to be built.
1. ### Dependencies:
    - python >= 3.8
    - latest [pyinstaller](https://github.com/pyinstaller/pyinstaller)
2. After necessary installations, navigate to the project directory in the terminal with `delfiles.py`.
3. Type the command `pyinstaller --one-file delfiles.py`, you can set custom flags referring to the docs.
4. This command will create 2 directories, `build` & `dist`
5. `delfiles.exe` can be found in `dist`, you can take this app and distribute to wherever you like. Also this is our CLI

## Usage:

The application comes with `4` flags.
1. `-h` to display help
2. `--folder` or `-F`, to specify the path of your directory where deletable files are presented.
3. `--dictionary` or `-D`, to specify the path of the `.txt` file which contains the possible matches of the file names, that needs to be deleted or preserved.
4. `--exclude` or `-E`, doesn't take arguments, but if added `delfiles` will skip all the files that has a name matching with any of the strings provided in the `--dictionary`. If not added then the files whose name matches with the names provided in the `--dictionary` file WILL be deleted.

### Note:
 - `--folder` and `--dictionary` takes both absolute and relative paths.
 - The strings in `--dictionary` files "should" be seperated with a new line

## Example:
`delfiles --folder "./sample" --dictionary "dict.txt" --exclude`
This deletes all the files in `sample` directory with names that doesn't match with any strings given on `dict.txt`

### Additional:
A `createfiles.py` can be used to create randomly generated files for you to delete, default is 30. You can edit the code as per your testing needs.
### Disclaimer:
Feel free to download and mess around. Even create a PR. Have fun coding !!!
