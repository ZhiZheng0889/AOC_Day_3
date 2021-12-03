#import re to more efficiently create a list from the text file
import re
import statistics
from statistics import mode
from collections import Counter

#Open day 1 input text file
my_file = open("Day3.txt", "r")

#Create a list to put the inputs from Day1.txt into
day3inputlist = []

#Looping the inputs into the list
for line in my_file:
    day3inputlist = list(map(str, re.findall('\d+', my_file.read())))
my_file.close()

print(day3inputlist)

#Part 1 of the AOC Day 3 question
#i equal to the counter for locating the integers in the list
i = 0

digit1list = []
digit2list = []
digit3list = []
digit4list = []
digit5list = []
digit6list = []
digit7list = []
digit8list = []
digit9list = []
digit10list = []
digit11list = []
digit12list = []

#Looping through the list to find increase and decrease for each measurement

for i in range(i, len(day3inputlist)):

    try:
        digit = day3inputlist[i]
        digit1list.append(digit[0])
        digit2list.append(digit[1])
        digit3list.append(digit[2])
        digit4list.append(digit[3])
        digit5list.append(digit[4])
        digit6list.append(digit[5])
        digit7list.append(digit[6])
        digit8list.append(digit[7])
        digit9list.append(digit[8])
        digit10list.append(digit[9])
        digit11list.append(digit[10])
        digit12list.append(digit[11])

    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

digit1 = int(mode(digit1list))
digit2 = int(mode(digit2list))
digit3 = int(mode(digit3list))
digit4 = int(mode(digit4list))
digit5 = int(mode(digit5list))
digit6 = int(mode(digit6list))
digit7 = int(mode(digit7list))
digit8 = int(mode(digit8list))
digit9 = int(mode(digit9list))
digit10 = int(mode(digit10list))
digit11 = int(mode(digit11list))
digit12 = int(mode(digit12list))

gammarate = [digit1, digit2, digit3, digit4, digit5, digit6, digit7, digit8, digit9, digit10, digit11, digit12]

least_common1 = Counter(digit1list).most_common()[-1]
least_common2 = Counter(digit2list).most_common()[-1]
least_common3 = Counter(digit3list).most_common()[-1]
least_common4 = Counter(digit4list).most_common()[-1]
least_common5 = Counter(digit5list).most_common()[-1]
least_common6 = Counter(digit6list).most_common()[-1]
least_common7 = Counter(digit7list).most_common()[-1]
least_common8 = Counter(digit8list).most_common()[-1]
least_common9 = Counter(digit9list).most_common()[-1]
least_common10 = Counter(digit10list).most_common()[-1]
least_common11 = Counter(digit11list).most_common()[-1]
least_common12 = Counter(digit12list).most_common()[-1]

print(least_common1)

eplisonrate = [int(least_common1[0]), int(least_common2[0]), int(least_common3[0]), int(least_common4[0]),
                int(least_common5[0]), int(least_common6[0]), int(least_common7[0]), int(least_common8[0]),
                int(least_common9[0]), int(least_common10[0]), int(least_common11[0]), int(least_common12[0])]

print(gammarate)
print(eplisonrate)

num = 0
for b in gammarate:
    num = 2 * num + b
print(num) # 6

num2 = 0
for b in eplisonrate:
    num2 = 2 * num2 + b
print(num2) # 6

print(f'The power consumption of the submarine is {num*num2}!')

#Part 2 of the AOC Day 3 question
j = 0
k = 0
test = 1
for j in range(j, len(gammarate)):
    #for k in range(k, len(day3inputlist)):
    while test > 0:
        if gammarate[j] == 0 and day3inputlist[k][j] == '1':
            day3inputlist = day3inputlist.pop(day3inputlist[k])
            print(day3inputlist)
        elif gammarate[j] == 1 and day3inputlist[k][j] == '0':
            day3inputlist = day3inputlist.pop(day3inputlist[k])
            print(day3inputlist)
        else:
            test = 0

print(day3inputlist)