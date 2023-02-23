import random
import pandas as pd
import csv

# Open file
friendlist = open("/Users/caitlin/Documents/Frienddates/friendlist.csv", 'r')
friendlist = pd.read_csv('/Users/caitlin/Documents/Frienddates/friendlist.csv', header = 0, index_col=0).to_dict()

# Open file
friendlist = {}

with open('/Users/caitlin/Documents/Frienddates/friendlist.csv', mode='r') as inp:
    friendlist = csv.reader(inp)
    #friendlist = {rows[0]:rows[23] for rows in reader}

print(friendlist)

# Dictionary that stores friends as keys and previous matches as values
#friendlist = {'Liz': ['JuanPa', 'Jordan', 'Kateri'],
              'JuanPa': ['Liz', 'Aleda'],
              'Sarah': 'Elliot',
              'Atza': ['Ernest', 'Elliot'],
              'Luca': 'Kateri',
              'Ben': ['Charlotte', 'Ash'],
              'Elliot': ['Sarah', 'Atza'],
              'Whitney': ['Jordan', 'Ernest'],
              'Charlotte': ['Ben', 'Caitlin'],
              'Shervin': ['Caitlin', 'Michelle'],
              'Aleda': ['Brian', 'JuanPa'],
              'Jordan': ['Whitney', 'Kateri', 'Liz'],
              'Kateri': ['Luca', 'Jordan', 'Liz'],
              'Michelle': ['Scott', 'Shervin'],
              'DR': 'Tristan',
              'Ernest': ['Atza', 'Whitney'],
              'Scott': 'Michelle',
              'Brian': ['Aleda', 'Kelly'],
              'Kelly': ['Ash', 'Brian'],
              'Tristan': 'DR',
              'Ash': ['Kelly', 'Ben'],
              'Caitlin': ['Shervin', 'Charlotte']}


# Define a function to do set subtraction for lists
def setsubtract(list1, list2):
    list3 = []
    for l in list1:
        if l not in list2:
            list3.append(l)
    return list3


# Initialize dictionary for matches
matches = {}

done = False
while not done:
    for friend in friendlist:
        matchlist = list(matches.keys()) + list(matches.values())  # list of keys & values in matches so far
        if friend not in matchlist:
            exclusion_list = friendlist[friend]
            inclusion_list = setsubtract(friendlist,exclusion_list)  # list of names not in exclusion list for friend
            inclusion_list = setsubtract(inclusion_list, friend)  # inclusion list had key in it, removes
            eligible = setsubtract(inclusion_list, matchlist)    # setsubtract matchlist from inclusion list,generate list of people eligible to be randomly picked
            if len(eligible) > 0:
                choice = random.choice(eligible)
                matches[friend] = choice
            else:
                matches[friend] = 'N/A'

        #check if done, then done = true
        done = True

print(matches)
print(len(matches))
print(len(friendlist))


#
# #What to do for uneven numbers
#
# What to do when no more unique matches can be made?


