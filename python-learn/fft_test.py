from numpy import fft, array

# timedomain = array([0, 0.5, 1, 0.5, 0, -0.5, -1, -0.5, 0])
s = 'That\'s the joke.'
td = array([ord(c) for c in s])
fd = fft.fft(td)
print fd
