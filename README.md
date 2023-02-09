# Cloud-Computing 
Home work - 1 Write a web application to find the weather of a given city. 

    1. Design the service using two microservices: 
      a. which takes city name as input and provide zipcode as output
      b. which takes zipcode as input and provide temprature as output

    2. Implement these two independent microservices and then test them using either browser client or curl client.
    3. Make these two microservices work together (Optional).

GITHUB Link: https://github.com/DKruti/Cloud-Computing.git

STEPS are As Follows:

## ZIPCODE Service:
1. Created one project for service 1 : [city name ->zipcode] in python file name: main.py 
NOTE: here to call another serice form one serice you have to write http request call in try catch. Refer code
2. Added requirements.txt which has pre requisties of flask and requests install command
3. run the code in the python
4. To run in to browerser type following line in any browser:
   http://localhost:5000/zipcode?city=San%20Jose
5. To run using curl type following line in terminal:
   curl http://localhost:5000/zipcode?city=San Jose
Output: weather = 72F 
 
## NOW steps for Docker and container

 6. After completing above steps create Dockerfile with code
 7. open terminal and type command: docker build --tag zipcode-service .
 8. run the docker type command in terminal: docker run --name zipcode-serice-container --publish 5000:5000 zipcode-service
   
## weather Service:
1. Created second project for service 2 : [zipcode -> temprature] in python file name: main.py
NOTE: this is called service so no need to write http request call. the code same as you call individual service but you have to write different not used port number while calling run().
2. Added requirements.txt which has flask command and in Docker file also add the same port number as written in .py code in CMD[].
3. run the code in the python
### It is automatically called from the zipcode service but to check it is individually working then write a following steps
4. To run in to browerser type following line in any browser:
   http://http://0.0.0.0:5001//weather?zipcode=95112
5. To run using curl type following line in terminal:
   curl http://0.0.0.0:5001/weather?zipcode=95112

## NOW steps for Docker and container
 
 6. After completing above steps create Dockerfile with code
 7. open terminal and type command: docker build --tag weather-service .
 8. run the docker type command in terminal: docker run --name weather-service-container -p 5001:5001 weather-service

###

NOTE: output is in "updated final Screenshot of homework1 output and steps -19732-kruti dhyani.pdf" file the images are older one which shows individual serivce are working.
