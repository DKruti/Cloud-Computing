FROM python:3.8-alpine

#setting a working directory
WORKDIR /src

#copy the requirements.txt file into our working directory /src
COPY requirements.txt requirements.txt

#install all of the dependencies within the requirements.txt file in the image.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /src
COPY . .

ENV FLASK_APP=main.py

#CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
#CMD ["flask", "run", "--host=0.0.0.0"]
# add port to run on different port different services
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]

