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
        print("homophonic substitution encrypt")

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