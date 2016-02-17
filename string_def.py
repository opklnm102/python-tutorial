# -*- coding: utf-8 -*-

def break_words(stuff):
	"""문자열을 단어로 쪼갠다."""
	words = stuff.split(' ')
	return words

def sord_words(words):
	"""단어 정렬"""
	return sorted(words)

def print_first_word(words):
	"""첫단어 출력"""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""마지막 단어 출력"""
	word = words.pop(-1)
	print word

def sort_setence(setence):
	"""한 문장에 있는 단어 정렬"""
	words = break_words(setence)
	return sord_words(words)

def print_first_and_last(setence):
	"""문장의 처음, 마지막 단어 출력"""
	words = break_words(setence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(setence):
	"""단어를 정렬하고 처음, 마지막 단어 출력"""
	words = sort_setence(setence)
	print_first_word(words)
	print_last_word(words)

