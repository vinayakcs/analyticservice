Analytic Service
===================


This service is intended to be used for tracking activities of the subscribing applications.

----------


API
-------------

localhost:5000/feedback/v1 **Endpoint**

> **Description:**

> - Media type : application/json
> - Request can be any valid json
> - The provided request body along with time stamp information and request headers of the service is recorded.
> - HTTP Method POST

#### Database

Database used is nosql(mongodb) to support dynamic schema,
The schema at version V1 looks like
```json
{
        "pld": json request to api,
        "tst":{"y": year,
        "m":month,
        "d":day,
        "s":seconds
        },
        "reqhdr":request_header,
        "ver":version of the api
    }
```
The time information is acquired of UTC.


####  Environment

1. host, defaults to localhost
2. port, defaults to 27017
3. database, defaults to feedback
4. collection, defaults to feedback
5. username, defaults to nil
6. password, defaults to  nil



#### Installation
docker-compose up   


#### Author
Vinayak srinivas [Linkedin](https://linkedin.com/in/vinayakcs)

#### License
Creative Commons Attribution (CC BY)

#### Demo
[![Demo](https://img.youtube.com/vi/J8FohgI7nG0/maxresdefault.jpg)](https://youtu.be/J8FohgI7nG0)


