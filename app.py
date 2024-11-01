from src import create_app


def main():
    app = create_app()

    app.run(debug=True)
