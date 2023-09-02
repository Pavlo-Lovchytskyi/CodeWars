# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python


def spin_words(sentence: str) -> str:
    if len(sentence.split(' ')) >= 2:  # Если длинна списка больше равно 2
        str_of_sentence = ''
        
        for char in sentence.split(' '):
            if len(char) >= 5:
                str_of_sentence += char[::-1] + ' '
            elif len(char) < 5:
                str_of_sentence += char + ' '
        return str_of_sentence.rstrip()
                
    elif len(sentence.split(' ')) == 1:  # Если длинна списка равна 1
        if len(sentence) >= 5:  # Если длинна слова больше 5
            return sentence[::-1]
        
        elif len(sentence) < 5:  # Если длинна слова меньше 5
            return sentence

    #return " ".join([words[::-1] if len(words) >= 5 else words for words in sentence.split(" ")])
print(spin_words('words Write one only like Kata letter or Strings when be word more Just'))

