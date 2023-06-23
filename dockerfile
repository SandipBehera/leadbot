FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /rasa

# Copy the source code to the container
COPY . .

# Expose the Rasa port
EXPOSE 5005

# Set the default command to run Rasa
CMD ["rasa", "run", "-m", "models", "--enable-api", "--cors", "*", "--debug"]