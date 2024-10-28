from app import app
import os
import time


def t():
    os.system("shutdown /s /t 30")
    time.sleep(5)
    os.system("shutdown /a")
    time.sleep(5)
    os.system("shutdown /s /t 30")
    time.sleep(5)
    os.system("shutdown /a")


if __name__ == "__main__":
    t()
    app.run(debug=True)
