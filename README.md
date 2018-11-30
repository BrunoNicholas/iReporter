![Build Status](https://travis-ci.org/BrunoNicholas/iReporter.svg?branch=Develope)

# iReporter | The API Endpoints
iReporter is a simple web application that enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public.

In this case, users can also report on things that needs government intervention.

## How the API works
_This project works on the URLs below for the operations of the HTTP resources_

| REQUEST | ROUTE | FUNCTIONALITY |
| ------- | ----- | ------------- |
| *GET* | ```/api/v1/users``` | _Returns all saved records of users_|
| *POST* | ```/api/v1/users``` | _Creates a new user record_|
| *GET* | ```/api/v1/users/<user_id>;``` | _Returns a specific user_|
| *PUT* | ```/api/v1/users/<user_id>;``` | _Updates a specific user record_|
| *GET* | ```/api/v1/users/<user_id>/edit;``` | _Returns a specific user for editing_|
| *DELETE* | ```/api/v1/users/<user_id>;``` | _Deletes a specific user record_|

| REQUEST | ROUTE | FUNCTIONALITY |
| ------- | ----- | ------------- |
| *GET* | ```/api/v1/red-flags``` | _Returns all saved records of red-flags|
| *POST* | ```/api/v1/red-flags``` | _Creates a new red-flag record_|
| *GET* | ```/api/v1/red-flags/<flag_id>;``` | _Returns a specific red-flag_|
| *PUT* | ```/api/v1/red-flags/<flag_id>;``` | _Updates a specific red-flag record_|
| *GET* | ```/api/v1/red-flags/<flag_id>/edit;``` | _Returns a specific red-flag for editing_|
| *DELETE* | ```/api/v1/red-flags/<flag_id>;``` | _Deletes a specific red-flag record_|

| REQUEST | ROUTE | FUNCTIONALITY |
| ------- | ----- | ------------- |
| *GET* | ```/api/v1/interventions``` | _Returns all saved records of interventions_|
| *POST* | ```/api/v1/interventions``` | _Creates a new intervention record_|
| *GET* | ```/api/v1/interventions/<int_id>;``` | _Returns a specific intervention_|
| *PUT* | ```/api/v1/interventions/<int_id>;``` | _Updates a specific intervention record_|
| *GET* | ```/api/v1/interventions/<int_id>/edit;``` | _Returns a specific intervention for editing_|
| *DELETE* | ```/api/v1/interventions/<int_id>;``` | _Deletes a specific intervention record_|



