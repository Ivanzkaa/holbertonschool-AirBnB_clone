<head>
<h1><center>AirBnB clone project</center></h1>
<img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20221010%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221010T203457Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=62d74b632ff01c143e85aecfaa518382a42810c1f239ef89ff69fb6f8ace7743">
</head>
<body>
<h3>In this project we will deploy on our own server a copy of the AirBnb website. We will work on creating a console in which we will create a data model. In this data model we will create, update, destroy, etc, objects via the console and we will store and persist objects to a file. When finished we will have a functioning copy with the popular and most useful features of the of the AirBnb website.</h3>
<ul><h2>We will also work on these tasks throughout the project:</h2>
<h3>
<li>Webstatic(HTML/CSS)</li>
<li>MySQL storage</li>
<li>Web framewok</li>
<li>RESTful API</li>
<li>Web dynamic</li>
</h3>
</ul>
<h1><center>Files</center></h1>
<ul><h3>
<li>base_model.py</li>
<li>__init__.py</li>
<li>file_storage.py</li>
<li>console.py</li>
<li>user.py</li>
<li>state.py</li>
<li>city.py</li>
<li>amenity.py</li>
<li>place</li>
<li>review.py</li>
</ul></h3>
<br>
<h1><center>The console</center></h1>
<ul>
<h3>
<li>Creating a data model</li>
<li>Manage the objects (users, place, states, cities, etc)
<li>Storing the objects into a file</li>
</h3>
</ul>
<img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20221011%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221011T144449Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=01ad1eac505ed3af57a69f9240caee3b66ca3258a74e41abda7e341d05c58ea2">
<br>
<h1><center>Examples</center></h1>
<h2>Interactive mode:</h2>
<h3>
$ ./console.py
<br>
(hbnb) help
<br>
Documented commands (type help <topic>):
<br>
========================================
<br>
EOF  help  quit
(hbnb)
(hbnb)
(hbnb) quit
$
</h3>
<br>
<h2>Non-interactive mode:</h2>
<h3>
$ echo "help" | ./console.py
<br>
(hbnb)
<br>
Documented commands (type help <topic>):
<br>
========================================
<br>
EOF  help  quit
<br>
(hbnb)
<br>
$
<br>
$ cat test_help
<br>
help
<br>
$
<br>
$ cat test_help | ./console.py
<br>
(hbnb)
<br>
Documented commands (type help <topic>):
<br>
========================================
<br>
EOF  help  quit
<br>
(hbnb)
<br>
$
</h3>
<br>
<h2>Installation</h2>
<h3>To use the console you need to have
<ul>
<li>Linux Ubuntu 20.04 LTS or higher</li>
<li>Python 3.8.5 or higher</li>
</h3>
</ul>
<h2>Authors</h2>
<ul>
<h3>
<li>Ivanzka Rodriguez (@Ivanzkaa)</li>
<li>Jaime Diaz</li>
</h3>
</ul>
</body>
