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
COPY ./app /code/app

# Set Environment Variables
ARG BOT_TOKRN
ENV BOT_TOKEN=$BOT_TOKRN

# Create Volume
RUN mkdir /code/app/volume

# Set the command to run the uvicorn server.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]