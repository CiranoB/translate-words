vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']
punctuation_list = [",", ".", ":", ";", "!", "?"]


# 6th rule
def translate_case_only_vowels(input: str) -> str:
    result = input + "yay"
    return result


def translate_case_first_letter_is_vowel(input: str) -> str:
    result = input + 'ay'
    return result


def translate_case_first_letter_isn_t_vowel(input: str) -> str:
    for str in input:
        if str not in vowel_list:
            input = input[1:] + input[0]
        else:
            break
    result = input + "ay"
    return result


def translate(e_word: str, only_vowels: bool = True):
    # 2nd rule
    punctuation = ""
    if e_word[-1] in punctuation_list:
        punctuation = e_word[-1]
        e_word = e_word[:-1]

    # 1st rule
    if e_word.isalpha() is False:
        return e_word
    original_word = e_word
    result = e_word.lower()

    for str in result:
        if str not in vowel_list:
            only_vowels = False
            break

    # 4th, 5th and 6th rules:
    if only_vowels:
        result = translate_case_only_vowels(result)

    if e_word[0] in vowel_list:
        result = translate_case_first_letter_is_vowel(result)

    if result[0] not in vowel_list:
        result = translate_case_first_letter_isn_t_vowel(result)

    # 3rd rule
    if original_word[0].isupper():
        result = result.capitalize()

    result = result + punctuation
    return result


def translate_phrases(input: str) -> str:
    list_with_words = input.split(" ")
    list_with_translated_words = []
    for word in list_with_words:
        list_with_translated_words.append(translate(word))

    return ''.join(e + " " for e in list_with_translated_words)[:-1]


dict_english_to_new_language = {"Stop": "Opstay",
                                "No littering": "Onay itteringlay",
                                "No shirts, no shoes, no service": "Onay irtsshay, onay oesshay, onay ervicesay",
                                "No persons under 14 admitted": "Onay ersonspay underay 14 admitteday",
                                "Hey buddy, get away from my car!": "Eyhay uddybay, etgay awayay omfray ymay arcay!"}

for english_phrases in dict_english_to_new_language.keys():
    if translate_phrases(english_phrases) == dict_english_to_new_language[english_phrases]:
        print("Test success!")
    else:
        print(translate_phrases(english_phrases) + "!=" + dict_english_to_new_language[english_phrases])
        print("Test failed!")
