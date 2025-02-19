#!/usr/bin/env python
# guess = input("Gissa flaggan! ")
# guess = [x for x in guess]


def format(lst):
    if (
        lst[0] == "f"
        and lst[1] == "r"
        and lst[2] == "o"
        and lst[3] == "{"
        and lst[len(lst) - 1] == "}"
    ):
        return True
    else:
        return False


# def check(lst):
def check():
    var1 = [
        79,
        91,
        70,
        82,
        95,
        72,
        91,
        118,
        77,
        76,
        93,
        118,
        76,
        71,
        66,
        76,
        69,
        118,
        66,
        70,
        77,
        22,
        84,
    ]
    # if len(lst) != len(var1):
    #     return False
    # lst2 = []
    # for i in lst:
    #     lst2.append(ord(i) ^ 41)
    # if lst2 == var1:
    #     return True
    # else:
    #     return False

    ### This line basically does the opposite of what the for loop above does, so it returns the flag
    return "".join([chr(i ^ 41) for i in var1])


# if len(guess) < 5:
#     print("För kort")
# elif format(guess) == False:
#     print("Fel format")
# elif check(guess) == True:
#     print("Bra jobbat, du hittade rätt flagga!")
# else:
#     print("Fel flagga")
print(check())
