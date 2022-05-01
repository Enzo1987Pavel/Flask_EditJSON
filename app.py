import logging

from flask import Flask, send_from_directory, render_template

from main.views import main_blueprint
from loader.views import loader_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


# Для обработки неверного типа загружаемого файла
@app.errorhandler(400)
def bad_request(error):
    logging.info("Неверный формат загружаемого файла!")
    return render_template("Error_pict_load.html", error_pict=error)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run()
