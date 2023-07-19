# Base image
FROM python:3.8.2

# Set the working directory in the container
WORKDIR /rasa

# Upgrade pip
RUN pip3 install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir twilio
RUN pip3 install --no-cache-dir websockets==10.
RUN pip3 install --no-cache-dir protobuf==3.20
# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the source code to the container
COPY . .

# Expose the Rasa port
EXPOSE 5005 5055

# Train the Rasa models
RUN rasa train

# Set the default command to run Rasa
CMD ["rasa", "run", "-m", "models", "--enable-api", "--cors", "*", "--debug"]