<div align="center">
<h3>AirBnB clone - The console</h3>
<h3>A command interpreter to manipulate data without a visual interface</h3>
<h5>Python OOP</h4>
  <img src="image/hbnb.png" width="1000" height="350"/>
</div>

### **Welcome to the AirBnB clone project!**

***First step: The command interpreter to manage AirBnB objects.***
This is the first step towards building full web application: the AirBnB clone. This first step is very important because it will use what is built during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help to:

- put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from `BaseModel`
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all classes and storage engine
## **The console**
- creating th data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give an abstraction between “My object” and “How they are stored and persisted”. This means: from the console code (the command interpreter itself) and from the front-end and RestAPI to build later, there won’t be a need to pay attention (take care) of how the objects are stored.

This abstraction will also allow to change the type of storage easily without updating all of its codebase.

<img src="image/flowdia.png" width="1000" height="350"/>

#### **How to start it**
The console will be a tool to validate this storage engine

```
`$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
`$
But also in non-interactive mode: (like the Shell project in C)

`$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
`$
`$ cat test_help
help
`$
`$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
`$
```

#### **How to use it**

**`create`**: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: ``$ create BaseModel
- If the class name is missing, print `** class name missing **` (ex: `$ create`)
- If the class name doesn’t exist, print `** class doesn't exist **` (ex: `$ create MyModel`)
```
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
```
**`show`**: Prints the string representation of an instance based on the class name and id. Ex: `$ show BaseModel 1234-1234-1234
- If the class name is missing, print `** class name missing **` (ex: `$ show`)
- If the class name doesn’t exist, print `** class doesn't exist **` (ex: `$ show MyModel`)
- If the id is missing, print `** instance id missing **` (ex: `$ show BaseModel`)
- If the instance of the class name doesn’t exist for the id, print `** no instance found **` (ex: `$ show BaseModel 121212`)
```
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
```

**`destroy`**: Deletes an instance based on the class name and id (save the change into the `JSON file`). Ex: `$ destroy BaseModel 1234-1234-1234.`
- If the class name is missing, print `** class name missing **` (ex: `$ destroy`)
- If the class name doesn’t exist, print `** class doesn't exist **` (ex:`$ destroy MyModel`)
- If the id is missing, print `** instance id missing **` (ex: `$ destroy BaseModel`)
- If the instance of the class name doesn’t exist for the id, print `** no instance found **` (ex: `$ destroy BaseModel 121212`)
```
(hbnb) destroy
** class name missing **
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
```
**`all`**: Prints all string representation of all instances based or not on the class name. Ex: `$ all BaseModel or $ all`.
The printed result must be a list of strings (like the example below)
- If the class name doesn’t exist, print ** class doesn't exist ** (ex: `$ all MyModel`)
```
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
```
**`update`**: Updates an instance based on the class name and id by adding or updating attribute (save the change into the `JSON file`). Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`.
**Usage: `update <class name> <id> <attribute name> "<attribute value>"`**
Only one attribute can be updated at the time
You can assume the attribute name is valid (exists for this model)
The attribute value must be casted to the attribute type
- If the class name is missing, print `** class name missing **` (ex: `$ update`)
- If the class name doesn’t exist, print `** class doesn't exist **` (ex: `$ update MyModel`)
- If the id is missing, print `** instance id missing **` (ex: `$ update BaseModel`)
- If the instance of the class name doesn’t exist for the id, print `** no instance found **` (ex: `$ update BaseModel 121212`)
- If the attribute name is missing, print `** attribute name missing **` (ex: `$ update BaseModel existing-id`)
- If the value for the attribute name doesn’t exist, print `** value missing **` (ex: `$ update BaseModel existing-id first_name`)
```
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
```
**`default command:`**
- to retrieve all instances of a class by using: **`<class name>.all()`**
```
root@Learnsoft:AirBnB$ ./console.py
(hbnb) User.all()
[[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@mail.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}, [User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}]
(hbnb) 
```
- to retrieve the number of instances of a class: **`<class name>.count()`**.
```
root@Learnsoft:AirBnB$ ./console.py
(hbnb) User.count()
2
(hbnb)
```
- to retrieve an instance based on its ID: **`<class name>.show(<id>)`**.
```
root@Learnsoft:AirBnB$ ./console.py
(hbnb) User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@mail.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}
(hbnb) User.show("Bar")
** no instance found **
(hbnb)
```
- to destroy an instance based on his ID: **`<class name>.destroy(<id>)`**.
```
root@Learnsoft:AirBnB$ ./console.py
(hbnb) User.count()
2
(hbnb) User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb) User.count()
1
(hbnb) User.destroy("Bar")
** no instance found **
(hbnb)
``` 
- to update an instance based on his ID: **`<class name>.update(<id>, <attribute name>, <attribute value>)`**.
```
root@Learnsoft:AirBnB$ ./console.py
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
(hbnb)
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "age", 89)
(hbnb)
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 89, 'first_name': 'John', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 15, 32, 299055), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
(hbnb) 
```

#### Authors: [**`Adam Sanusi Babatunde`**](https://github.com/iAdamo) & [**`Linda Nwachukwu`**](https://github.com/Lyndha)
