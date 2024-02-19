# Use the official Miniconda image as a parent image
FROM continuumio/miniconda3

# Copy the current directory contents into the container at /app
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Create the environment using the environment.yml file
RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "filmpicker_env", "/bin/bash", "-c"]

# Expose the port the app runs on
EXPOSE 80

# Define the command to run the app using conda run to ensure the environment is activated
CMD ["conda", "run", "-n", "filmpicker_env", "python", "app.py"]
