#imported into the main app
def capitalize(x): #Sanitizes inputs
    x=list(x)
    capitals={
        'a':'A',
        'b':'B',
        'c':'C',
        'd':'D',
        'e':'E',
        'f':'F',
        'g':'G',
        'h':'H',
        'i':'I',
        'j':'J',
        'k':'K',
        'l':'L',
        'm': 'M',
        'n': 'N',
        'o': 'O',
        'p': 'P',
        'q': 'Q',
        'r': 'R',
        's': 'S',
        't': 'T',
        'u': 'U',
        'v':'V',
        'w':'W',
        'x':'X',
        'y':'Y',
        'z':'Z'
    }
    for i in range(len(x)):
        try:
            x[i]=capitals[x[i]] #makes lowercase letters capital
        except KeyError:
            pass #passes out inputs that do not need to be sanitized
    return(x)


def encode(message): #encodes a string of normal English to morse code
  string=""
  message=(''.join(capitalize(message))) #sanitizes input
  for letter in message:
    try:
      string+=MORSE_CODE_DICT[letter]+" " #trys to translate to morse code
    except KeyError: #If it fails, pass
      pass
  return(string)

def decode(message): #decodes a string of morse code to english
  letter="" #represents one english letter
  string="" #represents the final output
  for i in range(len(message)): #for each dot or dash
    if message[i]==" ": #if there is a space, which denotes the end of a letter
      try:
        string+=rev_morse_code[letter] #translate to English
        letter="" #reset letter
      except: #if there is a problem translating (invalid character), pass
        pass
      if message[i]=="/": #if there is a slash, which denotes a space between English words
        string+=" " #insert
        letter="" #reset letter
    else:
      try:
        letter+=message[i] #else add onto the letter waiting to be translated
      except:
        pass
  try:
    string+=rev_morse_code[letter] #handles the end of the string if there are still is still an untranslated letter
  except:
    pass
  return(string) #outputs result

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-',' ':"/","'":'.----.','!':'-.-.--','"':'.-..-.','@':'.--.-.','&':'.-...'}
rev_morse_code={a:b for b,a in MORSE_CODE_DICT.items()} #reverse of the morse code dictionary for decoding
