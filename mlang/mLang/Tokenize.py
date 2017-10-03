def tokenize(line):
	if line.endswith("\n"):
		line=line[:len(line)-1]
	atToken=0
	openParens=0
	closeParens=0
	tokens=['']
	restIsString=False
	inNumber=False
	inCharacter=False
	for character in line:
		if character==" ":
			if restIsString:
				tokens[len(tokens)-1]+=" "
				inNumber=False
				continue
		elif character in ["+", "-", "*", "**", "%"]:
			inNumber=False
			tokens.append(character)
			tokens.append("")
		elif character in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
			if inNumber:
				tokens[len(tokens)-1]+=character
			else:
				inNumber=True
				tokens.append("")
				tokens[len(tokens)-1]+=character
		elif character=="/":
			inNumber=False
			tokens.append("/")
			tokens.append("")
			restIsString=True
			continue
		else:
			if not inCharacter:
				tokens[len(tokens)-1]+="\""
				
			if inCharacter:
				tokens[len(tokens)-1]+=character
			inNumber=False
			continue
	if inCharacter:
		tokens[len(tokens)-1]+="\""
	return tokens
