from lib2to3.pgen2.token import NUMBER
import random


class encryption_type:
    SPACE = 999999999
    UPPER_CASE = {
    'A': [5, 10, 15, 20],
    'B': [300, 400, 30],
    'C': [8, 9, 12],
    'D': [14, 16, 18],  # Modified to ensure distinct numbers
    'E': [21, 25, 28, 30],  # Modified to ensure distinct numbers
    'F': [35, 40],
    'G': [42, 45],
    'H': [50, 55],
    'I': [58, 60],
    'J': [65],
    'K': [70],
    'L': [75],
    'M': [78, 80],
    'N': [85, 90],
    'O': [95, 100, 105],  # Modified to ensure distinct numbers
    'P': [110, 115, 120],  # Modified to ensure distinct numbers
    'Q': [125, 130, 135],  # Modified to ensure distinct numbers
    'R': [140, 145],
    'S': [150, 155],
    'T': [160, 165, 170],  # Modified to ensure distinct numbers
    'U': [175, 180],
    'V': [185, 190],
    'W': [195, 200],
    'X': [205, 210],
    'Y': [215, 220, 225],  # Modified to ensure distinct numbers
    'Z': [230, 235, 240],  # Modified to ensure distinct numbers
}

    LOWER_CASE = {
    'a': [2, 7, 11],  # Modified to ensure distinct numbers
    'b': [15, 19, 23],  # Modified to ensure distinct numbers
    'c': [28, 33],  # Modified to ensure distinct numbers
    'd': [38, 43, 48],  # Modified to ensure distinct numbers
    'e': [53, 58, 63, 68],  # Modified to ensure distinct numbers
    'f': [73, 78],
    'g': [83, 88],
    'h': [93, 98],
    'i': [103, 108],
    'j': [113],
    'k': [118],
    'l': [123],
    'm': [128, 133],
    'n': [138, 143],
    'o': [148, 153, 158],  # Modified to ensure distinct numbers
    'p': [163, 168, 173],  # Modified to ensure distinct numbers
    'q': [178, 183, 188],  # Modified to ensure distinct numbers
    'r': [193, 198],
    's': [203, 208],
    't': [213, 218, 223],  # Modified to ensure distinct numbers
    'u': [228, 233],
    'v': [238, 243],
    'w': [248, 253],
    'x': [258, 263],
    'y': [268, 273, 278],  # Modified to ensure distinct numbers
    'z': [283, 288, 293],  # Modified to ensure distinct numbers
}

    NUMBERS = {
    0: [0, 13, 26],  # Modified to ensure distinct numbers
    1: [111, 222, 333],  # Modified to ensure distinct numbers
    2: [555, 777, 999],  # Modified to ensure distinct numbers
    3: [1515, 2020, 2525],  # Modified to ensure distinct numbers
    4: [3030, 4040, 5050],  # Modified to ensure distinct numbers
    5: [6060, 8080, 10100],  # Modified to ensure distinct numbers
    6: [12000, 15000, 18000],
    7: [20000, 25000, 30000],
    8: [35000, 40000, 45000],
    9: [50000, 55000, 60000]
}
    def basic_caesar_encrypt(self):
        filepath = input("This is the basic Caesar encryption. Please enter the file path of the message you want to encrypt: ")
        shift = 3
        try:
            with open(filepath, 'r') as file:
                # Read the entire content of the file
                text = file.read()
                
                result = ""
                
                # Iterate through each character in the text
                for char in text:
         
                    if char.isalpha():
                        # Check if the character is uppercase
                        if char.isupper():
                            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                        else:
                            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                        result += encrypted_char
                    else:
                        result += char
                print("This is the encrypted message: ")
                print(result + "\n")
        except FileNotFoundError:
            print(f"The file '{filepath}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


    def basic_caeser_decrypt(self):
        filepath = input("This is the basic Caesar decryption. Please enter the file path of the message you want to decrypt: ")
        shift = 3
        try:
            with open(filepath, 'r') as file:
                # Read the entire content of the file
                text = file.read()

                result = ""

                # Iterate through each character in the text
                for char in text:
              
                    if char.isalpha():
                        # Check if the character is uppercase
                        if char.isupper():
                            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                        else:
                            decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                        result += decrypted_char
                    else:
                        result += char
                print("This is the decrypted message: ")
                print(result + "\n")
        except FileNotFoundError:
            print(f"The file '{filepath}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
            
    def adv_caeser_encrypt(self):
        filepath = input("This is the advanced Caesar encryption. Please enter the file path of the message you want to encrypt: ")
        while True:
            shift = input("Please enter the shifting value: ")
            if shift.isdigit() and int(shift) > 0:
                break
            else:
                print("Please enter an integer greater than zero")  
        shift = int(shift)  
        try:
            with open(filepath, 'r') as file:
                # Read the entire content of the file
                text = file.read()
                
                result = ""
                
                # Iterate through each character in the text
                for char in text:
         
                    if char.isalpha():
                        # Check if the character is uppercase
                        if char.isupper():
                            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                        else:
                            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                        result += encrypted_char
                    else:
                        result += char
                print("This is the encrypted message: ")
                print(result + "\n")
        except FileNotFoundError:
            print(f"The file '{filepath}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


    def adv_caeser_decrypt(self):
        filepath = input("This is the advanced Caesar decryption. Please enter the file path of the message you want to decrypt: ")
        while True:
            shift = input("Please enter the shifting value: ")
            if shift.isdigit() and int(shift) > 0:
                break
            else:
                print("Please enter an integer greater than zero")  
        shift = int(shift)  
        try:
            with open(filepath, 'r') as file:
                # Read the entire content of the file
                text = file.read()
                
                result = ""
                
                # Iterate through each character in the text
                for char in text:
         
                    if char.isalpha():
                        # Check if the character is uppercase
                        if char.isupper():
                            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                        else:
                            decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                        result += decrypted_char
                    else:
                        result += char
                print("This is the decrypted message: ")
                print(result + "\n")
        except FileNotFoundError:
            print(f"The file '{filepath}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    

    def monoalphabetic(self, filepath: str):
        ALPHA_KEY = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
        ALPHA_UPPER_KEY = ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']

        try:
            with open(filepath, 'r') as file:
                # Read the entire content of the file
                text = file.read()
                
                result = ""
                
                # Iterate through each character in the text
                for char in text:
         
                    if char.isalpha():
                        # Check if the character is uppercase
                        if char.isupper():
                            encrypted_char = ALPHA_UPPER_KEY[ord(char) - ord('A')]
                            
                        else:
                            encrypted_char = ALPHA_KEY[ord(char) - ord('a')]
                            
                        result += encrypted_char
                    else:
                        result += char
                print("This is the decrypted message: ")
                print(result + "\n")
        except FileNotFoundError:
            print(f"The file '{filepath}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def monoalphabetic_encrypt(self):
        filepath = input("This is the monoalphabetic encryption. Please enter the file path of the message you want to encrypt: ")
        self.monoalphabetic(filepath)
    
    def monoalphabetic_decrypt(self):
        filepath = input("This is the monoalphabetic decryption. Please enter the file path of the message you want to decrypt: ")
        self.monoalphabetic(filepath)


    def homophonic_substitution_encrypt(self):
        

        filepath = input("This is the homophonic substitution encryption. Please enter the file path of the message you want to encrypt: ")
        
        try:
            with open(filepath, 'r') as file:
                text = file.read()
                result = ""
                    
                for char in text:      
                    if char.isspace():
                        result += str(self.SPACE)   
                    if char.isalpha():
                        key = char
                        if key in self.UPPER_CASE:
                            random_number = random.choice(self.UPPER_CASE[key])
                        elif key in self.LOWER_CASE:
                            random_number = random.choice(self.LOWER_CASE[key])
                        result += str(random_number)
                            
                    if char.isdigit():
                        key = char
                        if key in self.NUMBERS:
                            random_number = random.choice(self.NUMBERS[key])
                        result += str(random_number)
                    else:
                        result += char
                    result += " "
                    print(result)
                print("This is the encrypted message: ")
                print(result + "\n")
        except FileNotFoundError:
            print(f"The file '{filepath}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

        


    def create_reverse_lookup(self, hashset):
        reverse_lookup = {}
        for key, numbers_list in hashset.items():
            for number in numbers_list:
                reverse_lookup[number] = key
        return reverse_lookup
    
    def homophonic_substitution_decrypt(self):
        UPPER_CASE_REVERSED = self.create_reverse_lookup(self.UPPER_CASE)
        LOWER_CASE_REVERSED = self.create_reverse_lookup(self.LOWER_CASE)
        NUMBERS_REVERSED = self.create_reverse_lookup(self.NUMBERS)
        filepath = input("This is the homophonic substitution decryption. Please enter the file path of the message you want to decrypt: ")

        try:
            with open(filepath, 'r') as file:
                result = ""
                for line in file:
                    words = line.split()
                    for word in words:
                        if word.isdigit():
                            key = int(word)
                            
                            msg = ""
                            if key == self.SPACE:
                                result += " "
                            elif key in NUMBERS_REVERSED:
                                msg = NUMBERS_REVERSED[key]
                            elif key in LOWER_CASE_REVERSED:
                                msg = LOWER_CASE_REVERSED[key]
                            elif key in UPPER_CASE_REVERSED:
                                msg = UPPER_CASE_REVERSED[key]
                            result += str(msg)
                        else:
                            result += word
                        
                    # Add newline character after processing each line
                    result += "\n"

                print("This is the decrypted message: ")
                print(result)
        except FileNotFoundError:
            print(f"The file '{filepath}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


    def polygram_substitution_encrypt(self):
        print("polygram substitution encrypt")

    def polygram_substitution_decrypt(self):
        print("polygram substitution decrypt")

    def polyalphabetic_substitution_encrypt(self):
        print("polyalphabetic substitution encrypt")

    def polyalphabetic_substitution_decrypt(self):
        print("polyalphabetic substitution decrypt")

    def playfair_encrypt(self):
        print("playfair encrypt")

    def playfair_decrypt(self):
        print("playfair decrypt")

    def hill_encrypt(self):
        print("hill encrypt")

    def hill_decrypt(self):
        print("hill decrypt")