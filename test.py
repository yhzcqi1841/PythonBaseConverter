from analysis import letter_to_number

def check_integer(a):
	holder_one = list()
	answer = True

	for z in a:
		holder_one.append(letter_to_number(z))

	for z in holder_one:
		if z == "error":
			answer = False
			break
		elif z >= 10:
			answer = False
			break
		else:
			answer = True
	return answer

def check_base(a, b):
	holder_one = list()
	answer = True

	for z in a:
		holder_one.append(letter_to_number(z))

	for z in holder_one:
		if z >= b:
			answer = False
	return answer
