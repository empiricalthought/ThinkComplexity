import string

def alphanumeric_identifiers():
    number = 1
    while True:
        for c in string.ascii_lowercase:
            yield c + str(number)
        number = number + 1

            
