# Font size problem of Microsoft interview
testCaseNum = int(raw_input())
for i in range(testCaseNum):
	NPWHlist = raw_input().split(' ')
	wordList = raw_input().split(' ')

	pagragraghNum = int(NPWHlist[0])
	pageNum = int(NPWHlist[1])
	screenWidth = int(NPWHlist[2])
	screenHeight = int(NPWHlist[3])
	wordOfParagragh = [0] * pagragraghNum
	for i in range(pagragraghNum):
		wordOfParagragh[i] = int(wordList[i])

	totalWords = sum(wordOfParagragh)
	font = int((pageNum * screenWidth * screenHeight) ** 0.5)
	print font


