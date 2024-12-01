from typing import Dict, Union, List

# Type for a single file
File = Dict[str, Union[str, int]]

# Type for a directory, which can contain files or other directories
Directory = Dict[str, Union[str, int, List[Union[File, 'Directory']]]]

JsonFileSystemStructure = Union[Directory, File]