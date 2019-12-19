from xlrd import open_workbook
import math

class Part1(object):
    def __init__(self, length: object, upper : object, lower: object, digit: object, special: object, strength: object) -> object:
        self.length = length
        self.upper = upper
        self.lower = lower
        self.digit = digit
        self.special = special
        self.strength = strength

    def __str__(self):
        return("Part1 object:\n"
               "  Length = {0}\n"
               "  Upper = {1}\n"
               "  Lower = {2} \n"
               "  Digit = {3} \n"
               "  Special = {4} \n"
               "  Strength = [5]"
               .format(self.length, self.upper, self.lower, self.digit, self.special, self.strength))

wb = open_workbook('New_Data_Set.xlsx')
worksheet = wb.sheet_by_name("Sheet1")

for sheet in wb.sheets():
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols
    items = []
    rows = []

    weak = medium = strong = 0

    l1_weak = l1_medium = l1_strong = 0
    l2_weak = l2_medium = l2_strong = 0
    l3_weak = l3_medium = l3_strong = 0

    u1_weak = u1_medium = u1_strong = 0
    u2_weak = u2_medium = u2_strong = 0
    u3_weak = u3_medium = u3_strong = 0

    lo1_weak = lo1_medium = lo1_strong = 0
    lo2_weak = lo2_medium = lo2_strong = 0
    lo3_weak = lo3_medium = lo3_strong = 0

    d1_weak = d1_medium = d1_strong = 0
    d2_weak = d2_medium = d2_strong = 0
    d3_weak = d3_medium = d3_strong = 0

    s1_weak = s1_medium = s1_strong = 0
    s2_weak = s2_medium = s2_strong = 0
    s3_weak = s3_medium = s3_strong = 0

    for row in range(1, number_of_rows):
        values = []
        for col in range(number_of_columns):
            value = (sheet.cell(row,col).value)

            if (sheet.cell(row,col).value == 'weak'):
                weak += 1

                if (sheet.cell(row,0).value == 1):
                    l1_weak += 1
                elif (sheet.cell(row,0).value == 2):
                    l2_weak += 1
                elif (sheet.cell(row,0).value == 3):
                    l3_weak += 1

                if (sheet.cell(row,1).value <= 3):
                    u1_weak += 1
                elif (sheet.cell(row,1).value >= 4 and sheet.cell(row,1).value <= 7):
                    u2_weak += 1
                elif (sheet.cell(row,1).value >= 8):
                    u3_weak += 1

                if (sheet.cell(row,2).value <= 3):
                    lo1_weak += 1
                elif (sheet.cell(row,2).value >= 4 and sheet.cell(row,2).value <= 7):
                    lo2_weak += 1
                elif (sheet.cell(row,2).value >= 8):
                    lo3_weak += 1

                if (sheet.cell(row,3).value <= 3):
                    d1_weak += 1
                elif (sheet.cell(row,3).value >= 4 and sheet.cell(row,3).value <= 7):
                    d2_weak += 1
                elif (sheet.cell(row,3).value >= 8):
                    d3_weak += 1

                if (sheet.cell(row,4).value <= 3):
                    s1_weak += 1
                elif (sheet.cell(row,4).value >= 4 and sheet.cell(row,4).value <= 7):
                    s2_weak += 1
                elif (sheet.cell(row,4).value >= 8):
                    s3_weak += 1



            elif (sheet.cell(row,col).value == 'medium'):
                medium += 1

                if (sheet.cell(row,0).value == 1):
                    l1_medium += 1
                elif (sheet.cell(row,0).value == 2):
                    l2_medium += 1
                elif (sheet.cell(row,0).value == 3):
                    l3_medium += 1

                if (sheet.cell(row,1).value <= 3):
                    u1_medium += 1
                elif (sheet.cell(row,1).value >= 4 and sheet.cell(row,1).value <= 7):
                    u2_medium += 1
                elif (sheet.cell(row,1).value >= 8):
                    u3_medium += 1

                if (sheet.cell(row,2).value <= 3):
                    lo1_medium += 1
                elif (sheet.cell(row,2).value >= 4 and sheet.cell(row,2).value <= 7):
                    lo2_medium += 1
                elif (sheet.cell(row,2).value >= 8):
                    lo3_medium += 1

                if (sheet.cell(row,3).value <= 3):
                    d1_medium += 1
                elif (sheet.cell(row,3).value >= 4 and sheet.cell(row,3).value <= 7):
                    d2_medium += 1
                elif (sheet.cell(row,3).value >= 8):
                    d3_medium += 1

                if (sheet.cell(row,4).value <= 3):
                    s1_medium += 1
                elif (sheet.cell(row,4).value >= 4 and sheet.cell(row,4).value <= 7):
                    s2_medium += 1
                elif (sheet.cell(row,4).value >= 8):
                    s3_medium += 1

            elif (sheet.cell(row, col).value == 'strong'):
                strong += 1

                if (sheet.cell(row, 0).value == 1):
                    l1_strong += 1
                elif (sheet.cell(row, 0).value == 2):
                    l2_strong += 1
                elif (sheet.cell(row, 0).value == 3):
                    l3_strong += 1

                if (sheet.cell(row,1).value <= 3):
                    u1_strong += 1
                elif (sheet.cell(row,1).value >= 4 and sheet.cell(row,1).value <= 7):
                    u2_strong += 1
                elif (sheet.cell(row,1).value >= 8):
                    u3_strong += 1

                if (sheet.cell(row,2).value <= 3):
                    lo1_strong += 1
                elif (sheet.cell(row,2).value >= 4 and sheet.cell(row,2).value <= 7):
                    lo2_strong += 1
                elif (sheet.cell(row,2).value >= 8):
                    lo3_strong += 1

                if (sheet.cell(row,3).value <= 3):
                    d1_strong += 1
                elif (sheet.cell(row,3).value >= 4 and sheet.cell(row,3).value <= 7):
                    d2_strong += 1
                elif (sheet.cell(row,3).value >= 8):
                    d3_strong += 1

                if (sheet.cell(row,4).value <= 3):
                    s1_strong += 1
                elif (sheet.cell(row,4).value >= 4 and sheet.cell(row,4).value <= 7):
                    s2_strong += 1
                elif (sheet.cell(row,4).value >= 8):
                    s3_strong += 1

            try:
                value = str(int(value))
            except ValueError:
                pass
            finally:
                values.append(value)
        item = Part1(*values)
        items.append(item)

l1 = l1_weak + l1_medium + l1_strong
l2 = l2_weak + l2_medium + l2_strong
l3 = l3_weak + l3_medium + l3_strong

u1 = u1_weak + u1_medium + u1_strong
u2 = u2_weak + u2_medium + u2_strong
u3 = u3_weak + u3_medium + u3_strong

lo1 = lo1_weak + lo1_medium + lo1_strong
lo2 = lo2_weak + lo2_medium + lo2_strong
lo3 = lo3_weak + lo3_medium + lo3_strong

d1 = d1_weak + d1_medium + d1_strong
d2 = d2_weak + d2_medium + d2_strong
d3 = d3_weak + d3_medium + d3_strong

s1 = s1_weak + s1_medium + s1_strong
s2 = s2_weak + s2_medium + s2_strong
s3 = s3_weak + s3_medium + s3_strong

weak_probability = weak/(number_of_rows-1)
medium_probability = medium/(number_of_rows-1)
strong_probability = strong/(number_of_rows-1)

l1_over_weak = l1_weak/weak
l1_over_medium = l1_medium/medium
l1_over_strong = l1_strong/strong

l2_over_weak = l2_weak/weak
l2_over_medium = l2_medium/medium
l2_over_strong = l2_strong/strong

l3_over_weak = l3_weak/weak
l3_over_medium = l3_medium/medium
l3_over_strong = l3_strong/strong

u1_over_weak = u1_weak/weak
u1_over_medium = u1_medium/medium
u1_over_strong = u1_strong/strong

u2_over_weak = u2_weak/weak
u2_over_medium = u2_medium/medium
u2_over_strong = u2_strong/strong

u3_over_weak = u3_weak/weak
u3_over_medium = u3_medium/medium
u3_over_strong = u3_strong/strong

lo1_over_weak = lo1_weak/weak
lo1_over_medium = lo1_medium/medium
lo1_over_strong = lo1_strong/strong

lo2_over_weak = lo2_weak/weak
lo2_over_medium = lo2_medium/medium
lo2_over_strong = lo2_strong/strong

lo3_over_weak = lo3_weak/weak
lo3_over_medium = lo3_medium/medium
lo3_over_strong = lo3_strong/strong

d1_over_weak = d1_weak/weak
d1_over_medium = d1_medium/medium
d1_over_strong = d1_strong/strong

d2_over_weak = d2_weak/weak
d2_over_medium = d2_medium/medium
d2_over_strong = d2_strong/strong

d3_over_weak = d3_weak/weak
d3_over_medium = d3_medium/medium
d3_over_strong = d3_strong/strong

s1_over_weak = s1_weak/weak
s1_over_medium = s1_medium/medium
s1_over_strong = s1_strong/strong

s2_over_weak = s2_weak/weak
s2_over_medium = s2_medium/medium
s2_over_strong = s2_strong/strong

s3_over_weak = s3_weak/weak
s3_over_medium = s3_medium/medium
s3_over_strong = s3_strong/strong

take2 = int (input())
take = input()
length = len(take)
upcnt = lowcnt = digitcnt = specnt = 0
for a in range (0, length):
    temp = ord(take[a])
    if (temp >= 65 and temp <= 90):
        upcnt += 1
    elif (temp >= 97 and temp <= 122):
        lowcnt += 1
    elif (temp >= 48 and temp <= 57):
        digitcnt += 1
    else:
        specnt += 1

if (take2 == 1):
    len_take_weak = l1_over_weak
    len_take_medium = l1_over_medium
    len_take_strong = l1_over_strong
elif (take2 == 2):
    len_take_weak = l2_over_weak
    len_take_medium = l2_over_medium
    len_take_strong = l2_over_strong
elif (take2 == 3):
    len_take_weak = l3_over_weak
    len_take_medium = l3_over_medium
    len_take_strong = l3_over_strong

if (upcnt <= 3):
    up_take_weak = u1_over_weak
    up_take_medium = u1_over_medium
    up_take_strong = u1_over_strong
elif (upcnt >= 4 and upcnt <= 7):
    up_take_weak = u2_over_weak
    up_take_medium = u2_over_medium
    up_take_strong = u2_over_strong
elif (upcnt >= 8):
    up_take_weak = u3_over_weak
    up_take_medium = u3_over_medium
    up_take_strong = u3_over_strong

if (lowcnt <= 3):
    low_take_weak = lo1_over_weak
    low_take_medium = lo1_over_medium
    low_take_strong = lo1_over_strong
elif (lowcnt >= 4 and upcnt <= 7):
    low_take_weak = lo2_over_weak
    low_take_medium = lo2_over_medium
    low_take_strong = lo2_over_strong
elif (lowcnt >= 8):
    low_take_weak = lo3_over_weak
    low_take_medium = lo3_over_medium
    low_take_strong = lo3_over_strong

if (digitcnt <= 3):
    digit_take_weak = d1_over_weak
    digit_take_medium = d1_over_medium
    digit_take_strong = d1_over_strong
elif (digitcnt >= 4 and digitcnt <= 7):
    digit_take_weak = d2_over_weak
    digit_take_medium = d2_over_medium
    digit_take_strong = d2_over_strong
elif (digitcnt >= 8):
    digit_take_weak = d3_over_weak
    digit_take_medium = d3_over_medium
    digit_take_strong = d3_over_strong

if (specnt <= 3):
    spe_take_weak = s1_over_weak
    spe_take_medium = s1_over_medium
    spe_take_strong = s1_over_strong
elif (specnt >= 4 and specnt <= 7):
    spe_take_weak = s2_over_weak
    spe_take_medium = s2_over_medium
    spe_take_strong = s2_over_strong
elif (specnt >= 8):
    spe_take_weak = s3_over_weak
    spe_take_medium = s3_over_medium
    spe_take_strong = s3_over_strong

probability_input_over_weak = len_take_weak * up_take_weak * low_take_weak * digit_take_weak * spe_take_weak
probability_input_over_medium = len_take_medium * up_take_medium * low_take_medium * digit_take_medium * spe_take_medium
probability_input_over_strong = len_take_strong * up_take_strong * low_take_strong * digit_take_strong * spe_take_strong

likelyhood = (probability_input_over_weak * weak_probability) + (probability_input_over_medium * medium_probability) + (probability_input_over_strong * strong_probability)

probability_weak_over_input = (probability_input_over_weak * weak_probability)/likelyhood
probability_medium_over_input = (probability_input_over_medium * medium_probability)/likelyhood
probability_strong_over_input = (probability_input_over_strong * strong_probability)/likelyhood

if (probability_weak_over_input > probability_medium_over_input and probability_weak_over_input > probability_strong_over_input):
    print("Weak")
elif (probability_medium_over_input > probability_weak_over_input and probability_medium_over_input > probability_strong_over_input):
    print("Medium")
else:
    print("Strong")
