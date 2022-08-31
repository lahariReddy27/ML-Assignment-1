# “I am a teacher and I love to inspire and teach people”
# • How many unique words have been used in the sentence? Use the split methods and set
# to get the unique words.

sentence = "I am a teacher and I love to inspire and teach people".split(" ")
set_sentence = set()
for elem in sentence:
    if elem not in set_sentence:
        set_sentence.add(elem)
    elif elem in set_sentence:
        set_sentence.remove(elem)

print(f'number of unique items in set: {len(set_sentence)}')