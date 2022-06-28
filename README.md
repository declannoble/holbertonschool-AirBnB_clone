# holbertonschool-AirBnB_clone
This console is the first part of the AirBnB project at the Holberton school.
This program will cover some fundamental concepts of higher level programming
that we have gone over in our curriculum. The goal of this project is to deploy
a simple clone of the AirBnB website. A command interpreter has been created
to manage objects for the website.

## Environment:
This project has been completed on Ubuntu 20.04 using python3 (3.8.5)

## Testing:

## Files:
| FILES           | DESCRIPTION                                          | ATTRIBUTES                                                                                                                           |
|-----------------|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| user.py         | user class                                           | email, password, first_name, last_name                                                                                               |
| amenity.py      | amenity class                                        | name                                                                                                                                 |
| place.py        | place class                                          | city_id, user_id, name, description, number_of_rooms, longitude, latitude, max_guests, number_bathrooms, price_by_night, amenity_ids |
| review.py       | review class                                         | place_id, user_id, text                                                                                                              |
| state.py        | state class                                          | name                                                                                                                                 |
| city.py         | city class                                           | state_id, name                                                                                                                       |
| file_storage.py | class to handle storage of date                      | __file_path, __objects                                                                                                               |
| base_model.py   | base class which  defines common attributes/ methods | id, created_at, updated_at                                                                                                           |