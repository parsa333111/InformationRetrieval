from re import sub
from parsivar import FindStems


def transform_space_to_half_space(string):
    find1 = r'^(می|نمی)( )'
    replace1 = r'\1‌'
    result1 = sub(find1, replace1, string)
    find2 = r'( )(می|نمی)( )'
    replace2 = r'\1\2‌'
    result2 = sub(find2, replace2, result1)
    find3 = r'( )(های|ها|هایی|ی|ای|تر|تری|ترین|گر|گری|ام|ات|اش)( )'
    replace3 = r'‌\2\3'
    result3 = sub(find3, replace3, result2)
    find4 = r'( )(شده|نشده)( )'
    replace4 = r'‌\2‌'
    result4 = sub(find4, replace4, result3)
    find5 = r'( )(می‌خواهند|نمی‌خواهند|می‌خواهید|نمی‌خواهید|می‌خواهیم|نمی‌خواهیم|می‌خواهی|نمی‌خواهی|می‌خواهد|نمی‌خواهد|می‌خواهم|نمی‌خواهم)( )'
    replace5 = r'‌\2‌'
    result5 = sub(find5, replace5, result4)

    return result5


def change_unicode(string):
    find0 = r'0'
    replace0 = r'۰'
    result0 = sub(find0, replace0, string)
    find1 = r'1'
    replace1 = r'۱'
    result1 = sub(find1, replace1, result0)
    find2 = r'2'
    replace2 = r'۲'
    result2 = sub(find2, replace2, result1)
    find3 = r'3'
    replace3 = r'۳'
    result3 = sub(find3, replace3, result2)
    find4 = r'4'
    replace4 = r'۴'
    result4 = sub(find4, replace4, result3)
    find5 = r'5'
    replace5 = r'۵'
    result5 = sub(find5, replace5, result4)
    find6 = r'6'
    replace6 = r'۶'
    result6 = sub(find6, replace6, result5)
    find7 = r'7'
    replace7 = r'۷'
    result7 = sub(find7, replace7, result6)
    find8 = r'8'
    replace8 = r'۸'
    result8 = sub(find8, replace8, result7)
    find9 = r'9'
    replace9 = r'۹'
    result9 = sub(find9, replace9, result8)
    find10 = r'ﻲ|ﯾ|ﯿ|ي'
    replace10 = r'ی'
    result10 = sub(find10, replace10, result9)
    find11 = r'ﻚ|ﮏ|ﻛ|ﮑ|ﮐ|ك'
    replace11 = r'ک'
    result11 = sub(find11, replace11, result10)
    find12 = "ء|ې|ێ"
    replace12 = "ی"
    result12 = sub(find12, replace12, result11)
    find13 = r"ٲ|ٱ|إ|ﺍ|أ|آ"
    replace13 = r"ا"
    result13 = sub(find13, replace13, result12)
    find13_2 = r'ﺆ|ۊ|ۇ|ۉ|ﻮ|ؤ'
    replace13_2 = r'و'
    result13_2 = sub(find13_2, replace13_2, result13)
    find13_3 = r'ّ'
    replace13_3 = r''
    result13_3 = sub(find13_3, replace13_3, result13_2)
    find14 = r'﷽'
    replace14 = r'بسم االله الرحمن الرحیم'
    result14 = sub(find14, replace14, result13_3)
    find15 = r'طهران'
    replace15 = r'تهران'
    result15 = sub(find15, replace15, result14)
    find16 = r'گفت‌وگو|گفت و گو|گفت‌و‌گو'
    replace16 = r'گفتگو'
    result16 = sub(find16, replace16, result15)
    find17 = r'جست‌وجو|جست و جو|جست‌و‌جو'
    replace17 = r'جستجو'
    result17 = sub(find17, replace17, result16)
    find18 = r'دشک'
    replace18 = r'تشک'
    result18 = sub(find18, replace18, result17)
    find19 = r'طوس'
    replace19 = r'توس'
    result19 = sub(find19, replace19, result18)
    find20 = r'باطری'
    replace20 = r'باتری'
    result20 = sub(find20, replace20, result19)
    find21 = r'توفان'
    replace21 = r'طوفان'
    result21 = sub(find21, replace21, result20)
    find22 = r'بلیط'
    replace22 = r'بلیت'
    result22 = sub(find22, replace22, result21)
    find23 = r'ریال'
    replace23 = r'ریال'
    result23 = sub(find23, replace23, result22)
    find24 = r'FIFA'
    replace24 = r'فیفا'
    result25 = sub(find24, replace24, result23)

    return result25


def separate_numbers(string):
    find1 = r'([0-9۰-۹]+)'
    replace1 = r' \1 '
    result1 = sub(find1, replace1, string)
    return result1


stemmer = FindStems()


def stemming(string):
    strings = string.split()
    index = 0
    for word in strings:
        strings[index] = stemmer.convert_to_stem(word)
        index += 1
    string = " ".join(strings)
    return string


bad_char = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', ',', '.',
            '?', '/', '>', '<', '،', '«', '»', '؛', '؟', '"', '!', '!', '!', '"', "'"]


def delete_negharesh(string):
    string = list(string)
    index = 0
    for char in string:
        if char in bad_char:
            string[index] = ' '
        index += 1
    string = "".join(string)

    return string


def normalizer(string):
    string = delete_negharesh(string)
    string = change_unicode(string)
    string = transform_space_to_half_space(string)
    string = separate_numbers(string)
    string = stemming(string)
    return string


def tokenizer(string):
    string = normalizer(string)
    find1 = r'\s'
    replace1 = r' '
    result1 = sub(find1, replace1, string)
    non_empty_token = [i for i in result1.split() if i != ""]
    return non_empty_token
