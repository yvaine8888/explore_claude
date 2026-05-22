from flask import Flask, render_template, request, redirect, url_for


def create_app() -> Flask:
    app = Flask(__name__)
    return app


if __name__ == "__main__":
    create_app().run(debug=True, port=5000)
