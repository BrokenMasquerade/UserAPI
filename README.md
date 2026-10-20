# UserAPI
A REST API that can communicate with the DummyJSON User API.

This program depends on Requests and Flask, which must be installed 
before the application is run:

> python -m pip install requests
>
> python -m pip install Flask


Running the program
-------------------

Open a command prompt and run either run_server_windows.bat (for Windows)
or run_server_linux_macos.bat (for Linux or MacOS) file to launch the 
server. Under normal circumstances the server will run on the URL
http://127.0.0.1:5000

When the server is running, you can send HTTP requests to it with 
a program like Invoke-WebRequest or cURL. The API only supports GET 
requests, with the ability to filter for first and/or last names. 

*Get all users*

> Invoke-WebRequest:
>
>> Invoke-WebRequest -Uri http://127.0.0.1:5000/users -Method GET
>
> cURL:
>
>> curl "http://127.0.0.1:5000/users"

*Get all users with the first name Emily*

> Invoke-WebRequest:
>
>> Invoke-WebRequest -Uri http://127.0.0.1:5000/users -Body @{'firstName' = 'Emily'} -Method GET
>
> cURL:
>
>> curl "http://127.0.0.1:5000/users?firstName=Emily"


*Get all users with the first name Emily and last name Brown*

> Invoke-WebRequest:
>
>> Invoke-WebRequest -Uri http://127.0.0.1:5000/users -Body @{'firstName' = 'Emily'; 'lastName' = 'Brown'} -Method GET
>
> cURL:
>
>> curl "http://127.0.0.1:5000/users?firstName=Emily&lastName=Brown"

Assumptions
-----------

This application was developed with the assumption that it might be
modified in the future. As such, the upstream API's URL and which user 
fields should be included in the response are listed as global variables
in the code to allow for easy modification.

It is also assumed that the upstreams API could possibly have some users 
with missing fields (such as a user with no phone number). In this case, 
the user will lack this field in the response as well.

