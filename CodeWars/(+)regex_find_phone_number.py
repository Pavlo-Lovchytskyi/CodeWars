import re


def find_all_phones(text):
    spisok = []
    result = re.findall(r"[+][()0-9]{3,11}[-][0-9]{1,2}[-][0-9]{2,3}", text)
    for i in result:
        if len(i) == 18:
            i = i[:-1]
            result[-1] = i
            return result
    return result


print(find_all_phones('Irma +380(50)111-7-771 second +380(50-)777-77-77 aloha a@test.com abc111@test.com.net +380(67)777-777-77-7+380(50)777-77-787'))
