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


def test_key(self, text):
    rate = 0
    for word in english_words:
        if word in text:
            rate += 1
    return rate


def break_key_word(self, text):
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

with open("TopWord.txt") as word_file:
    english_words = set(word.strip().upper() for word in word_file)