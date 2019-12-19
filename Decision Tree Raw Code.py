from xlrd import open_workbook
import math

def information_gain (take1, take2, take3):
    sum = take1 + take2 + take3
    if (take1 == 0):
        part1 = 0
    else:
        part1 = ((-take1)/sum) * math.log2(take1/sum)
    if (take2 == 0):
        part2 = 0
    else:
        part2 = ((-take2)/sum) * math.log2(take2/sum)
    if (take3 == 0):
        part3 = 0
    else:
        part3 = ((-take3)/sum) * math.log2(take3/sum)
    return (part1+part2+part3)

def entropy (t1, t1e, t2, t2e, t3, t3e, sum):
    result = ((t1/sum)*t1e) + ((t2/sum)*t2e) + ((t3/sum)*t3e)
    return  result

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

last_column_entropy = (((-weak)/(number_of_rows - 1))*math.log2(weak/(number_of_rows - 1)) + ((-medium)/(number_of_rows - 1))*math.log2(medium/(number_of_rows - 1)) + ((-strong)/(number_of_rows - 1))*math.log2(strong/(number_of_rows - 1)))

l1_info_gain = information_gain(l1_weak, l1_medium, l1_strong)
l2_info_gain = information_gain(l2_weak, l2_medium, l2_strong)
l3_info_gain = information_gain(l3_weak, l3_medium, l3_strong)
length_entropy = entropy(l1, l1_info_gain, l2, l2_info_gain, l3, l3_info_gain, (number_of_rows - 1))
length_final_gain = last_column_entropy - length_entropy

u1_info_gain = information_gain(u1_weak, u1_medium, u1_strong)
u2_info_gain = information_gain(u2_weak, u2_medium, u2_strong)
u3_info_gain = information_gain(u3_weak, u3_medium, u3_strong)
upper_entropy = entropy(u1, u1_info_gain, u2, u2_info_gain, u3, u3_info_gain, (number_of_rows - 1))
upper_final_gain = last_column_entropy - upper_entropy

lo1_info_gain = information_gain(lo1_weak, lo1_medium, lo1_strong)
lo2_info_gain = information_gain(lo2_weak, lo2_medium, lo2_strong)
lo3_info_gain = information_gain(lo3_weak, lo3_medium, lo3_strong)
lower_entropy = entropy(lo1, lo1_info_gain, lo2, lo2_info_gain, lo3, lo3_info_gain, (number_of_rows - 1))
lower_final_gain = last_column_entropy - lower_entropy

d1_info_gain = information_gain(d1_weak, d1_medium, d1_strong)
d2_info_gain = information_gain(d2_weak, d2_medium, d2_strong)
d3_info_gain = information_gain(d3_weak, d3_medium, d3_strong)
digit_entropy = entropy(d1, d1_info_gain, d2, d2_info_gain, d3, d3_info_gain, (number_of_rows - 1))
digit_final_gain = last_column_entropy - digit_entropy

s1_info_gain = information_gain(s1_weak, s1_medium, s1_strong)
s2_info_gain = information_gain(s2_weak, s2_medium, s2_strong)
s3_info_gain = information_gain(s3_weak, s3_medium, s3_strong)
special_entropy = entropy(s1, s1_info_gain, s2, s2_info_gain, s3, s3_info_gain, (number_of_rows - 1))
special_final_gain = last_column_entropy - special_entropy

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

if (lowcnt <= 3):
    if (digitcnt <= 3):
        if (upcnt <= 3):
            print("Strong")
        elif (upcnt >= 4 and upcnt <= 7):
            print("Medium")
        elif (upcnt >= 8):
            print("Weak")
    elif (digitcnt >= 4 and digitcnt <= 7):
        if (upcnt <= 3):
            print("Strong")
        elif (upcnt >= 4 and upcnt <= 7):
            print("Medium")
        elif (upcnt >= 8):
            print("Weak")
    elif (digitcnt >= 8):
        print("Strong")

elif (lowcnt >= 4 and lowcnt <= 7):
    if (digitcnt <= 3):
        if (upcnt <= 3):
            if (specnt <= 3):
                if (take2 == 1):
                    print("Strong")
                elif (take2 == 2):
                    print("Strong")
                elif (take2 == 3):
                    print("Medium")
            elif (specnt >= 4 and specnt <= 7):
                print("Strong")
            elif (specnt >=8):
                print("Strong")
        elif (upcnt >= 4 and upcnt <= 7):
            print("Medium")
        elif (upcnt >= 8):
            print("Medium")
    elif (digitcnt >= 4 and digitcnt <= 7):
        print("Strong")
    elif (digitcnt >= 8):
        print("Strong")
elif (lowcnt >= 8):
    if (digitcnt <= 3):
        print("Weak")
    elif (digitcnt >= 4 and digitcnt <= 7):
        print("Medium")
    elif (digitcnt >= 8):
        print("Medium")
