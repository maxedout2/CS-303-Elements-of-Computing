# File: Project3.py
# Student: Anna Dougharty
# UT EID: amd5933
# Course Name: CS303E
# 
# Date Created: 5.3.21
# Date Last Modified: 5.3.21
# Description of Program: Building a query processing utility for covid cases file

covid = open("county-covid-data.txt", "r")

countylist = []
dictionary = {}
line = covid.readline()
totalconfirmed = []
totaldeaths = []
while line:
    line.strip
    x = line.split(',')
    first = x[0]
    if first[0] == '#':
        exit
    else:
        countylist.append(x[0])
        val1 = (int(x[1]), int(x[3]))
        totalconfirmed.append(int(x[1]))
        totaldeaths.append(int(x[3]))
        dictionary[x[0]] = val1
    line = covid.readline()
val2 = (sum(totalconfirmed), sum(totaldeaths))
dictionary['Texas'] = val2


print("Welcome to the Texas Covid Database Dashboard.")
print("This provides Covid data in Texas as of 1/26/21.")
print("Creating dictionary from file: county-covid-data.txt\n")

print("Enter any of the following commands:")
print("Help - list available commands;\nQuit - exit this dashboard;\nCounties - list all Texas counties;")
print("Cases <countyName>/Texas - confirmed Covid cases in specified county or statewide;\nDeaths <countyName>/Texas - Covid deaths in specified county or statewide.")

action = input("\nPlease Enter a command: ")
while action.lower() != 'quit':
    if action.lower() == 'help':
        print("Help - list available commands;\nQuit - exit this dashboard;\nCounties - list all Texas counties;")
        print("Cases <countyName>/Texas - confirmed Covid cases in specified county or statewide;\nDeaths <countyName>/Texas - Covid deaths in specified county or statewide.")
    elif action.lower() == 'counties':
        n = int(len(countylist)/11)
        for i in range(n):
            print(", ".join(countylist[i*10:(i+1)*10]))
    elif action.lower().split(' ',1)[0] == 'cases':
        if action.title().split(' ',1)[1] in countylist:
            x = dictionary[action.title().split(' ',1)[1]]
            cases = x[0]
            print(action.title().split(' ',1)[1], "county has", str(cases), "confirmed Covid cases.")
        elif action.title().split(' ',1)[1] == 'Texas':
            x = dictionary[action.title().split(' ',1)[1]]
            cases = x[0]
            print(action.title().split(' ',1)[1], "total confirmed Covid cases:", str(cases))
        else:
            print("County", action.title().split(' ',1)[1],"is not recognized.")
    elif action.lower().split(' ',1)[0] == 'deaths':
        if action.title().split(' ',1)[1] in countylist:
            y = dictionary[action.title().split(' ',1)[1]]
            deaths = y[1]
            print(action.title().split(' ',1)[1], "county has", str(deaths), "fatalities.")
        elif action.title().split(' ',1)[1] == 'Texas':
            y = dictionary[action.title().split(' ',1)[1]]
            deaths = y[1]
            print(action.title().split(' ',1)[1], "total confirmed Covid deaths:", str(deaths))
        else:
            print("County", action.title().split(' ',1)[1],"is not recognized.")
    else:
        print("Command is not recognized.  Try again!")
    action = input("\nPlease Enter a command: ")
print("Thank you for using the Texas Covid Database Dashboard.  Goodbye!\n")
covid.close()
