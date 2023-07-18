# Base image
FROM python:3.10.6

# Set the working directory in the container
WORKDIR /rasa

# Upgrade pip
RUN pip3 install --no-cache-dir --upgrade pip
# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip3 install --upgrade rasa

# Copy the source code to the container
COPY . .

# Expose the Rasa port
EXPOSE 5005

# Train the Rasa models
RUN rasa train

# Set the default command to run Rasa
CMD ["rasa", "run", "-m", "models", "--enable-api", "--cors", "*", "--debug"]