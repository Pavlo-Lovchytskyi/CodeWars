import re


def replace_spam_words(text, spam_words):

    for i in spam_words:
        words = re.findall(i, text, re.IGNORECASE)

        if len(words) == 0:
            continue
        text = re.sub('|'.join(words), '*'*len(i), text)

    return text


print(replace_spam_words(
    'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn', ['began', 'Python']))
