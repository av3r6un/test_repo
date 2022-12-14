from flask import Flask
from main import check_changes, commit_changes, pull_changes
app = Flask(__name__)


def check_updates():
    if check_changes():
        if pull_changes():
            commit_changes()


@app.route('/')
def index():
    return '<h1 style="color:red;">Hello, World!</h1>'


if __name__ == '__main__':
    check_updates()
    app.run(host="0.0.0.0", debug=True)
