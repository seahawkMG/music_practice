#!usr/bin/env/ python3
# coding:utf-8

import math

# 各Aの設定

A_freq_list = []
for i in list(range(9)):
	A0_freq = 27.5
	Ax_freq = (2 ** i) * A0_freq
	A_freq_list.append(Ax_freq)

All_freq_list = []
for freq in A_freq_list:
	for j in list(range(12)):
		freq_temporal = freq * math.pow(2, j/12)
		All_freq_list.append(round(freq_temporal, 5))


"""
音階表示eg: Af3
"""


def note_to_number(note):
	onkai_lib = {
		"A": 0,
		"B": 2,
		"C": 3,
		"D": 5,
		"E": 7,
		"F": 8,
		"G": 10,
	}
	choon_lib = {
		"f": -1,
		"n": 0,
		"s": 1,
	}
	octave = int(note[2])
	note_number = 12*octave + onkai_lib[note[0]] + choon_lib[note[1]]
	if note_number >= 0 and note_number < len(All_freq_list):
		return note_number
	else:
		print("Illegal Note")
		return -1

def num_to_freq(num):
	return All_freq_list[num]

def note_to_freq(note):
	num = note_to_number(note)
	return All_freq_list[num]






