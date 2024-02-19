# Filmpicker Backend Server

The backend server for FilmPicker, a website for generating movie recommendations based on your favorite film!

This application requires a virtual environment with a number of auxiliary packages that are not included in the Python Standard Library. To simplify this, the latest docker image can be pulled directly from my dockerhub by running command:

---

USING DOCKER TO SPIN UP A LOCAL CONTAINER

- docker pull ericesposito/filmpicker-flask-api
- NOTE: Docker is required to be installed on your computer to follow these steps

Now, you can simply spin up a container based on this image, creating a local server that should be accessible on your device via port 8080 (e.g. localhost:8080)

- To easily spin up a container, run this command to make it accessible on port 8080 locally:
- docker run -p 8080:80 filmpicker-flask-api

## If following these directions via Docker, you can skip down to the === section below

OR, if you prefer to not use Docker, and spin up a server locally, you can follow these steps:

---

RUNNING SERVER LOCALLY IN A TERMINAL INSTANCE

This application requires a virtual environment with a number of auxiliary packages that are not included in the Python Standard Library.

- The dependencies for this application are bundled up in the .yml file, environment.yml

To reproduce the environment on your machine, follow these steps:

1. Install Conda (either Anaconda or Miniconda) on your machine.
2. Clone this repository, which should include the environment.yml file.
3. Open a terminal, navigate to your project directory, and create a new Conda environment using the environment.yml file:

- conda env create -f environment.yml

4. Activate the environment by running this command:

- conda activate filmpicker_env

Now, the environment has been reproduced with all dependencies installed, and you should be able to run the jupyter notebook to generate the dataframe locally on your machine.

To do this, navigate to /data_analysis/notebooks/similarity_analysis.ipynb

- In this file, run the provided notebook, which will generate your dataframe (Note, this will generate a large file (~140MB) within this local directory)
  - More specifically, it will generate a .csv file on this path:
    - data_analysis/data/processed/movie_similarity.csv

And now, with the dataframe generated locally, you will be able to run the provided python application via a local terminal instance in this project's root directory, using this command:

- python app.py

===

Now, your server is up and running, and you can test it out by sending a request!

- You can test backend functionality via Postman with the following options:
  - Send a POST request to localhost:8080
  - Attach a raw JSON shaped as follows:
    {"favorite_movie": "Blue Velvet (1986)"}
    - Note that you need to follow the proper convention with the correct spelling followed by its release year in parentheses

OR

- You can test backend functionality via running this command in your terminal, with the server up and running:
- curl -X POST http://localhost:8080/recommendations -H 'Content-Type: application/json' -d '{"favorite_movie":"Blue Velvet (1986)"}'
  - Note that you need to follow the proper convention with the correct spelling followed by its release year in parentheses

Using either of these methods, you should receive a response consisting of a JSON with an array of movie recommendations

Feel free to experiment and build a beautiful Front End that can run based off of this backend server!
