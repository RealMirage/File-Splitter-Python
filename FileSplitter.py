import argparse
import sys
import os.path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default="",help="What is the path to the input file?")
    parser.add_argument('--delim', type=str, default="",help="What is the delimiter?")
    parser.add_argument('--column',type=int, default=0,help = "What is the column index? Defaults to 0 if not provided")
    parser.add_argument('--skip', type=int, default=0,help="Are there any lines to skip? E.g. set to 1 if header is present")
    args = parser.parse_args()
    sys.stdout.write(Split(args))

def FileCheck(file):
    try:
        open(file, "r")
        return True
    except IOError:
        print("Check your file path, the file {} does not exist", file)
        return False


def FileWriter(filePath, writeOption, lineData):
    try:
        with open(filePath, writeOption) as writer:
            writer.write(lineData)
    except Exception as e:
        print("Error! {0}".format(e))


def Split(args):
    inputFile = args.input
    linesToSkip = args.skip
    delimiter = args.delim
    splitIndex = args.column

    inputFileNoExtension = os.path.splitext(inputFile)[0]
    splitList = []
    truncOption = "w+"
    appendOption = "a"
    lineNumber = 0
    lineSplitColumn = ""

    #Handling case with Windows Cmd how it passes \t from command line.
    if (delimiter == "\\t"):
        delimiter = "\t"

    if FileCheck(inputFile) == False:
        return "Please check your input file parameter - file may not exist!"

    with open(inputFile) as FileOpener:
        for x in range(linesToSkip):
            FileOpener.readline()
            lineNumber += 1

        for line in FileOpener:
            lineParts = line.strip().split(delimiter)
            try:
                lineSplitColumn = lineParts[splitIndex]
            except:
                return "Error on line {} (count is index 0)! Check the delimiter & column index!".format(lineNumber)
            finally:
                lineNumber += 1

            splitFileName = "{}_{}.txt".format(inputFileNoExtension, lineSplitColumn)

            if lineSplitColumn not in splitList:
                splitList.append(lineSplitColumn)
                FileWriter(splitFileName, truncOption, "")

            FileWriter(splitFileName, appendOption, line)

    return "Sucess! {} was split! {} files were generated.".format(inputFile, len(splitList))

if __name__ == "__main__":
    main()