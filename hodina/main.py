def string(str):
    str1 = ""
    for i in str:
        str1 = i + str1
    return str1


def JeToPalindrom(slovo):
    otoceneslovo = slovo[::-1]
    if otoceneslovo == slovo:
        print("slovo je palindrom")
    else:
        print("slovo nie je palindrom")


JeToPalindrom("oko")
JeToPalindrom("sova")
JeToPalindrom("vlk")
JeToPalindrom("radar")


