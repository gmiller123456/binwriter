#!/user/bin/python
from lib import BinWriter
from lib import FileListGetter
import os

def useage():
    print("convert.py -- Converts ASCII NASA JPL DE files to binary format.")
    print("Useage:")
    print("convert.py [denum]")
    print("   [denum] - required - the version of the DE to look for (e.g. 405, 431t, etc)")
    print("   -p ASCII file path [Default is current directory]")
    print("   -r Start JD End JD [Default is all matching files]")
    print("   -h ASCII header file [Default 'header.[denum]' e.g. 'header.405']")
    print("   -o Output binary file [Default 'jpleph.[denum] in same path as ASCII files]")
    print()
    print("Examples:")
    print("   convert.py 431t -p \"c:\\asciifiles\\\" -o \"c:\\binfiles\\jpleph.431t\"")
    print("   convert.py 405 -r 2451536.5 2458864.5")
    print()
    print("ASCII file names are assumed to match asc*.[denum] and are in the proper")
    print("order when sorted alphabetically")


path="E:\\Astronomy\\_Ephemeris\\Development Ephemeris Data\\planets\\ascii\\de405\\"
denum="405"
outputFile="ephtest.405"
processAllFiles=False
startJD=2451536.5
endJD=  2451567.5
headerFile="header."+denum

lg=FileListGetter.FileListGetter(denum,path,processAllFiles,startJD,endJD)
headerFile=os.path.join(path,headerFile)

if processAllFiles==True:
    startJD=lg.startJD
    endJD=lg.endJD
else:
    if startJD<lg.startJD:
        startJD=lg.startJD
    if endJD>lg.endJD:
        endJD=lg.endJD

h=BinWriter.FileWriter(denum,headerFile,lg.files,outputFile,startJD,endJD)