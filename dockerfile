# Base image
FROM python:3.8.2

# Set the working directory in the container
WORKDIR /rasa

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code to the container
COPY . .

# Expose the Rasa port
EXPOSE 5005


# Train the Rasa models
RUN rasa train

# Set the default command to run Rasa
CMD ["rasa", "run", "-m", "models", "--enable-api", "--cors", "*", "--debug"]