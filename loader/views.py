import logging

from flask import Blueprint, request, render_template, abort
from config import POST_PATH
from extensions import WrongFileType
from main import funcs
from loader.funcs import save_picture, add_post


loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")

logging.basicConfig(filename="logfile.log", level=logging.INFO)


@loader_blueprint.route("/post", methods=["GET"])
def page_of_create_new_post():
	logging.info("Демонстрация формы с постами и их картинками.")
	return render_template("post_form.html")  # показать форму с постами


@loader_blueprint.route("/post", methods=["POST"])
def page_of_creating_new_post_by_user():
	content = request.form.get("content")
	picture = request.files.get("picture")

	try:
		new_post = {"pic": save_picture(picture), "content": content}
	except WrongFileType:
		logging.info("Неверный формат загружаемого файла!")
		abort(400)

	if not content and not picture:
		logging.info("Ошибка загрузки на сервер нового поста. Текст и изображение поста отсутствуют!")
		return render_template("No_data.html", post_error="Текст и изображение поста отсутствуют! Необходимо добавить данные!")

	elif not content:
		logging.info("Ошибка загрузки на сервер нового поста. Текст поста отсутствует!")
		return render_template("No_data.html", post_error="Текст поста отсутствует!")

	elif not picture:
		logging.info("Ошибка загрузки на сервер нового поста. Изображение поста отсутствует!")
		return render_template("No_data.html", post_error="Изображение поста отсутствует! Необходимо добавить изображение!")

	posts = funcs.load_json_file(POST_PATH)

	add_post(posts, new_post)

	logging.info("Пост успешно добавлен!")
	return render_template("post_uploaded.html", new_post=new_post)
