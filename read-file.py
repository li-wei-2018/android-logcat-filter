# This snippet demonstrates how to read a file, show it on a screen, and how to add a filter.
# To use the filter make sure 

import sys

if len(sys.argv) > 1:
    filenameIn = sys.argv[1]
else:
    filenameIn = raw_input('Please input a file name: ')

filenameInPeriodIndex = filenameIn.rfind('.')
if filenameInPeriodIndex == -1:
    filenameInWithNoExtention = filenameIn
    filenameInExtention = ''
else:
    filenameInWithNoExtention = filenameIn[:filenameInPeriodIndex]
    filenameInExtention = filenameIn[filenameInPeriodIndex:]

print 'DEBUG: filenameInPeriodIndex: ' + str(filenameInPeriodIndex)
print 'DEBUG: filenameIn: ' + filenameIn
print 'DEBUG: filenameInWithNoExtention: ' + filenameInWithNoExtention
print 'DEBUG: filenameInExtention: ' + filenameInExtention
filenameOut = filenameInWithNoExtention + '-filtered' + filenameInExtention

if len(sys.argv) > 2:
    filter = sys.argv[2]
else:
    filter = raw_input('Please input a filter: ')

print 'filter: ' + filter

fileIn = open(filenameIn, 'rU')
fileOut = open(filenameOut, 'w')

for line in fileIn:
    if line.find(filter) != -1:
        fileOut.write(line)
        # Has a trailing comma "," so that `print` doesn't add an extra end-of-line char.
        #print line,


fileIn.close()
fileOut.close()



