# ⛱️ AirBnB Clone Project - The Console
![hbnb](https://user-images.githubusercontent.com/91517809/176107896-998e3280-f565-4e09-a801-c609984bfed6.png)

This console is the first part of the AirBnB project at the Holberton school.
This program will cover some fundamental concepts of higher level programming
that we have gone over in our curriculum. The goal of this project is to deploy
a simple clone of the AirBnB website. A command interpreter has been created
to manage objects for the website.

## 🌳 Environment:
This project has been completed on Ubuntu 20.04 using python3 (3.8.5)

## ⚙️ Installation

> Step 1 - Clone the repo locally using this command 
```
gh repo clone chiaracaprasi/holbertonschool-AirBnB_clone
```
> Step 2 - Navigate to the folder 
```
cd holbertonschool-AirBnB_clone
```
> Step 3 - Run the console shell in interactive mode:
```
./console.py
```
> Step 4 - Type a command e.g.
```
(hbnb) help 
```
> Step 5 - Exit the shell 
```
(hbnb) quit
```

## 🚀 Operation Modes

#### Interactive mode
In the interactive mode, the console will display (hbnb) prompting the user to type in and execute a command. After the command is run, the prompt (hbnb) will appear again in a new line waiting for a new command to be entered. As long as the user doesn't quit the shell (by typing quit and pressing enter), this will go indefinitely. 
Example: 

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

#### Non-interactive mode

In the non-interactive mode, the console is run with a command pipped into into its execution - this way the command is run as soon as the shell starts. In this mode no prompt (hbnb) appears, and no further input is expected from the user.
Example:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```



## 🛂 Testing:
All files, classes and functions can be tested with unit tests.

**Interactive mode:** 
```
python3 -m unittest discover tests
```

**Non-interactive mode** 
```
echo "python3 -m unittest discover tests" | bash
```



## 📁 Files:
| FILES                                             | DESCRIPTION                                          | ATTRIBUTES                                                                                                                           |
|---------------------------------------------------|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [user.py](/models/user.py)                        | user class                                           | email, password, first_name, last_name                                                                                               |
| [amenity.py](/models/amenity.py)                  | amenity class                                        | name                                                                                                                                 |
| [place.py](/models/place.py)                      | place class                                          | city_id, user_id, name, description, number_of_rooms, longitude, latitude, max_guests, number_bathrooms, price_by_night, amenity_ids |
| [review.py](/models/review.py)                    | review class                                         | place_id, user_id, text                                                                                                              |
| [state.py](/models/state.py)                      | state class                                          | name                                                                                                                                 |
| [city.py](/models/city.py)                        | city class                                           | state_id, name                                                                                                                       |
| [file_storage.py](/models/engine/file_storage.py) | class to handle storage of date                      | __file_path, __objects                                                                                                               |
| [base_model.py](/models/base_model.py)            | base class which  defines common attributes/ methods | id, created_at, updated_at                                                                                                           |

### [console.py](console.py)
console description
(what have we coded that the console can do?)

### [base_model.py](/models/base_model.py)
base model description

### [file_storage.py](/models/engine/file_storage.py)


## 🛖 Examples

## 🐛 Bugs

## ✍🏽 Authors

- Chiara Caprasi
- Declan Noble
- Matthew Brinkmann 
