# 0x00. AirBnB clone - The console

# AirBnb_clone

# AirBnB Clone - The Console 
 
This is the command interpreter for the AirBnB Clone project. 
 
## Description 
 
The AirBnB Clone project is a Python-based project that aims to replicate the functionality of the AirBnB website. This command interpreter is the first step towards building the full web application. It allows you to manage AirBnB objects by performing various operations such as creating new objects, retrieving objects, updating attributes, and more. 
 
## How to Start 
 
To start the command interpreter, run the following command:
  
$ ./console.py
## How to Use 
 
The command interpreter provides a prompt  (hbnb)  where you can enter commands to manage AirBnB objects. The supported commands include: 
 
-  `help` : Display a list of available commands and their descriptions. 
-  `quit` : Exit the command interpreter. 
-  `create` : Create a new object of a specified class. 
-  `show` : Display the string representation of an object. 
-  `destroy` : Delete an object. 
-  `all` : Display the string representation of all objects or of objects of a specified class. 
-  `update` : Update the attributes of an object. 
 
Examples:
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) create BaseModel
b6a6e15c-c67d-4312-9a75-9d084935e579
(hbnb) show BaseModel b6a6e15c-c67d-4312-9a75-9d084935e579
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
(hbnb) update BaseModel b6a6e15c-c67d-4312-9a75-9d084935e579 name "Updated Model"
(hbnb) show BaseModel b6a6e15c-c67d-4312-9a75-9d084935e579
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'Updated Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
(hbnb) all
["[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'Updated Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}"]
(hbnb) quit
## Authors 
 
This project was developed by `Archford Chipadza` and `Ben Vilakazi`. 
 
## Requirements 
 
- Python Scripts: 
  - Python version: 3.8.5 
  - pycodestyle version: 2.8.* 
  - All files should end with a new line 
  - The first line of all files should be  `#!/usr/bin/python3`  
  - All files must be executable 
  - All modules, classes, and functions should have proper documentation 
- Python Unit Tests: 
  - All test files should be inside the  `tests`  folder 
  - All test files and folders should start with  `test_`  
  - Test file organization should match the project's file structure 
  - All tests should be executed using the command  `python3 -m unittest discover tests`

# Files and Directories
- `models` directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
- `tests` directory will contain all unit tests.
- `console.py` file is the entry point of our command interpreter.
- `models/base_model.py` file is the base class of all our models. It contains common elements:
- attributes: `id`, `created_at` and `updated_at`
- methods: `save()` and `to_json()`
- models/engine directory will contain all storage classes (using the same prototype). For the moment you will have only one: `file_storage.py`.  
 
Please refer to the project's GitHub repository for more information and detailed requirements.
