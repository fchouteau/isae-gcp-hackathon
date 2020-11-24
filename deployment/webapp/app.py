import os
import random
from pathlib import Path

from flask import Flask
from jinja2 import Environment, FileSystemLoader

random.seed(2020)

app = Flask(__name__, static_url_path="", static_folder=str(Path(__file__).parent))

# list of images
images = Path(__file__).parent / "imgs"
images = sorted(list(images.glob("*.gif")))

with open(Path(__file__).parent / "AUTHOR.txt", "r") as f:
    author = f.read().strip("\n")

template_loader = FileSystemLoader(Path(__file__).parent)
template_env = Environment(loader=template_loader)
template = template_env.get_template("template.html.jinja2")

@app.route("/")
def index():
    url = images[random.randint(0, len(images) - 1)]
    url = url.relative_to(Path(__file__).parent)
    return template.render(url=str(url), author=author)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
