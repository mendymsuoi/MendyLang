builtIn={"print":"print"}
def ConvertTokensToPython(tokens):
	out=""
	inAnEasyString=False
	for token in tokens:
		if inAnEasyString:
			out+=token
		elif token in builtIn:
			out+=builtIn[token]
		elif token=="/":
			out+="(\""
			inAnEasyString=True
	if inAnEasyString:
		out+="\")"
	return out