book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
for words in book_title:
    word_counter[words] = word_counter.get(words, 0) + 1
print(word_counter)


words = ("will only give you access to the keys in the dictionary - which is what you'd want in some situations. In other cases, you'd want to iterate through both the keys and values in the dictionary. Let's see how this is done in an example. Consider this dictionary that uses names of actors as keys and their characters as values.")
now = words.split()
counter = {}
for word in now:
    counter[word] = counter.get(word, 0) + 1
print(counter)
cont = {}
for word in now:
    if word not in cont:
        cont[word] = 1
    else:
        cont[word] += 1
print(cont)
