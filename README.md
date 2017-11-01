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
* Edit the whitelist in Settings, to ensure requests come from known routes. 
* Split DB server off from API.

## Available Endpoints
Examples are contained in SA.postman_collection.json.
If accessing the Authorised Endpoints, include HTTP_AUTHORIZATION in request Header.
* Register - POST
```http://localhost:8000/register/```
    * Include ```password: value``` and ```email: value``` in Request
* Status -GET (Example returns list of Customers with Active status)
```http://localhost:8000/auth/status/ACTIVE```
```http://localhost:8000/api/status/ACTIVE```
* Customer -GET (Example returns list of Customers matching query)
```http://localhost:8000/auth/customer/C0201XEX```
```http://localhost:8000/api/customer/C0200098```
* ID -GET (Example returns list of Customers matching query)
```http://localhost:8000/auth/id/A02029VF```
```http://localhost:8000/api/id/A02017NU/```
* Balance -GET (Example returns list of Customers matching query)
```http://localhost:8000/auth/balance/0.00```
```http://localhost:8000/api/balance/0.04/```
* Balance with Option -GET (Example returns list of Customers matching query, valid operators are lte, gte)
```http://localhost:8000/auth/balance/0.00/op/gte```
```http://localhost:8000/api/balance/111/op/gte/```