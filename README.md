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

## Installation

To install the `pyls` application, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/pyls.git
    ```

2. Navigate to the project directory:
    ```sh
    cd pyls
    ```

3. Ensure the JSON file system structured file `structure.json` file is present in the root directory. A default one is given, but is possible to change it keeping the same name. 

5. Install the required dependencies:
    ```sh
    pip install -e .
    ```

## Usage

Once installed follow the previous steps you can run the commands described in the previous section just as:
    ```
    pyls [options] [path]
    ```

### Examples

- List all files and directories in the current directory:
```sh
pyls
```
- List all files, including hidden files:
```
pyls -A
```

- List files in long format:
```
pyls -l
```

- List files in human-readable format:
```
pyls -l -h
```

- List all files and directories in reverse order:
```
pyls -A -r
```

- List all files and directories ordered by last modification timestamp:
```
pyls -A -l -t
```

- List only files
```
pyls --filter file
```

- Display help message:
```
pyls --help
```

## Running Tests

To run the tests for this project, navigate to the `pyls` directory and execute `pytest`:

```sh
pytest
```

Ensure you have `pytest` installed. You can install it using pip with:

```sh
pip install pytest
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
