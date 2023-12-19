from encryption_type import encryption_type


def homepage():
    while True:
        user_input = (input('''Hello and welcome to the cipher program. This program allows you to encrypt or decrypt any message using one of the following cipher types

1. Basic Ceaser Cipher
2. Advanced Ceaser Cipher
3. Monoalphabetic Cipher
4. Homophonic Substitution Cipher
5. Polygram Substitution Cipher
6. Polyalphabetic Substitution Cipher
7. Playfair Cipher
8. Hill Cipher

To input the message, you need to ensure the message is located in a text file.
Please select a number from 1 - 8 or press 0 to exit the program: '''))
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Please enter an integer from 0 - 8")

def get_encrypt_or_decrypt():
    while True:
        user_input = input("Press 1 to encrypt or 2 to decrypt: ")
        if user_input.isdigit() and user_input in {'1', '2'}:
            return int(user_input)
        else:
            print("Please enter either 1 or 2")


def main():
    encryption_types = encryption_type()

    hashset = {
    (1, True): encryption_types.basic_ceaser_encrypt,
    (1, False): encryption_types.basic_ceaser_decrypt,
    (2, True): encryption_types.adv_ceaser_encrypt,
    (2, False): encryption_types.adv_ceaser_decrypt,
    (3, True): encryption_types.monoalphabetic_encrypt,
    (3, False): encryption_types.monoalphabetic_decrypt,
    (4, True): encryption_types.homophonic_substitution_encrypt,
    (4, False): encryption_types.homophonic_substitution_decrypt,
    (5, True): encryption_types.polygram_substitution_encrypt,
    (5, False): encryption_types.polygram_substitution_decrypt,
    (6, True): encryption_types.polyalphabetic_substitution_encrypt,
    (6, False): encryption_types.polyalphabetic_substitution_decrypt,
    (7, True): encryption_types.playfair_encrypt,
    (7, False): encryption_types.playfair_decrypt,
    (8, True): encryption_types.hill_encrypt,
    (8, False): encryption_types.hill_decrypt,
}


    while True:
        first_user_input = homepage()
        if first_user_input == 0:
            break
        elif 0 < first_user_input <= 8:
            second_user_input = get_encrypt_or_decrypt()
            encrypt_flag = True if second_user_input == 1 else False
            key = (first_user_input, encrypt_flag)
            if key in hashset:
                hashset[key]()
            else:
                print("Key not found in hashset.")
        else:
            print("Please enter a number from 0 - 8")


if __name__ == "__main__":
    main()