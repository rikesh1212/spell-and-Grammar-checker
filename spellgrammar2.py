from spellchecker import SpellChecker

spell = SpellChecker()

text = "Last but no leest; i would rather u use the best tool n customise it if that is neded"

lst = []
def convert(lst):
    return (lst[0].split())

lst.append(text)

a = convert(lst)

misspelled = spell.unknown(a)

for word in misspelled:
    print(spell.candidates(word))




