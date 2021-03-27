# importing libraries.
import os

# from dotenv import load_dotenv
from flask import Flask, request, render_template
# from flask_autoindex import AutoIndex
# from werkzeug.utils import secure_filename

# init dotenv
# load_dotenv()

# init main application 
horse = Flask(__name__)

# hacky cracky.
# KEY = os.environ.get("PRIVATE_KEY", "1234")


# indexing files feom main folder
# @horse.route('/dir', methods=['GET'])
# def index():
#    AutoIndex(horse, browse_root=os.path.curdir + 'Engineering')

# home
@horse.route('/', methods=['GET'])
@horse.route('/home', methods=['GET'])
def home():
    return render_template(
        "index.html")
