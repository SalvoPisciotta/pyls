import json
import argparse
from datetime import datetime


class PyLS:

    def __init__(self, json_dir_structure: json, options: argparse.ArgumentParser):
        self.output = ''
        self.options = options
        self.json_dir_structure = json_dir_structure

    def generate_output(self):
        """
        Generate formatted output of directory contents based on the input options.
        """
        top_level_dir_contents = self.json_dir_structure["contents"]
        if self.options.l:
            self.generate_item_info_output(top_level_dir_contents)
        else:
            self.generate_item_names_output(top_level_dir_contents)

    def get_output(self):
        return self.output

    def get_subitems_list(self, dir_contents: json):
        """
        Extracts and returns list of sub-items from the given directory contents.
        Order of the list is based on the input options.
        Args:
            dir_contents (json): A JSON object containing the directory contents.
        Returns:
            list: A list of sub-items extracted from the directory contents.
        """
        sub_items = [item for item in dir_contents]
        if self.options.t:
            sub_items = sorted(sub_items, key=lambda x: x["time_modified"])
        if self.options.r:
            sub_items.reverse()
        return sub_items

    def generate_item_names_output(self, dir_contents: json):
        """
        Generates a string of content names from the given directory contents.
        Args:
            dir_contents (json): A JSON object containing the directory contents.
        """
        for item in self.get_subitems_list(dir_contents):
            if item["name"][0] == '.' and not self.options.A:
                continue
            else:
                self.output += item["name"] + ' '

    def generate_item_info_output(self, directory_contents: json):
        """
        Generates a formatted output string of content informations from the input dir contents.
        Args:
            dir_contents (json): A JSON object containing the directory contents.
        """
        for item in self.get_subitems_list(directory_contents):
            if item["name"][0] == "." and not self.options.A:
                continue
            else:
                self.output += item["permissions"] + " "
                self.output += str(item["size"]) + " "
                date_time = datetime.fromtimestamp(item["time_modified"])
                self.output += date_time.strftime("%b %d %H:%M") + " "
                self.output += item["name"] + " "
                self.output += "\n"
