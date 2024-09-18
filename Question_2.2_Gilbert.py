#Chapter 1:Gatekeeper
print("Chapter1")
from PIL import Image
import time  # Import the time module

def generate_number():
    # Get the current time in seconds since the epoch and convert it to an integer
    current_time = int(time.time())
    
    # Generate a number based on the current time
    generated_number = (current_time % 100) + 50
    
    # If the number is even, add 10 to it
    if generated_number % 2 == 0:
        generated_number += 10
    
    return generated_number

def modify_image(input_image_path, output_image_path, n):
    # Start timing
    start_time = time.time()
    
    # Open the image
    image = Image.open(input_image_path)
    pixels = image.load()  # Load pixel data
    width, height = image.size
    
    # Create a new image with the same size and mode
    new_image = Image.new("RGB", (width, height))
    new_pixels = new_image.load()
    
    red_sum = 0  # To keep track of the sum of red pixel values

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            # Modify the pixel values
            new_r = r + n
            new_g = g + n
            new_b = b + n
            
            # Ensure pixel values stay within valid range
            new_r = min(255, max(0, new_r))
            new_g = min(255, max(0, new_g))
            new_b = min(255, max(0, new_b))
            
            # Set the new pixel values
            new_pixels[i, j] = (new_r, new_g, new_b)
            
            # Add the red value to the red_sum
            red_sum += new_r
    
    # Save the new image
    new_image.save(output_image_path)
    
    # End timing
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    return red_sum, elapsed_time

# Example usage:
generated_number = generate_number()
print("Generated number:", generated_number)

input_image_path = "chapter1.jpg"
output_image_path = "chapter1out.jpg"
red_sum, elapsed_time = modify_image(input_image_path, output_image_path, generated_number)

print("Sum of red pixel values:", red_sum)
print("Time taken to process the image:", elapsed_time, "seconds")




#Chapter 2
print("Chapter2")
def process_string(s):
    # Separate numbers and letters
    num_string = ''.join(filter(str.isdigit, s))
    letter_string = ''.join(filter(str.isalpha, s))
    
    # Convert even numbers to ASCII values
    even_numbers = [int(digit) for digit in num_string if int(digit) % 2 == 0]
    even_ascii = [ord(str(num)) for num in even_numbers]
    
    # Convert uppercase letters to ASCII values
    uppercase_letters = [ch for ch in letter_string if ch.isupper()]
    uppercase_ascii = [ord(ch) for ch in uppercase_letters]
    
    return even_ascii, uppercase_ascii

# Example usage:
s = '56aAww1984sktr235270aYmn145ss785fsq3100'
even_ascii, uppercase_ascii = process_string(s)
print("Even number ASCII values:", even_ascii)
print("Uppercase letter ASCII values:", uppercase_ascii)

#Chapter 3
print("Chapter3")
def decrypt_cipher(ciphertext, shift):
    decrypted_text = []
    for char in ciphertext:
        if 'A' <= char <= 'Z':  # Uppercase letter
            new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        elif 'a' <= char <= 'z':  # Lowercase letter
            new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            new_char = char  # Non-alphabetic characters remain unchanged
        decrypted_text.append(new_char)
    return ''.join(decrypted_text)

def find_shift(ciphertext, known_quote):
    for shift in range(26):  # There are 26 possible shifts
        decrypted_text = decrypt_cipher(ciphertext, shift)
        if decrypted_text == known_quote:
            return shift
    return None

# Example usage:
ciphertext = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NE URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"
known_quote = "THE EXAMPLE OF DECRYPTED TEXT IS HERE"  # Replace with the known decrypted quote

shift = find_shift(ciphertext, known_quote)
print("Shift value that gives the original quote:", shift)
