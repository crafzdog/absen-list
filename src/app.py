from flask import Flask
from routes.page import page

app = Flask(__name__)
app.register_blueprint(page)

if __name__ == "__main__":
    app.run(debug=True)
