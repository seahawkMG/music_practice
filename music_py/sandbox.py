#!usr/bin/env/ python3
# coding:utf-8
"""
import wav_generation

note = "An4"

An3_list = wav_generation.sin_generator_from_note(note)

wav_generation.wavfile_generation(An3_list, "An3_test_02.wav")
"""
"""
from wav_generation import *

test = SoundWave()
test.set_triangle("Cn3", sec=1.0, mode="et")
test.set_triangle("Dn3", sec=1.0, mode="et")
test.set_triangle("En3", sec=1.0, mode="et")
test.set_triangle("Fn3", sec=1.0, mode="et")
test.set_triangle("Gn3", sec=1.0, mode="et")
test.set_triangle("An4", sec=1.0, mode="et")
test.set_triangle("Bn4", sec=1.0, mode="et")
test.set_triangle("Cn4", sec=1.0, mode="et")
print(len(test.wave_list))
test.wavfile_generation_mono("test_Oct_180507_tr_02.wav")
"""
"""
test = SoundWave()
test.type_check()
print(len(test.wave_list))
test.set_sin("Cn3", sec=2.0, mode="et")
test.type_check()
print(len(test.wave_list))
"""


from wav_generation import *
from visualize import Visualize

test = SoundWave()
test.set_noise(sec=3.0, mode="et")
test.set_amp(10000)

vis = Visualize(test)
vis.plt_stereo_partial()