str = 'My name is  Naiera'

def reversestring(str):
    length = len(str)
    list = []
    tempstr = ''

    if length > 0:
        for char in str:
            if char != " ":
                tempstr += char
            else:
                if len(tempstr) > 0:
                    list.append(tempstr)
                    tempstr= ''
                list.append(" ")

        if len(tempstr) > 0:
            list.append(tempstr)

    revstr = ''.join(list[::-1])
    return revstr

str = 'My name is  Naiera'
print(reversestring(str))
