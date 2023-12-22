class encryption_type:
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
        

        UPPER_CASE = {
    'A': [5, 10, 15, 20],
    'B': [300, 400, 30],
    'C': [8, 9],
    'D': [12, 14, 16],
    'E': [18, 21, 25, 28],
    'F': [30, 35],
    'G': [40, 42],
    'H': [45, 50],
    'I': [55, 58],
    'J': [60],
    'K': [65],
    'L': [70],
    'M': [75, 78],
    'N': [80, 85],
    'O': [90, 95, 100],
    'P': [105, 110, 115],
    'Q': [120, 125, 130],
    'R': [135, 140],
    'S': [145, 150],
    'T': [155, 160, 165],
    'U': [170, 175],
    'V': [180, 185],
    'W': [190, 195],
    'X': [200, 205],
    'Y': [210, 215, 220],
    'Z': [225, 230, 235]
}
    LOWER_CASE = {
    'a': [2, 5, 8],
    'b': [15, 20, 25],
    'c': [30, 35],
    'd': [40, 45, 50],
    'e': [55, 60, 65, 70],
    'f': [75, 80],
    'g': [85, 90],
    'h': [95, 100],
    'i': [105, 110],
    'j': [115],
    'k': [120],
    'l': [125],
    'm': [130, 135],
    'n': [140, 145],
    'o': [150, 155, 160],
    'p': [165, 170, 175],
    'q': [180, 185, 190],
    'r': [195, 200],
    's': [205, 210],
    't': [215, 220, 225],
    'u': [230, 235],
    'v': [240, 245],
    'w': [250, 255],
    'x': [260, 265],
    'y': [270, 275, 280],
    'z': [285, 290, 295]
}
    NUMBERS = {
    0: [0, 10, 20],
    1: [100, 200, 300],
    2: [500, 750, 1000],
    3: [1500, 2000, 2500],
    4: [3000, 4000, 5000],
    5: [6000, 8000, 10000],
    6: [12000, 15000, 18000],
    7: [20000, 25000, 30000],
    8: [35000, 40000, 45000],
    9: [50000, 55000, 60000]
}
    
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


        

    def homophonic_substitution_decrypt(self):
        print("homophonic substitution decrypt")

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