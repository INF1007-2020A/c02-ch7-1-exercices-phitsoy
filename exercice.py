#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


def get_fibonacci_number(index):
	# if index == 0:
	# 	return 0
	# elif index == 1:
	# 	return 1
	# else:
	# 	return get_fibonacci_number(index-1) + get_fibonacci_number(index-2)
	# pass
	# if i == 0:
	# 	return a
	# if i == 1:
	# 	return b
	# else:
	# 	return c
	# return a if i == 0 else b id i == 1 else c
	return (
		0 if index == 0 else
		1 if index == 1 else
		get_fibonacci_number(index-1) + get_fibonacci_number(index-2)
	)
def get_fibonacci_sequence(length, seq=[0, 1]):
	# # BAtir avec les deux premiers elements pas definis recursivement
	# # Batie recursivement le reste:
	# if length == 1:
	# 	return seq[0:1]
	# elif length == 2:
	# 	return seq[0:2]
	# elif len(seq) < length:
	# 	return get_fibonacci_sequence(length, seq + [seq[-1] + seq[-2]])
	# else:
	# 	return seq
	#
	return (
		seq[0:length] if length <=2 else
		get_fibonacci_sequence(length, seq + [seq[-1] + seq[-2]]) if len(seq) < length else
		seq
	)

def get_sorted_dict_by_decimals(dict_arg):
	# def decimal_part(t):
	# 	return t[1] % 1.0
	# return dict(sorted(dict_arg.items(), key=decimal_part))
	return dict(sorted(dict_arg.items(), key=lambda t: t[1] % 1.0))

def fibonacci_numbers(length):
	# INIT_VALUES = [0, 1]
	# yield INIT_VALUES[0]
	# if length >= 2:
	# 	yield INIT_VALUES[1]
	#
	# if length > 2:
	# 	last_elems = deque(INIT_VALUES)
	# 	for i in range(2, length):
	# 		fibo_number = last_elems[-1] + last_elems[-2]
	# 		last_elems.append(fibo_number)
	# 		last_elems.popleft()
	# 		yield fibo_number
	INIT_VALUES = [0, 1]
	for i, elem in enumerate(INIT_VALUES):
		if i >= length:
			break
		yield elem
	last_elems = deque(INIT_VALUES)
	for i in range(len(INIT_VALUES), length):
		fibo_number = last_elems[-1] + last_elems[-2]
		last_elems.append(fibo_number)
		last_elems.popleft()
		yield fibo_number



def build_recursive_sequence_generator(TODO):
	pass

if __name__ == "__main__":
	print([get_fibonacci_number(0), get_fibonacci_number(1), get_fibonacci_number(2)])
	print([get_fibonacci_number(i) for i in range(10)])
	print()

	print(get_fibonacci_sequence(1))
	print(get_fibonacci_sequence(2))
	print(get_fibonacci_sequence(10))
	print()

	spam = {
		2: 2.1,
		3: 3.3,
		1: 1.4,
		4: 4.2
	}
	eggs = {
		"foo": 42.6942,
		"bar": 42.9000,
		"qux": 69.4269,
		"yeet": 420.1337
	}
	print(get_sorted_dict_by_decimals(spam))
	print(get_sorted_dict_by_decimals(eggs))
	print()

	for fibo_num in fibonacci_numbers(10):
		print(fibo_num, end=" ")
	print("\n")

	def fibo_def(last_elems):
		return last_elems[-1] + last_elems[-2]
	fibo = build_recursive_sequence_generator([0, 1], fibo_def)
	for fi in fibo(10):
		print(fi, end=" ")
	print("\n")

	lucas = build_recursive_sequence_generator(TODO)
	print(f"Lucas : {[elem for elem in lucas(10)]}")
	perrin = build_recursive_sequence_generator(TODO)
	print(f"Perrin : {[elem for elem in perrin(10)]}")
	hofstadter_q = build_recursive_sequence_generator(TODO)
	print(f"Hofstadter-Q : {[elem for elem in hofstadter_q(10)]}")
