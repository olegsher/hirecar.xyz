from flask import Flask, render_template


if __name__ == '__main__':
        app.run()


app = Flask(__name__,
            static_folder = "../../frontend-dev/static",
            template_folder = "../../frontend-dev/dist")
@app.route('/')
def index():
    return render_template("index.html")
