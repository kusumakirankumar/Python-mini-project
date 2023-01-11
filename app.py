from flask import Flask, render_template, send_from_directory
import os
import random

app = Flask(__name__)

@app.route("/")
def index():
    static_folder = os.path.join(os.getcwd(), "static")
    image_files = [f for f in os.listdir(static_folder) if f.endswith(".webp")]
    random_image = random.choice(image_files)
    return render_template("index.html", image=random_image)

@app.route("/static/<path:path>")
def serve_static(path):
    return send_from_directory("static", path)
    
if __name__ == "__main__":
    app.run(debug=True)
