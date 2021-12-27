#  File: Benford.py

#  Description: This program will output the frequency of first digits in data (count and actual percentage) 

#  Student Name: anna dougharty

#  Student UT EID: amd5933

#  Course Name: CS 303E

#  Unique Number: 51635

#  Date Created: 4/23

#  Date Last Modified: 4/23

def main():
  pop_num = []
  inFile = open ("Census_2009.txt", "r")
  count = 0
  for line in inFile:
    if (count == 0):
      count += 1
      continue
    else:
      count += 1
      line = line.strip()
      word_list = line.split()
      pop_num.append (word_list[-1])
  # pop_num is a list that contains all the population numbers

  # Create an empty dictionary. Keys = First digit, Values = Frequency (initially zero)
  freq_dict = {}
  for i in range (1, 10):
    freq_dict[i] = 0
  # Go through the pop_num list and chec kthe first digit. Add one to the respective digit in freq_dict
  count = 0
  for elt in pop_num:
    elt = str(elt)
    first_digit = elt[0]
    first_digit = int (first_digit)
    freq_dict[first_digit] += 1
    count += 1
  # Freq_dict has keys (first digits) and values (number of times that digit is shown in pop_num as first digit)
  # Output all the keys, the values, and the percentage of freequency
  print ("Digit     Count    %")
  i = 1
  for key in freq_dict:
    percentage = freq_dict[key] / count * 100
    percentage = float(percentage)
    percentage = round(percentage, 1)
    percentage = str (percentage)
    print(str(i) + "          " + str(freq_dict[key]).ljust(4) + "    " + percentage)
    i = i + 1
  
  inFile.close()
main()
