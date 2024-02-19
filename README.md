# Filmpicker Backend Server

The backend server for FilmPicker, a website for generating movie recommendations based on your favorite film!

This application requires a virtual environment with a number of auxiliary packages that are not included in the Python Standard Library. To simplify this, the latest docker image can be pulled directly from my dockerhub by running command:

- docker pull ericesposito/filmpicker-flask-api
- NOTE: Docker is required to be installed on your computer to follow these steps

Now, you can simply spin up a container based on this image, creating a local server that should be accessible on your device via port 8080 (e.g. localhost:8080)

- To easily spin up a container, run this command to make it accessible on port 8080 locally:
- docker run -p 8080:80 filmpicker-flask-api

- You can test backend functionality via Postman with the following options:
  - Send a POST request to localhost:8080
  - Attach a raw JSON shaped as follows:
    {"favorite_movie": "Blue Velvet (1986)"}
    - Note that you need to follow the proper convention with the correct spelling followed by its release year in parenthese

OR

- You can test backend functionality via running this command in your terminal, with the server up and running:
- curl -X POST http://localhost:8080/recommendations -H 'Content-Type: application/json' -d '{"favorite_movie":"Blue Velvet (1986)"}'

Using either of these methods, you should receive a response consisting of a JSON with an array of movie recommendations
