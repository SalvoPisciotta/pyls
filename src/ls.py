import json
import argparse
from datetime import datetime
from src.exception import InvalidPathError
from src.utils import human_readable_datetime, human_readable_file_size
import sys

class PyLS:

    def __init__(self, json_structure: json, options: argparse.ArgumentParser):
        self.output = ""
        self.options = options
        self.set_root_structure(json_structure)

    def set_root_structure(self, json_structure):
        """
        Sets the root structure of the JSON data.
        This method sets the root structure of the JSON based on the input path parameter
        If an `InvalidPathError`is raised, stop_execution_with_message method is called.
        Args:
            json_structure (dict): The JSON structure to be set as the root.
        """

        if self.options.path == '.' or self.options.path == json_structure['name']:
            self.json_root_structure = json_structure
        else:
            try:
                self.json_root_structure = self.get_root_structure(json_structure)
            except InvalidPathError as error:
                self.stop_execution_with_message(error)

    def get_root_structure(self, json_structure):
        """
        Retrieves the root structure from a given JSON structure based on the specified path.
        Args:
            json_structure (dict): The JSON structure to navigate.
        Returns:
            dict: The root structure corresponding to the specified path.
        """
        
        items_to_root = [item for item in self.options.path.split('/') if item != '.']
        root_structure = json_structure
        for item_name in items_to_root:
            for sub_item in root_structure['contents']:
                if sub_item['name'] == item_name:
                    root_structure = sub_item
        if root_structure == json_structure:
            raise InvalidPathError(f"cannot access {self.options.path}: No such file or directory")

        return root_structure

    def generate_output(self):
        """
        Generate formatted output of directory contents based on the input options.
        """
        if "contents" in self.json_root_structure:
            root_contents = self.json_root_structure["contents"]
        else:
            root_contents = [self.json_root_structure]
        if self.options.l:
            self.generate_item_info_output(root_contents)
        else:
            self.generate_item_names_output(root_contents)

    def get_output(self):
        return self.output
    
    def filtered_sublist(self, directory_contents: json, item_type: str):
        """
        Filters the directory contents based on the specified item type.
        Args:
            directory_contents (json): A JSON object representing the contents of a directory.
            item_type (str): The type of items to filter ('dir' for directories, 'file' for files).
        Returns:
            list: A list of filtered items based on the specified item type.
        """
        if item_type == 'dir':
            sub_items = [item for item in directory_contents if 'contents' in item.keys()]
        elif item_type == 'file':
            sub_items = [item for item in directory_contents if 'contents' not in item.keys()]
        return sub_items

    def get_subitems_list(self, root_contents: json):
        """
        Extracts and returns list of sub-items from the given directory contents.
        Order of the list is based on the input options.
        Args:
            dir_contents (json): A JSON object containing the directory contents.
        Returns:
            list: A list of sub-items extracted from the directory contents.
        """
        
        if self.options.filter is not None:
            sub_items = self.filtered_sublist(root_contents, self.options.filter)
        else:
            sub_items = [item for item in root_contents]
        if self.options.t:
            sub_items = sorted(sub_items, key=lambda x: x["time_modified"])
        if self.options.r:
            sub_items.reverse()
        return sub_items

    def generate_item_names_output(self, root_contents: json):
        """
        Generates a string of content names from the given directory contents.
        Args:
            dir_contents (json): A JSON object containing the directory contents.
        """
        for item in self.get_subitems_list(root_contents):
            if item["name"][0] == "." and not self.options.A:
                continue
            else:
                self.output += item["name"] + " "

    def generate_item_info_output(self, root_contents: json):
        """
        Generates a formatted output string of content informations from the input dir contents.
        Args:
            dir_contents (json): A JSON object containing the directory contents.
        """
        for item in self.get_subitems_list(root_contents):
            if item["name"][0] == "." and not self.options.A:
                continue
            else:
                self.output += item["permissions"] + " "
                if self.options.h:
                    self.output += human_readable_file_size(item["size"])+ " "
                else:
                    self.output += str(item["size"]) + " "
                self.output += human_readable_datetime(item["time_modified"]) + " "
                self.output += item["name"] + " "
                self.output += "\n"

    def stop_execution_with_message(self, message):
        """
        Stops the execution of the program and prints the relative error message.
        Args:
            message (str): The message to be printed before stopping the execution.
        """
        
        print(f"{message}")
        sys.exit()