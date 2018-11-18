import sys

# Not finshed Yet"



def ReadFromFile(FileName, s):
	FileName = FileName+"_"+s+".text"
	file = open(FileName, “r”): 
	print(file.read())
	f.close()
	return None

def main():
	suffix = sys.argv[1]
	query = sys.argv[2]
	
	ReadFromFile("tmpUP", suffix)
	
main()