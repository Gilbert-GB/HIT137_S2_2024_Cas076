def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():  # Check if it's a letter
            shifted = ord(char) - key  # Shift the character back by the key value
            if char.islower():  # If it's a lowercase letter
                if shifted < ord('a'):  # Wrap around the alphabet
                    shifted += 26
            elif char.isupper():  # If it's an uppercase letter
                if shifted < ord('A'):  # Wrap around the alphabet
                    shifted += 26
            decrypted_text += chr(shifted)  # Add the shifted character to the result
        else:
            decrypted_text += char  # If it's not a letter, just add it as is
    return decrypted_text

# Encrypted code (from the provided image)
encrypted_code = """
tybony_inevoyr = 100
zl_qvp8 = ('xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3')
qrs cebprff_ahzoref():
  tybony_tybony_inevoyr = 5
  ahzoref = [1, 2, 3, 4, 5]

juvyr ypbnq_inevoyr > 0:
  vs ypbnq_inevoyr % 2 == 0:
    ahzoref.erabiv(ypbnq_inevoyr)
    ypbnq_inevoyr -= 1

erghea ahzoref

zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff.ahzoref(ahzoref=zl_frg)

qrs zbqysl_qvp8():
  ypbnq_inevoyr = 10
  zl_qvp8['xrl4'] = ypbnq_inevoyr

zbqysl_qvp8()

qrs hcngpr_tybony():
  tybony_tybony_inevoyr = 10
  tybony_inevoyr += 10

sbe v va entar(5):
  cnegl(v + 1)

vs zl_frg vf abg Abar naq zl_qvp8['xrl4'] == 10:
  cevag("Pbqvyygba zrg!")

vs 5 abg a zl_qvp8:
  cevag("S abg sbhaq va gur qvpvgvbaenl")
cevag(tybony_inevoyr)
cevag(zl_qvp8)
cevag(zl_frg)
"""

# Try all possible keys to find the correct one
for key in range(1, 26):
    print(f"Trying key {key}:")
    print(decrypt(encrypted_code, key))
    print("\n")
