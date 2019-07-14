quote = "some people drink from the fountain of knowledge, others just gargle."
VOWELS = "aeiou"

def vowels_position(stringi,vowels):
    list_position=[c for c, value in enumerate(stringi) if value in vowels]
    return(list_position)

print (vowels_position(quote, VOWELS))