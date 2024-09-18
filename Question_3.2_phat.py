# Function to decrypt the Caesar cipher
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
"""

# Decrypt the code with key 13 (as found in Question 1)
key = 13
decrypted_code = decrypt(encrypted_code, key)

# Print the decrypted code
print(decrypted_code)
