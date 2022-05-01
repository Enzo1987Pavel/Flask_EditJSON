import json
from extensions import DataJSONError


def load_json_file(path):
	"""Загрузка и чтение JSON-файла по указанному пути"""
	try:
		with open(path, "r", encoding="utf-8") as file:
			return json.load(file)
	except (FileNotFoundError, json.JSONDecodeError):
		raise DataJSONError


def search_post_by_substring(posts, substring):
	"""Поиск введенного слова ('substring') в тексте всех постов ('posts')"""
	posts_list = []  # пустой список для добавления постов, в которых найдены указанные слово/слова

	# перебор всех постов в списке на наличие искомого слова и приведение к нижнему регистру
	for post in posts:
		if substring.lower() in post["content"].lower():
			posts_list.append(post)  # добавление найденного поста к новому списку для вывода пользователю
	return posts_list
