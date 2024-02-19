from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

# Import dataframe from processed data using the first column as an index
similarity_dataframe = pd.read_csv(
    "data_analysis/data/processed/movie_similarity.csv", index_col=0
)

# Initiate an instance of Flask and store it in app for route decorator creation
app = Flask(__name__)
# Prevent cors errors due to requests from other servers
CORS(app)


# Declare a /recommendations endpoint, allowing for POST requests
@app.route("/recommendations", methods=["POST"])
def make_recommendations():
    # If a proper POST request is sent, grab the request body and store the favorite movie
    if request.method == "POST":
        # Grabbing the request body
        data = request.json
        # Declare variable movie and store the request movie choice
        movie = data["favorite_movie"]
        # Try block for catching errors
        try:
            # Check if the movie is found in our dataframe
            similarity_score = similarity_dataframe[movie]
            # If so, sort the relevant list of similarities in descending order to find top recommendations
            similar_movies = similarity_score.sort_values(ascending=False)[1:50]
            # Convert this into a List and store it in variable api_recommendations
            api_recommendations = similar_movies.index.to_list()
        except:
            # For errors where the movie is not found, return that as a string
            api_recommendations = ["Movie not found"]
            # Send an appropriate response back to the requester
        return jsonify({"movie_recs": api_recommendations})


# Ensure app is the main file being executed by Python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
