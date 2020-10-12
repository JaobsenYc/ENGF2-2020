import sys


class caesar(object):
    def break_cipher(self, text, key=None):
        plain_text = ""
        if key is None:
            key = self.break_key_letter(text)
        for letter in text:
            decrypted_letter = chr(65 + (ord(letter) - 65 - key) % 26)
            plain_text = plain_text + str(decrypted_letter)

        return (plain_text)

    def break_key_letter(self, encrypted_text):
        common_index = ord("E")
        distribution = {}
        for x in encrypted_text:
            if x in distribution:
                distribution[x] = distribution[x] + 1
            else:
                distribution[x] = 1
        max_value = max(distribution.values())
        for k, v in distribution.items():
            if v == max_value:
                key = ord(k) - common_index
        return key

    def test_key(self,text):
        rate = 0
        for word in english_words:
            if word in text:
                rate += 1
        return rate

    def break_key_word(self,text):
        distribution = {}
        for key in range(26):
            distribution[key] = self.test_key(self.break_cipher(text, key))

        max_key = max(distribution, key=distribution.get)

        return max_key


    def iterate_break(self, text):
        for key in range(26):
            print(f"For key :{key}, the plain_text is {self.break_cipher(text, key)}")

    def encrpt(self, text, key):
        plain_text = ""
        for letter in text:
            encrypted_letter = chr(65 + (ord(letter) - 65 + key) % 26)
            plain_text = plain_text + str(encrypted_letter)

        return (plain_text)


class Selections(object):

    def auto_crack_byletter(self):
        cipher_text = input("Please input the Caesar’s Cipher text:")
        caesar.iterate_break(cipher_text)
        key = caesar.break_key_letter(cipher_text)
        Decrypted=caesar.break_cipher(cipher_text)
        print(
            f"-----------------After the calculated, the most possible key for this Caesar’s Cipher is {key}-----------------")
        print("Decrypted text:\n", Decrypted)
        rate=caesar.test_key(Decrypted)
        print(f"There are {rate}/{len(english_words)} english word in the string \n")

    def auto_crack_byword(self):
        cipher_text = input("Please input the Caesar’s Cipher text:")
        caesar.iterate_break(cipher_text)
        key = caesar.break_key_word(cipher_text)
        Decrypted=caesar.break_cipher(cipher_text)
        print(
            f"-----------------After the counted, the most possible key for this Caesar’s Cipher is {key}-----------------")
        print("Decrypted text:\n", caesar.break_cipher(cipher_text))
        rate = caesar.test_key(Decrypted)
        print(f"There are {rate}/{len(english_words)} english word in the string \n")


    def test_key(self):
        text = input("Please input the text: ")
        rate = caesar.test_key(text)
        print(f"There are {rate}/{len(english_words)} english words in the string \n")

    def encrypt(self):
        cipher_text = input("Please input the plain text: ")
        key = int(input("Please input the key: "))
        encrypted_text = caesar.encrpt(cipher_text, key)
        print("Encrypted text:\n", encrypted_text)

    def decrypt(self):
        cipher_text = input("Please input the Caesar’s Cipher text:")
        key = int(input("Please input the key: "))
        print("Decrypted text:\n", caesar.break_cipher(cipher_text,key))

    def iterate_break(self):
        cipher_text = input("Please input the Caesar’s Cipher text:")
        caesar.iterate_break(cipher_text)


class Menu(object):
    def __init__(self):
        self.selection = Selections()
        self.menuChoices = {
            "1": self.selection.auto_crack_byletter,
            "2": self.selection.auto_crack_byword,
            "3": self.selection.encrypt,
            "4": self.selection.decrypt,
            "5": self.selection.test_key,
            "6": self.selection.iterate_break,
            "7": self.quit,

        }

    def display_menu(self):
        print("""
        -----------------Chen Yang Exercise 5:Breaking Caesar’s Cipher-----------------
        Operation Menu:
        1. Automatic crack the Caesar’s Cipher by letter frequency
        2. Automatic crack the Caesar’s Cipher by word frequency
        3. Encrypt by key
        4. Decrypt by key
        5. Word counting to test key
        6. Brute-force attack
        7. Quit
        ---------------------------------------------------
        """)

    def run(self):
        while True:
            self.display_menu()
            try:
                choice = input("Enter an option: ")
            except BaseException:
                print("Please input a valid option!");
                continue

            choice = str(choice).strip()
            action = self.menuChoices.get(choice)

            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def quit(self):
        print("\nThank you for using Chen Yang Breaking Caesar’s Cipher!\n")
        sys.exit(0)


if __name__ == '__main__':
    with open("TopWord.txt") as word_file:
        english_words = set(word.strip().upper() for word in word_file)
    caesar = caesar()
    Menu().run()