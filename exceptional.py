Digit_map = {
    "zero"  :   '0',
    "one"   :   '1',
    "two"   :   '2',
    "three" :   '3',
    "four"  :   '4',
    "five"  :   '5'
}


def convert(s):
    try:
        number= ""
        for token in s:
            number+= Digit_map[token]
        x = int(number)
        print(f"converson succeeded! x = {x}")
    except KeyError:
        print(f"Conversion failed!")
        x= -1s
    except TypeError:
        print("Please! Enter a string")
    return x