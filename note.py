import sys,os
from array import array
old_target = sys.stdout
devnull_target = open(os.devnull, 'w')
sys.stdout = devnull_target
import pygame
from pygame.mixer import Sound, get_init, pre_init
sys.stdout = old_target

class Note(Sound):
    def __init__(self, frequency, volume=.05):
        pygame.init()
        self.frequency = frequency
        pygame.mixer.Sound.__init__(self, self.build_samples())
        self.set_volume(volume)

    def build_samples(self):
        period = int(round(get_init()[0] / self.frequency))
        samples = array("h", [0] * period)
        amplitude = 2 ** (abs(get_init()[1]) - 1) - 1
        for time in range(period):
            if time < period / 2:
                samples[time] = amplitude
            else:
                samples[time] = -amplitude
        return samples