# A simple REST API to GET and POST data to a MongoDB instance

This is a simple example of a RESTful API utilising Django, 
Django Rest Framework, and MongoEngine. There are 2 sets of 5 GET end points
to query the MongoDB instance, both with and without a token created during 
 Registration. 
 
##To Build Locally
* Clone the Repo and create a virtual env
* Run ```pip install -r requirements.txt``` to install dependencies
* Ensure MongoDB is installed (and if necessary change host and port in settings)
* Run project using ```python manage.py runserver```

##To Run in Production
* Remove all SECRETS from the code base, and regenerate. 
Store these as Env variable in the shell and call back at runtime.
* Better enforcement of Auth Key, including expiry. This project is not secure as it stands. 

 