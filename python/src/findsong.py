
from eyed3 import id3

from flask import Flask ,request,jsonify
from lyrics_extractor import SongLyrics
from flask_cors import CORS, cross_origin


app = Flask(__name__)  
app.config['CORS_HEADERS'] = 'application/json'
cors = CORS(app)

@app.route("/search",methods=['POST'])
@cross_origin()
def get_metadata():

    song_file=request.files['file']
    try:
        tag = id3.Tag()
        tag.parse(song_file)
        song_data={
        "artist":tag.artist if tag.artist else "not found",
        "movie name": tag.album if tag.album else "not found",
        "title":tag.title if tag.album else "not found"
        }

    except:
        return jsonify("message","Song not found")

    return jsonify(song_data)



if __name__ =="__main__":  
    app.run(debug = True)
    
    
