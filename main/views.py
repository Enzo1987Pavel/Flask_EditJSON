import logging

from flask import Blueprint, render_template, request
from main.funcs import load_json_file, search_post_by_substring
from config import POST_PATH
from extensions import DataJSONError

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")

logging.basicConfig(filename="logfile.log", level=logging.INFO)


@main_blueprint.route("/")
def main_page():
	logging.info("Загрузка главной страницы")  # запись в лог-файл события загрузки главной страницы
	return render_template("index.html")


@main_blueprint.route("/search")
def search_page():
	s = request.args.get("s", "")  # второй аргумент по умолчанию принимаем пустым, чтобы не было ошибки
	logging.info("Поиск поста по указанной подстроке")

	try:
		posts = load_json_file(POST_PATH)  # загружаем посты через JSON-файл
	except DataJSONError:
		return "Проблема с открытием JSON-файла"

	search_post = search_post_by_substring(posts, s)  # найденные посты "складываем" в переменную
	return render_template("post_list.html", posts=search_post, s=s)
