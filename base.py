#!/usr/bin/python
import test
import converter
cBase = ""
cNumber = list()
nBase = ""
ndNumber = 0
nsNumber = ""
temp_holder = 0

# Will retrieve the user's current base, verify the information,
# and convert it to an integer.
check = True
while check:
    check_two = False
    s_cBase = raw_input("Enter the current base from 2 to 35. ")
    check_two = test.check_integer(s_cBase)
    if check_two:
        cBase = int(s_cBase)
        check = False
    if cBase < 2 or cBase > 35:
        check = True

# Will retrive the user's number in the current base, verify the information,
# and place it in a list(array) to prepare it for conversion.
check = True
while check:
    check_two = False
    s_cNumber = raw_input("Enter the current number. ")
    check_two = test.check_base(s_cNumber, cBase)
    if check_two:
        check = False
        for z in s_cNumber:
            cNumber.append(test.letter_to_number(z))

# Will retrive the user's new base, verify the information,
# and convert it to an integer.
check = True
while check:
    check_two = False
    s_nBase = raw_input("Enter the new base from 2 to 35. ")
    check_two = test.check_integer(s_nBase)
    if check_two:
        nBase = int(s_nBase)
        check = False
    if cBase < 2 or cBase > 35:
        check = True

if cBase == nBase:
    print s_cNumber
elif nBase == 10:
    ndNumber = converter.convert_to_ten(cNumber, cBase)
    print ndNumber
elif nBase != 10:
    temp_holder = converter.convert_to_ten(cNumber, cBase)
    nsNumber = converter.convert_to_nonten(temp_holder, nBase)
    print nsNumber
else:
    print "Something went wrong"
