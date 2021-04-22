# cities = ["a", "b", "c", "d", "e"]
# with open("write-to-file.txt", "w") as city_file:
#     for city in cities:
#         print(city, file=city_file, flush=True)

# cities = []
# with open("write-to-file.txt", "r") as city_file:
#     for city in city_file:
#         #when written to file it appends \n in end of line/beginning.
#         #strip wont remove character from between the words
#         #Strip can do partial match of characters from the word and remove those
#         #To remove the \n from each will use strip()
#         cities.append(city.strip('\n'))


# print(cities)
# for city in cities:
#     print(city)

# imelda = "More Mayhem", "Idelda May", "2011", (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Meyhem"), (4, "Kentish Town Waltz")
# )

# with open("imelda.txt", "w") as imelda_file:
#     print(imelda, file=imelda_file)

with open("imelda.txt", "r") as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents)

print(imelda)
title, artist, year, track = imelda
print(title)
print(artist)
print(year)
print(track)

