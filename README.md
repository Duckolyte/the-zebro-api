# the-zebro-api
REST API to the zebro project.


### Seed the database. 

```
set FLASK_APP=run.py
flask seed run
```

##### TODO 

1.
create a unit-test branch and implement unit tests.

2. 
Create logging branch and implement logging.
Log in the Exception route.
How to log from container out to local host file system?

3. Create requirements.txt file for ease of install.
List of the pypi packages.

###Partwise done
4. Create a docker-containerization branch and implement docker file.
https://docker-py.readthedocs.io/en/stable/client.html
https://www.youtube.com/watch?v=IZmlkoOO8Mg&t=397s @see 10:30

Done: <br>Setup Dockerfile and compose file.
Run docker with 

````
cd docker
python compose.py
````

 Todo: <br>
 At moment throws an error. Reason is the trial to connect to the local mysql database.  
 1. 
 Configure the container so it can access a local db. 
 2. 
 Then install the mysql db on the remote host fatality z and connect to this db.
