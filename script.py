# import sys

# args = sys.argv[:3]

path = input("Enter file path : ") 
chr = input("Fill in with : ") 

args = [ "script.py", path, chr ]

commentLib = {
    "py" : "#",
    "php" : "//",
    "js" : "//",
    "java" : "//",
    "c" : "//",
    "cpp" : "//",
    "txt" : " ",
    "doc" : " "
}

fname = str(args[1])
fnameSplitArray = fname.split('.')

try:
    comment = commentLib[ fnameSplitArray[ len( fnameSplitArray ) -1 ] ]
except:
    print("Cant fill this type of file ")

character = "."
fLength = -1

if len( args ) > 2:
    character = args[2]
    if len( character ) > 1:
        character += " "

try:
    if fLength == -1:
        with open(fname) as f:
            for l in f:
                l = l.rstrip()
                if fLength < len ( l ):
                    fLength = len ( l )
except:
  print("Cant open file")       

fLength +=2                    

fr = open( fname , 'r')
fw = open("output.txt", 'w')

lines = fr.readlines()

for line in lines:

    line = line.rstrip().rstrip('\n')
    lineLength = len( line )

    if lineLength < fLength :

        if line.strip() != "":
            lineExtension = "  " + comment
            diff = fLength - ( lineLength )
        else:
            lineExtension = comment
            diff = fLength - ( lineLength ) + 2
        
        lineExtension += character*diff
        line += lineExtension

        print(line +"\n"  , end="", file=fw)

    else:
        print(line + "\n" , end="", file=fw)


fr.close()
fw.close()

print ( "Output generated!" )
