from flask import Blueprint, render_template, request
import logging


main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")

logging.basicConfig(filename="logfile.log", level=logging.INFO)


@main_blueprint.route("/")
def main_page():
	logging.info("Загрузка главной страницы")
	return render_template("index.html")


@main_blueprint.route("/search")
def search_page():
	pass
