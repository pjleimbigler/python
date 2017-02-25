import time

N = int(1e6)

# start time
ts = time.time()
# Inefficient: create a list of length N in memory,
# then iterate over it
for k in range(N):
    k += 1

# end time
te = time.time()

print 'Iterating through a list of', N, 'elements took', 1000*(te - ts), 'milliseconds.'

# start time
ts = time.time()
for l in xrange(N):
    l += 1
# end time
te = time.time()

print 'Iterating through an xrange generator of', N, 'elements took', 1000*(te - ts), 'milliseconds.'
