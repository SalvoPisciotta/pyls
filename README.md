# Pyls: the python `ls` command from json

This repository contains a Python application that simulates the `ls` command found in Linux taking as input a JSON file named `structure.json`.
The application supports various argument parameters to provide similar functionality to the linux `ls` command.

The json file should be structured as `test/test_json` :
```json
{
    "name": "root",
    "size": 4096,
    "time_modified": 1699957865,
    "permissions": "-rw-r--r--",
    "contents": [
        {
            "name": "file1",
            "size": 1024,
            "time_modified": 1699957865,
            "permissions": "-rw-r--r--"
        },
        {
            "name": "dir1",
            "size": 4096,
            "time_modified": 1699957865,
            "permissions": "drwxr-xr-x",
            "contents": [
                {
                    "name": "file2",
                    "size": 2048,
                    "time_modified": 1699941437,
                    "permissions": "-rw-r--r--"
                }
            ]
        }
    ]
}
```

with directories that can be distinguished from files due to the presence of `content` field in the json object.
## Features

- List directory contents
- Support for various `ls` command options
    - path: The path of the folder to navigate with ls (default is current directory '.').
    - -A: Include all items, including those starting with a dot.
    - -l: Display additional information about items.
    - -r: Display items in reverse order.
    - -t: Sort items by the time they were last modified.
    - -h: Display human-readable sizes for items.
    - --filter: Filter options to display only files with 'file' or directories with 'dir'.
    - --help: Display the help message.

## Usage

Run the application with the desired options:
```sh
python -m pyls [options] [path]
```

### Examples

- List all files and directories in the current directory:
```sh
python -m pyls
```
- List all files, including hidden files:
```
python -m pyls -a
```

- List files in long format:
```
python -m pyls -l
```

- List files in human-readable format:
```
python -m pyls -l -h
```

- List all files and directories in reverse order:
```
python -m pyls -A -r
```

- List all files and directories ordered by last modification timestamp:
```
python -m pyls -A -l -t
```

- List only files
```
python -m pyls --filter file
```

- Display help message:
```
python -m pyls --help
```

## Running Tests

To run the tests for this project, navigate to the `pyls/test` directory and execute `pytest`:

```sh
cd pyls/test
pytest
```

Ensure you have `pytest` installed. You can install it using pip if necessary:

```sh
pip install pytest
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
