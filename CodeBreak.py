# Constraints are dictionary of the following format:
# "number": [a, b] where a is the number of digits which are correct but in the
#           wrong positions and b is the number of digits in the correct position
# Extras:   if a or b == -1, we know nothing about that information
#           [0,0], none of these digits are used

def isValid(num, possibleDigits):
    # Check that all digits are valid
    digits = [int(i) for i in [*num]]
    for d in digits:
        if d not in possibleDigits:
            return False

    # May add later functionality to look for repeated digits

    # Return true if still valid
    return True

def noGood(key, constraints):
    rules = constraints[key]
    if rules[0] == 0 and rules[1] == 0: return True
    return False

def setMinMax(key):
    #minCode = int("1" + "0" * (len(key) - 1))
    minCode = 1
    maxCode = int("9" * len(key))
    return (minCode, maxCode)

def eliminateDigits(key, pd):
    digits = [int(i) for i in [*key]]
    for d in digits:
        if d in pd:
            pd.remove(d)
    return pd

def checksum(act_num, test_num):
    wrong_spot = 0
    right_spot = 0
    
    test_digits = [int(i) for i in [*test_num]]
    act_digits  = [int(i) for i in [*act_num]]
    for index in range(len(test_digits)):
        if test_digits[index] == act_digits[index]:
            right_spot += 1
        elif test_digits[index] in act_digits:
            wrong_spot += 1

    return [wrong_spot, right_spot]

def removeRepeats(sols):
    outSols = []
    for s in sols:
        unique = True
        unique_Digits = []
        str_s = str(s)
        for i in [*str_s]:
            if i in unique_Digits: unique = False
            else: unique_Digits.append(i)
        if unique: outSols.append(s)
    return outSols

#####################################################################################



#constraints = {"9738": [1,-1], "5316": [-1,1], "9186": [2,-1],
#               "8942": [2,-1], "4935": [-1,1], "7625": [0,0], "6579": [0,0]}
#constraints = {"614": [1,-1], "682": [-1,1], "738": [0,0],
#               "206": [2,-1]}
#constraints = {"5816": [1,1], "3826": [2,-1], "1983": [2,-1], "1427": [-1,1]}
constraints = {"9285": [1,-1], "1937": [2,-1], "5201": [-1,1], "6507": [0,0], "8524": [2,-1]}


# Set size of iteration
firstKey = list(constraints.keys())[0]
minCode, maxCode = setMinMax(firstKey)
code_length = len(str(maxCode))

# Set possible digits
possibleDigits = [i for i in range(0,10)]

# Possible solutions
possibleSolutions = []

# Can we eliminate digits
zeroGroup = []
for key in constraints:
    if noGood(key, constraints):
        # Eliminate the digits of the key
        print("Removing digits of", key)
        zeroGroup.append(key)
        possibleDigits = eliminateDigits(key, possibleDigits)

print("Remaining digits in solution:", possibleDigits)

print(f"Iteration range, from {minCode} to {maxCode}")
# Iterate over all remaining combinations
for num_raw in range(minCode, maxCode + 1):
    num_str = "0" * (code_length - len(str(num_raw))) + str(num_raw)
    # Does number only contain possible digits?
    if isValid(num_str, possibleDigits):
        #print("Checking Number string:", num_str)
        
        # Check for validity
        isGood = True
        for c in constraints:
            if c not in zeroGroup:
                r = constraints[c]
                act_r = checksum(num_str, str(c))
                if r[0] == -1   and act_r[0] != 0: isGood = False
                elif r[0] != -1 and act_r[0] != r[0]: isGood = False
                if r[1] == -1   and act_r[1] != 0: isGood = False
                elif r[1] != -1 and act_r[1] != r[1]: isGood = False                
                
        if isGood:
            #print("vs", c, r, act_r)
            possibleSolutions.append(int(num_str))

# Output results without filtering
print()
print("All solutions     :", possibleSolutions)

# With no repeats
print("No repeated digits:", removeRepeats(possibleSolutions))
