## AirBnb Clone Project

<p align="center"><img src="https://i.ibb.co/9Z31skq/65f4a1dd9c51265f49d0-1.png" alt="AirBnB Clone Project" /></p>

<p>The AirBnB Project is the second group project in ALX sprint two. In this propect we are to implement a console prompt where we manipulate data without a visual interface, something like a Shell prompt. <br> The console does the following:</p>

1. Create your data model
2. Manage (create, update, destroy, count, retrive) object via console / command interpreter
3. Store and persis object of a file (JSON file)

### Repository Contents by Project Task

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/vickkykruz/AirBnB_clone/blob/main/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](https://github.com/vickkykruz/AirBnB_clone/tree/main/tests) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/vickkykruz/AirBnB_clone/blob/main/models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/vickkykruz/AirBnB_clone/blob/main/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/vickkykruz/AirBnB_clone/blob/main/models/engine/file_storage.py) [/models/_ _init_ _.py](https://github.com/vickkykruz/AirBnB_clone/blob/main/models/__init__.py) [/models/base_model.py](https://github.com/vickkykruz/AirBnB_clone/blob/main/models/base_model.py) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [console.py](https://github.com/vickkykruz/AirBnB_clone/blob/main/console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | [console.py](https://github.com/vickkykruz/AirBnB_clone/blob/main/console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [console.py](https://github.com/vickkykruz/AirBnB_clone/blob/main/console.py) [/models/engine/file_storage.py](https://github.com/vickkykruz/AirBnB_clone/blob/main/models/engine/file_storage.py) [/models/user.py](https://github.com/vickkykruz/AirBnB_clone/blob/main/models/user.py) | Dynamically implements a user class |
| 9. More Classes | [/models/user.py](https://github.com/vickkykruz/AirBnB_clone/blob/main/models/user.py) [/models/place.py](https://github.com/vickkykruz/AirBnB_clone/blob/main/models/place.py) [/models/city.py](https://github.com/vickkykruz/AirBnB_clone/blob/main/models/city.py) [/models/amenity.py](https://github.com/vickkykruz/AirBnB_clone/blob/main/models/amenity.py) [/models/state.py](https://github.com/vickkykruz/AirBnB_clone/blob/main/models/state.py) [/models/review.py](https://github.com/vickkykruz/AirBnB_clone/blob/main/models/review.py) | Dynamically implements more classes |
| 10. Console 1.0 | [console.py](https://github.com/vickkykruz/AirBnB_clone/blob/main/console.py) [/models/engine/file_storage.py](https://github.com/vickkykruz/AirBnB_clone/blob/main/models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all  classes update file storage |


### General Use
1. First clone this repository.

3. Once the repository is cloned locate the "console.py" file and run it as follows:
```
/AirBnB_clone$ ./console.py
```
4. When this command is run the following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)


##### Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

    * all - Shows all objects the program has access to, or all objects of a given class

	* count - Return number of object instances by class

    * show - Shows an object based on class and UUID

	* destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID
<br>
<br>

### Storage System For This Project
<p>In pharse we to collect the data the user input, manipute it an store it in a powerful storage system. This storage engine will give us an abstraction between the MyObject and "How they stored and persisted". Now using this abstraction allows us to change the type of storsge without affecting our program for this project.</p>

<p align="center"><img src="https://i.ibb.co/3B8dsfm/815046647d23428a14ca.png" alt="Algothim for storage" /></p>

### Data Diagram For This Project
<p>In this project we are to implement it using OOP (Object Oriented Progrmming) in Python, where we create classes, instanace and methods. so therfore we will have One BaseModel that handle common called methods and and instance, this will act the primary class model, so it will be inheritaned to other classe. Here is the data diagram for this project.</p>

<p align="center"><img src="https://i.ibb.co/8YTmJ2d/99e1a8f2be8c09d5ce5ac321e8cf39f0917f8db5-1.jpg" alt="Data Diagram" /></p>

<p>So in the above explanation we are going to implement and define the following for each propery in the class and store them, retrieve them when used by the user and delete it by the user.</p>

### Examples

#### Primary Command Syntax

###### Example 0: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
###### Example 1: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
###### Example 2: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```
###### Example 3: Update an object
Usage: update <class_name> <_id>
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
<h3>Alternative Syntax</h3>

###### Example 0: Show all User objects
Usage: <class_name>.all()
```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 1: Destroy a User
Usage: <class_name>.destroy(<_id>)
```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 2: Update User (by attribute)
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 3: Update User (by dictionary)
Usage: <class_name>.update(<_id>, <dictionary>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
<br>

### Collaboration For This Project.
<p>This project was done and implemented by the following Software Enginners</p>

1. Edward Victor Chukwuemeka
2. Johnson Adeola (adeola.johnson.37@gmail.com)

<p align="center">ALX Africa</p>
