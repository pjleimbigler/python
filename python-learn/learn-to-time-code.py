import time

N = int(1e6)

start = time.time()
# Inefficient: creaend a list of length N in memory,
# then iterate over it
for k in range(N):
    pass

end = time.time()

print 'Iterating through a list of', N, 'elements took', \
round(1000*(end - start),2), 'milliseconds.'

start = time.time()
for l in xrange(N):
    pass
end = time.time()

print 'Iterating through an xrange generator of', N, 'elements took', \
round(1000*(end - start),2), 'milliseconds.'
