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

# Set Environment Variables
ENV BOT_TOKEN=""
ENV BASE_URL="http://127.0.0.1:5000"

# Create Volume
RUN mkdir /code/volume
RUN echo "This is a test file" > /code/volume/test.txt
VOLUME /code/volume

# Set the command to run the uvicorn server.
CMD ["python", "bot.py"]