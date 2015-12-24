from analysis import number_to_letter

def convert_to_ten(original, base):
	y = -1
	base_ten = 0

	for x in original:
		y += 1

	for x in range(0, y + 1):
		the_a_s = original[y - x]
		the_power = base ** (x)
		base_ten = (the_a_s * the_power) + base_ten
		
	return base_ten

def convert_to_nonten(ten, new_base):
	new_base_array = list()
	non_reverse_array = list()
	reverse_string = ""
	temp_holder = 0
	x = 0
	
	while (ten / (new_base ** x)) > 0:
		temp_holder = (ten / (new_base ** x)) % new_base
		new_base_array.append(temp_holder)
		x += 1

	x = -1
	for y in new_base_array:
		non_reverse_array.append(number_to_letter(y))
		x += 1

	for y in range(0, x + 1):
		reverse_string = reverse_string + non_reverse_array[x - y]

	return reverse_string
