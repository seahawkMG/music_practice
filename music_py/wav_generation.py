#!usr/bin/env/ python3
# coding:utf-8

import wave
import numpy as np
from frequency import note_to_freq


class SoundWave:
	def __init__(self):
		self.wave_list = np.array([])
		self.wave_list_R = np.array([])
		self.wave_list_L = np.array([])
		self.wave_number = 0
		self.amp = 10000

	def set_amp(self, amp):
		self.amp = amp

	def set_stereo(self):
		self.wave_list_L = self.wave_list * 0.5
		self.wave_list_R = self.wave_list * 0.5

	# wave_list直接操作
	# ow:上書き、et:付けたし、"sy":合成
	def set_wave_list(self, wave_list, mode="ow"):
		if mode == "ow":
			self.wave_list = wave_list
			if self.wave_number != 1:
				self.wave_number = 1
		elif mode == "et":
			self.wave_list = np.append(self.wave_list, wave_list)
			if self.wave_number != 1:
				self.wave_number = 1
		elif mode == "sy":
			if len(wave_list) == len(self.wave_list):
				self.wave_list += wave_list
				self.wave_number += 1
			else:
				print("illegal synthesis")
		else:
			print("illegal wave list")

	# wavファイル出力
	def wavfile_generation_mono(self, filename):
		wave_for_wavfile = self.amp * self.wave_list / self.wave_number
		wave_form = wave_for_wavfile.astype(np.int16)
		outfile = wave.open(filename, "w")
		outfile.setnchannels(1)
		outfile.setsampwidth(2)
		outfile.setframerate(44100)
		outfile.writeframes(wave_form.tostring())
		outfile.close()

	def wavfile_generation_stereo(self, filename):
		wave_for_wavfile_L = self.amp * self.wave_list_L / self.wave_number
		wave_for_wavfile_R = self.amp * self.wave_list_R / self.wave_number
		wave_for_wavfile = np.array([wave_for_wavfile_L, wave_for_wavfile_R]).transpose()
		wave_form = wave_for_wavfile.astype(np.int16)
		outfile = wave.open(filename, "w")
		outfile.setnchannels(2)
		outfile.setsampwidth(2)
		outfile.setframerate(44100)
		outfile.writeframes(wave_form.tostring())
		outfile.close()

	# 波形生成
	def set_sin(self, note, sec=1.0, mode="ow"):
		freq = note_to_freq(note)
		time = np.linspace(0.0, sec, int(44100*sec))
		if freq >= 0:
			print(freq)
			sin_formula = np.sin(2.0 * np.pi * freq * time)
			self.set_wave_list(sin_formula, mode=mode)
			self.set_stereo()
		else:
			print("illegal note")

	def set_square(self, note, sec=1.0, mode="ow"):
		freq = note_to_freq(note)
		time = np.linspace(0.0, sec, int(44100*sec))
		if freq >= 0:
			print(freq)
			sqr_formula = np.sign(np.sin(2.0 * np.pi * freq * time))
			self.set_wave_list(sqr_formula, mode=mode)
			self.set_stereo()
		else:
			print("illegal note")

	def set_saw(self, note, sec=1.0, mode="ow"):
		freq = note_to_freq(note)
		time = np.linspace(0.0, sec, int(44100*sec))
		if freq >= 0:
			print(freq)
			saw_formula = 2 * (freq*time-np.floor((freq*time-0.5)))
			self.set_wave_list(saw_formula, mode=mode)
			self.set_stereo()
		else:
			print("illegal note")

	def set_triangle(self, note, sec=1.0, mode="ow"):
		freq = note_to_freq(note)
		time = np.linspace(0.0, sec, int(44100*sec))
		if freq >= 0:
			print(freq)
			triangle_formula = (2 * np.arccos(np.cos(2.0 * np.pi * freq * time)) / np.pi) - 1
			self.set_wave_list(triangle_formula, mode=mode)
			self.set_stereo()
		else:
			print("illegal note")

	def set_noise(self, sec=1.0, mode="ow"):
		time = np.linspace(0.0, sec, int(44100 * sec))
		noise = 2*np.random.rand(len(time))-1
		self.set_wave_list(noise, mode=mode)
		self.set_stereo()

	# 波形編集（エフェクター以外）
	def inverse(self):
		self.wave_list = self.wave_list*-1

	# エフェクター



