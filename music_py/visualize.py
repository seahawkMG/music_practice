#!usr/bin/env/ python3
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from wav_generation import SoundWave

class Visualize:
    def __init__(self, soundwave):
        # soundwave: SoundWave
        self.wave_list = soundwave.wave_list
        self.wave_list_L = soundwave.wave_list_L
        self.wave_list_R = soundwave.wave_list_R

    def plot_mono_partial(self, dp_start=0, dp_end=100):
        x = np.array(range(dp_start, dp_end))
        y = self.wave_list[dp_start:dp_end]
        plt.plot(x,y)
        plt.ylabel("Amplitude")
        plt.ylim([-1, 1])
        plt.show()

    def plt_stereo_partial(self, dp_start=0, dp_end=100):
        x = np.array(range(dp_start, dp_end))
        yL = self.wave_list_L[dp_start:dp_end]
        yR = self.wave_list_R[dp_start:dp_end]
        plt.subplot(2, 1, 1)
        plt.plot(x, yL)
        plt.ylabel("Amplitude")
        plt.ylim([-1, 1])
        plt.subplot(2, 1, 2)
        plt.plot(x, yR)
        plt.ylabel("Amplitude")
        plt.ylim([-1, 1])
        plt.show()

    def plot_mono_whole(self):
        x = np.array(range(len(self.wave_list)))
        y = self.wave_list[0:100]
        plt.plot(x,y)
        plt.ylabel("Amplitude")
        plt.ylim([-1, 1])
        plt.show()

    def plt_stereo_whole(self):
        x = np.array(range(len(self.wave_list)))
        yL = self.wave_list_L
        yR = self.wave_list_R
        plt.subplot(2, 1, 1)
        plt.plot(x, yL)
        plt.ylabel("Amplitude")
        plt.ylim([-1, 1])
        plt.subplot(2, 1, 2)
        plt.plot(x, yR)
        plt.ylabel("Amplitude")
        plt.ylim([-1, 1])
        plt.show()

    def

