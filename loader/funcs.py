import json

from config import POST_PATH, UPLOAD_FOLDER
from extensions import WrongFileType


def save_picture(picture):
	"""Сохранение изображения под определенным расширением и в определенной папке"""
	allowed_type = ["png", "jpg", "jpeg", "gif", "bmp"]  # Допустимые разрешения файлов изображений
	picture_type = picture.filename.split(".")[-1]

	if picture_type not in allowed_type:
		raise WrongFileType(f"Неверный формат файла! Допустимы только следующие форматы файлов: {', '.join(allowed_type)}")

	picture_path = f"{UPLOAD_FOLDER}/{picture.filename}"  # путь к папке сохранения изображения
	picture.save(picture_path)  # сохранение самого изображения по указанному пути

	return picture_path


def add_post(post_list, post):
	"""Добавление нового поста в JSON-файл, где 'post_list' - список постов, а 'post' - новый пост для добавления"""
	post_list.append(post)

	with open(POST_PATH, "w", encoding="utf-8") as file:
		json.dump(post_list, file)
