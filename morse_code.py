MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }

def morse_decoder(code:str):
    decoder = ""
    words = code.split(" ")
    for index, symb in enumerate(words):
        for key in MORSE:
            if symb == key:
                decoder += words[index].replace(symb, MORSE[key])
        if symb == "" and words[index + 1] == "":
            decoder += " "
    return decoder.capitalize()

# morse_decoder = lambda code: "".join([MORSE[i] for i in code.replace("   ", " + ").split()]).capitalize()

