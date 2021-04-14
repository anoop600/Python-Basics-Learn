#List all character in the input sentence which are not vowels

sample_text = "hi i am anoop"
vowels = frozenset("aeiou")

final_set = set(sample_text).difference(vowels)
print(final_set)

final_list = sorted(final_set)
print(final_list)