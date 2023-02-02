# Cloud-Computing 
Home work - 1 Write a web application to find the weather of a given city. 

    1. Design the service using two microservices: 
      a. which takes city name as input and provide zipcode as output
      b. which takes zipcode as input and provide temprature as output

    2. Implement these two independent microservices and then test them using either browser client or curl client.
    3. Make these two microservices work together (Optional).

GITHUB Link: https://github.com/DKruti/Cloud-Computing

STEPS are As Follows:

ZIPCODE Service:
1. Created one project for service 1 : [city name ->zipcode] in python file name: main.py
2. Added requirements.txt which has flask command
3. run the code in the python
4. To run in to browerser type following line in any browser:
   http://127.0.0.1:5001/zipcode?city=San Jose
5. To run using curl type following line in terminal:
   curl http://127.0.0.1:5001/zipcode?city=San Jose
 
NOW steps for Docker and container
6. After completing above steps create Dockerfile with code
7. open terminal and type command: docker build --tag zipcode-docker
8. run the docker type command in terminal: docker run --publish 5001:5000 zipcode-docker
9. Docker is successfully created to check images: docker images
10. check for container running: docker ps
   
weather Service:
1. Created second project for service 2 : [zipcode -> temprature] in python file name: main.py
2. Added requirements.txt which has flask command
3. run the code in the python
4. To run in to browerser type following line in any browser:
   http://127.0.0.1:5001/weather?zipcode=95112
5. To run using curl type following line in terminal:
   curl http://127.0.0.1:5001/weather?zipcode=95112

NOW steps for Docker and container
6. After completing above steps create Dockerfile with code
7. open terminal and type command: docker build --tag weather-docker
8. run the docker type command in terminal: docker run --publish 5001:5000 weather-docker
9. Docker is successfully created to check images: docker images
10. check for container running: docker ps

NOTE: output images are uploaded both browerser and running container.
