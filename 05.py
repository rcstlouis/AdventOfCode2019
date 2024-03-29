ADD = 1
MULT = 2
IN = 3
OUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8

HALT = 99
POSITION_MODE = 0
IMMEDIATE_MODE = 1

import csv

def runProgram(intCodeArray, input):
    pointer = 0
    input = input
    instruction = intCodeArray[pointer] % 100
    while(instruction != HALT):
        if(instruction == ADD):
            toAdd1 = getParameter(intCodeArray, pointer, 1)
            toAdd2 = getParameter(intCodeArray, pointer, 2)
            intCodeArray[intCodeArray[pointer + 3]] = toAdd1 + toAdd2
            pointer += 4
        elif(instruction == MULT):
            toMult1 = getParameter(intCodeArray, pointer, 1)
            toMult2 = getParameter(intCodeArray, pointer, 2)
            intCodeArray[intCodeArray[pointer + 3]] = toMult1 * toMult2
            pointer += 4
        elif(instruction == IN):
            if intCodeArray[pointer] // 100 == POSITION_MODE:
                intCodeArray[intCodeArray[pointer + 1]] = input
            elif intCodeArray[pointer] // 100 == IMMEDIATE_MODE:
                intCodeArray[pointer + 1] = input
            else:
                print('Invalid mode on input instruction at position ' + str(pointer) + ': ' + str(intCodeArray[pointer]))
            pointer += 2
        elif(instruction == OUT):
            print('Output position: ' + str(intCodeArray[intCodeArray[pointer + 1]]))
            print('Output immediate: ' + str(intCodeArray[pointer + 1]))
            print('Output As Told: ' + str(getParameter(intCodeArray, pointer, 1)))
            # if intCodeArray[pointer] // 100 == POSITION_MODE:
            #     print('Output' + str(intCodeArray[pointer + 1]))
            # elif intCodeArray[pointer] // 100 == IMMEDIATE_MODE:
            #     print('Output' + str(intCodeArray[intCodeArray[pointer + 1]]))
            # else:
            #     print('Invalid mode on output instruction at position ' + str(pointer) + ': ' + str(intCodeArray[pointer]))
            pointer += 2
        elif(instruction == JUMP_IF_TRUE):
            # Jump if first parameter is not zero
            if getParameter(intCodeArray, pointer, 1) != 0:
                pointer = getParameter(intCodeArray, pointer, 2)
            else:
                pointer += 3
        elif(instruction == JUMP_IF_FALSE):
            # Jump if the first parameter is zero
            if getParameter(intCodeArray, pointer, 1) == 0:
                pointer = getParameter(intCodeArray, pointer, 2)
            else:
                pointer += 3
        elif(instruction == LESS_THAN):
            # Store 1 at address third if first is less than second, else store 0
            isLessThan = 0
            if getParameter(intCodeArray, pointer, 1) < getParameter(intCodeArray, pointer, 2):
                isLessThan = 1
            if getModeOfParameter(intCodeArray, pointer, 3) == POSITION_MODE:
                intCodeArray[intCodeArray[pointer + 3]] = isLessThan
            elif getModeOfParameter(intCodeArray, pointer, 3) == IMMEDIATE_MODE:
                intCodeArray[pointer + 3] = isLessThan
            pointer += 4
        elif(instruction == EQUALS):
            isEqual = 0
            if getParameter(intCodeArray, pointer, 1) == getParameter(intCodeArray, pointer, 2):
                isEqual = 1
            if getModeOfParameter(intCodeArray, pointer, 3) == POSITION_MODE:
                intCodeArray[intCodeArray[pointer + 3]] = isEqual
            elif getModeOfParameter(intCodeArray, pointer, 3) == IMMEDIATE_MODE:
                intCodeArray[pointer + 3] = isEqual
            pointer += 4
        else:
            print("Invalid op: " + str(instruction) + " at position " + str(pointer))
            print(str(intCodeArray))
            break
        instruction = intCodeArray[pointer] % 100

def getParameter(intCodeArray, pointer, parameterNumber):
    modeDigit = 10 * (10**parameterNumber)
    if (intCodeArray[pointer] // modeDigit) % 10 == POSITION_MODE:
        return intCodeArray[intCodeArray[pointer + parameterNumber]]
    elif (intCodeArray[pointer] // modeDigit) % 10 == IMMEDIATE_MODE:
        return intCodeArray[pointer + parameterNumber]
    return None

def getModeOfParameter(intCodeArray, pointer, parameterNumber):
    return (intCodeArray[pointer] // (10 * (10**parameterNumber))) % 10

def main():
    inputArray = 0 #dummy value
    with open("input05.txt", "r") as fr:
        output = csv.reader(fr) #grab the list of columns in the first (and only) csv row
        for row in output:
            inputArray = row.copy()
    for i in range(len(inputArray)):
        inputArray[i] = int(inputArray[i])
    print("running")
    intCodeArray = inputArray.copy()
    runProgram(intCodeArray, 1)
    print("Final state" + str(intCodeArray))

def main2():
    inputArray = 0 #dummy value
    with open("input05.txt", "r") as fr:
        output = csv.reader(fr) #grab the list of columns in the first (and only) csv row
        for row in output:
            inputArray = row.copy()
    for i in range(len(inputArray)):
        inputArray[i] = int(inputArray[i])
    print("running")
    intCodeArray = inputArray.copy()
    runProgram(intCodeArray, 5)
    print("Final state" + str(intCodeArray))

if __name__ == "__main__":
    # main()
    main2()