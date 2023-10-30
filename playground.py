def translate(e_word: str, only_vowels: bool = True):
    if e_word.isalpha() is False:
        return e_word

    original_word = e_word
    result = e_word.lower()
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']


    #6th rule - check if it has only vowel
    for str in result:
        if str not in vowel_list:
            only_vowels = False
            break

    #6th
    if only_vowels:
        result = result + "yay"
        if original_word[0].isupper():
            result = result.capitalize()
        return result

    if e_word[0] in vowel_list:
        result = result + 'ay'
        if original_word[0].isupper():
            result = result.capitalize()
        return result

    if result[0] not in vowel_list:
        for str in result:
            if str not in vowel_list:
                result = result[1:] + result [0]
            else:
                break
        result = result + "ay"
        if original_word[0].isupper():
            result = result.capitalize()
        return result


    return result


e_word = "No persons under 14 admitted"
final_result = ""
list_with_words = e_word.split(" ")
list_with_translated_words = []
for word in list_with_words:
    list_with_translated_words.append(translate(word))

print(''.join(e + " " for e in list_with_translated_words).strip())


# --> Stop
# Opstay
# --> No littering
# Onay itteringlay
# --> No shirts, no shoes, no service
# Onay irtsshay, onay eosshay, onay ervicesay
# --> No persons under 14 admitted
# Onay ersonspay underay 14 admitteday
# --> Hey buddy, get away from my car!
# Eyhay uddybah, etgay awayay omfray ymay arcay!