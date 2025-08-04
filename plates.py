def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    
    if not (2 <= len(s) <= 6):
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    num_list = []
    for i in s:
        if i.isdigit():
            num_list.append(i)

    if "0" in num_list:
        if num_list[0] == "0":
            return False
    elif not (len(num_list) == 0):
        if (s[-1].isalpha()):
            return False
        else:
            return True

        
    for i in s:
        if not (i.isalpha()):
            return False
        else:
            return True

main()
