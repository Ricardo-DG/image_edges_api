# start by pulling the python image
FROM python:3.10-slim

RUN mkdir /app

ENV PYTHONPATH=/app

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN /usr/local/bin/pip install -r /app/requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# copy every content from the local file to the image
COPY . /app

# copy every content from the local file to the image
# COPY ./methods.py /app/methods.py

EXPOSE 8888

# configure the container to run in an executed manner
ENTRYPOINT ["python", "app/main.py"]
