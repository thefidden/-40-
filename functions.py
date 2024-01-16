import random
import tkinter as tk


def get_random_color() -> str:
	return '#' + ''.join(
		'{:02x}'.format(random.randint(0, 255)) for _ in range(3)
	)


def transpose_dict(dictionary: dict) -> dict:
	result = {}

	for key, value in dictionary.items():
		result[value] = key

	return result
