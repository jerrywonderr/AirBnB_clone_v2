#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects
    
    def generate_key(self, objekt=None):
        """
        Generates a string to be used as key for object_id
        Arguments:
            objekt: the objekt
        Returns:
            A string.
        """

        return "{}.{}".format(objekt.__class__.__name__, objekt.id)

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = self.generate_key(objekt=obj)
        FileStorage.__objects[key] = str(obj)

    def save(self):
        """Serializes __objects to the JSON file at self.__file_path"""
        with open(self.__file_path, 'w', encoding='utf-8') as outFile:
            print(FileStorage.__objects)
            json.dump(FileStorage.__objects, outFile)
        # Just to add a newline to the end of the file
        with open(self.__file_path, 'a', encoding='utf-8') as outFile:
            outFile.write('\n')

    def reload(self):
        """
        Deserializes the JSON file at self.__file_path
        into FileStorage.__objects if the file exists.
        Raises no error, if the file doesn't exist
        """

        if os.path.exists(self.__file_path):
            with open(self.__file_path) as outFile:
                FileStorage.__objects = json.load(outFile)
