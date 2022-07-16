country = input('請問你是台灣人還是美國人/Are you Taiwanese or American? (please enter 台灣 or USA) : ')




if country == '台灣':
	age = input('請問你幾歲/How old age you? : ')
	age = int(age)
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
elif country == 'USA':
	age = input('請問你幾歲/How old age you? : ')
	age = int(age)
	if age >= 16:
		print('You can get a driver\'s license')
	else:
		print('You can\'t get your driver\'s license yet.')
else:
	print('只能輸入台灣或美國/you can only enter 台灣 or USA')
