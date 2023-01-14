# Start from the official Python base image.
FROM python:3.9

# Set the current working directory to /code
# This is where we'll put the requirements.txt file and the app directory.
WORKDIR /code

# Copy the file with the requirements to the /code directory.
COPY ./requirements.txt /code/requirements.txt

# Install the package dependencies in the requirements file.
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the ./app directory inside the /code directory.
COPY . /code

ARG BOT_TOKEN
ARG BASE_URL
# Set Environment Variables
ENV BOT_TOKEN=$BOT_TOKEN
ENV BASE_URL=$BASE_URL

# Create Volume
RUN mkdir /code/volume

# Set the command to run the uvicorn server.
CMD ["python", "bot.py"]