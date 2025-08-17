def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Checking the first three mandatory requirements| 1 - length | 2 - first two characters are letters | 3 - All characters are letters or numbers.
    if 2 <= len(s) <= 6 and s[:2].isalpha():
        if s[:].isalnum():

            # loop to check for numbers and ensuring there is no letter after a number.
            num_list = []
            for char in s[:]:
                if char.isdigit():
                    num_list.append(char)
                    try:
                        if s[s.index(char) + 1].isalpha():
                            return False
                    except IndexError:
                        continue
            if len(num_list) > 0:
                if num_list[0] == "0":
                    return False
            return True

        else:
            return False

    else:
        return False


main()
