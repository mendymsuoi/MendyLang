from Tokenize import *
from ConvertTokensToPython import *
import sys

def main():
	
	if len(sys.argv)>1:
		interpreter(True)
	else:
		interpreter(False)

def interpreter(fileOrNot):
	if fileOrNot:
		inputFile=open(sys.argv[1])
		inputFileLines=inputFile.readlines()
		outputFileS='open(sys.argv[1][:len(sys.argv[1])-2]+".py", "w")'
		for line in inputFileLines:
			if line.startswith("//") or line=='':
				continue
			tokens=tokenize(line)
			for token in tokens:
				print(f"'{token}', ", end="")
			print()
			print ("Python:\n", ConvertTokensToPython(token for token in tokens))
			print()
	else:
		command=''
		while True:
			command=input("MMM--> ")
			if command in ['quit', 'quit()', 'q']:
				exit()
			if command=="":
				continue
			print(tokensToPython(tokenize(command)))
			
			
if __name__=="__main__":
	# try:
	main()
	# except EOFError:
	# 	print()
	# 	exit()