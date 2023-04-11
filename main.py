text_to_morse_dict = {"A": "*-",
                      "B": "-***",
                      "C": "-*-*",
                      "D": "-**",
                      "E": "*",
                      "F": "**-*",
                      "G": "--*",
                      "H": "****",
                      "I": "**",
                      "J": "*---",
                      "K": "-*-",
                      "L": "*-**",
                      "M": "--",
                      "N": "-*",
                      "O": "---",
                      "P": "*--*",
                      "Q": "--*-",
                      "R": "*-*",
                      "S": "***",
                      "T": "-",
                      "U": "**-",
                      "V": "***-",
                      "W": "*--",
                      "X": "-**-",
                      "Y": "-*--",
                      "Z": "--**",
                      "1": "*----",
                      "2": "**---",
                      "3": "***--",
                      "4": "****-",
                      "5": "*****",
                      "6": "-****",
                      "7": "--***",
                      "8": "---**",
                      "9": "----*",
                      "0": "-----",
                      "": "   ",
                      " ": "      "
                      }

morse_to_text_dict = {}

for key, value in text_to_morse_dict.items():
    morse_to_text_dict[value] = key


def text_to_morse():
    text = input("Enter Text:")
    morse_list = []
    morse = ''
    for i in text:
        if i.islower():
            i = i.upper()
        morse_list.append(text_to_morse_dict[i])
        morse_list.append(text_to_morse_dict[""])
        morse = "".join(morse_list)
    print(morse)


def morse_to_text():
    text_list = []
    morse = input("Enter Morse:")
    words_list = morse.split("            ")
    for word in words_list:
        alphabets_list = word.split("   ")
        for alphabet in alphabets_list:
            text_list.append(morse_to_text_dict[alphabet])
        text_list.append(" ")
    text = "".join(text_list)
    print(text)


text_to_morse()
morse_to_text()
