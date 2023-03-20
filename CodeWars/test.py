import re


def find_all_links(text):
    result = []
    text = text.replace(' ', '')
    print(text)
    iterator = re.finditer(
        r"(https|http)://([a-z]{3,}\.[a-z]{2,}\.[a-z]{3}|[a-z]{3,}\.[a-z]{2,})", text)
    for match in iterator:
        result.append(match.group())
    return result


print(find_all_links('The main search site in the world is https:// www.google.com The main social network for people in the world is https: // www.facebook.com Butprogrammers have their own social network http: // github.com There they share their code. some url to check https: // www..facebook.com www.facebook.com'))


# ['https://www.google.com', 'https://www.facebook.com', 'http://github.com']

#  iterator = re.finditer(r"(https|http)://[a-z]{3,}\.[a-z]{2,}", text)
