#########################################################
#programmer: Kyle Walter Schademan
#Date: 12/19/2014
#Last updated: 12/19/2014
#
#Program description:  This module is designed to 
#    complete a fourier transform on any square wave
#    and provide the amplitudes, frequencies, and 
#    phases of each of the component waves.  Catch 
#    them waves bro!
#########################################################

import numpy as np
import matplotlib.pyplot as plt

class wave:
    'contains a wave'

    def __init__(self, Hz, offset):
        siny = []
        sinx = []
        self.Hz = Hz
        self.offset = offset
        self.siny = [np.sin(2*np.pi*((self.Hz*np.pi)/100)*a + self.offset) 
                     for a in range(100)]
        self.sinx = [b for b in range(100)]
    
    def __add__(self, other):
        _temp = wave(.25, 0)
        _temp.siny = [x+y for x, y in zip(self.siny, other.siny)]
        return _temp
        
    def display(self):
        f = plt.figure()
        sp = f.add_subplot(111)
        sp.plot(self.sinx, self.siny)
        