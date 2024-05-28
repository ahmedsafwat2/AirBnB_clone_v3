## AirBnB clone - The console

The goal of the project is to deploy on The server a simple copy of 
the AirBnB website.

## steps

### The console
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

### Excusion
Your shell should work like this in interactive mode:
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

But also in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
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

## cmd command:
- `shell` - excute shell commands
- `EOF/quit` - quit the console
- `create` - create new object
- `show` - show an object based on id
- `all` - show all objects for specific class or all objects
- `destroy` - deletes an object
- `update` - update an object based on class name and id
- `count` - count number of objects
