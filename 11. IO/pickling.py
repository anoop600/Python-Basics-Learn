import pickle

#Pickle -> JAVA Serialisation
#Dump data into file
imelda = "More Mayhem", "Idelda May", "2011", (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Meyhem"), (4, "Kentish Town Waltz")
)
print(imelda)
# with open("imelda.pickle", "wb") as pickle_file:
#     pickle.dump(imelda, pickle_file)

with open("imelda.pickle", "rb") as pickle_file:
    imelda2 = pickle.load(pickle_file)

print(imelda2)
title, artist, year, track = imelda2
print(title)
print(artist)
print(year)
print(track)