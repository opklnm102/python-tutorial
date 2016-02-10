# -*- coding: utf-8 -*-
import random

def bubble_sort(l, count):
	for i in range(n):
		for j in range(1, n):
			if l[j] < l[j-1]:
				l[j], l[j-1] = l[j-1], l[j]
				count += 1
	return l, count

def random_list(n):
	l = []
	for i in range(n):
		l.append(random.randrange(1, 101, 1))
	return l

n = int(raw_input("input list size"))
unsorted_list = []
count = 0

unsorted_list = random_list(n)

print unsorted_list

sorted_list, count = bubble_sort(unsorted_list, count)

print sorted_list
print "total count: " + str(count)
