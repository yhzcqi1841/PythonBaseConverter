def letter_to_number(i):
	j = 0
	if i == "0":
		j = 0
	elif i == "1":
		j = 1
	elif i == "2":
		j = 2
	elif i == "3":
		j = 3
	elif i == "4":
		j = 4
	elif i == "5":
		j = 5
	elif i == "6":
		j = 6
	elif i == "7":
		j = 7
	elif i == "8":
		j = 8
	elif i == "9":
		j = 9
	elif (i == "a") or (i == "A"):
		j = 10
	elif (i == "b") or (i == "B"):
		j = 11
	elif (i == "c") or (i == "C"):
		j = 12
	elif (i == "d") or (i == "D"):
		j = 13
	elif (i == "e") or (i == "E"):
		j = 14
	elif (i == "f") or (i == "F"):
		j = 15
	elif (i == "g") or (i == "G"):
		j = 16
	elif (i == "h") or (i == "H"):
		j = 17
	elif (i == "i") or (i == "I"):
		j = 18
	elif (i == "j") or (i == "J"):
		j = 19
	elif (i == "k") or (i == "K"):
		j = 20
	elif (i == "l") or (i == "L"):
		j = 21
	elif (i == "m") or (i == "M"):
		j = 22
	elif (i == "n") or (i == "N"):
		j = 23
	elif (i == "o") or (i == "O"):
		j = 24
	elif (i == "p") or (i == "P"):
		j = 25
	elif (i == "q") or (i == "Q"):
		j = 26
	elif (i == "r") or (i == "R"):
		j = 27
	elif (i == "s") or (i == "S"):
		j = 28
	elif (i == "t") or (i == "T"):
		j = 29
	elif (i == "u") or (i == "U"):
		j = 30
	elif (i == "v") or (i == "V"):
		j = 31
	elif (i == "w") or (i == "W"):
		j = 32
	elif (i == "x") or (i == "X"):
		j = 33
	elif (i == "y") or (i == "Y"):
		j = 34
	elif (i == "z") or (i == "Z"):
		j = 35
	else:
		j = "error"
	return j

def number_to_letter(i):
	j = ""
	if i == 0:
		j = "0"
	elif i == 1:
		j = "1"
	elif i == 2:
		j = "2"
	elif i == 3:
		j = "3"
	elif i == 4:
		j = "4"
	elif i == 5:
		j = "5"
	elif i == 6:
		j = "6"
	elif i == 7:
		j = "7"
	elif i == 8:
		j = "8"
	elif i == 9:
		j = "9"
	elif i == 10:
		j = "a"
	elif i == 11:
		j = "b"
	elif i == 12:
		j = "c"
	elif i == 13:
		j = "d"
	elif i == 14:
		j = "e"
	elif i == 15:
		j = "f"
	elif i == 16:
		j = "g"
	elif i == 17:
		j = "h"
	elif i == 18:
		j = "i"
	elif i == 19:
		j = "j"
	elif i == 20:
		j = "k"
	elif i == 21:
		j = "l"
	elif i == 22:
		j = "m"
	elif i == 23:
		j = "n"
	elif i == 24:
		j = "o"
	elif i == 25:
		j = "p"
	elif i == 26:
		j = "q"
	elif i == 27:
		j = "r"
	elif i == 28:
		j = "s"
	elif i == 29:
		j = "t"
	elif i == 30:
		j = "u"
	elif i == 31:
		j = "v"
	elif i == 32:
		j = "w"
	elif i == 33:
		j = "x"
	elif i == 34:
		j = "y"
	elif i == 35:
		j = "z"
	else:
		j = "error"
	return j
