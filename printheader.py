from JPLDE import *

#filename="ephtest.405"
filename="jpleph1900-2100.405"
de=JPLDE(filename)

h=de.header
print(h.description)
print(h.startString)
print(h.endString)

print(h.constantNames)

print(h.jdStart)
print(h.jdEnd)
print(h.jdStep)
print(h.numConstants)
print(h.au)
print(h.emrat)

print(h.coeffPtr)

print(h.constants)

print(h.blockSize)

