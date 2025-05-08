"""Encryption Message"""


class CeasarCipher:

    @staticmethod
    def encrypt(shift, message):
        ency_list = []
        for char in message:
            if char.isalpha():
                base = ord("A") if char.isupper() else ord("a")
                shifted = (ord(char) - base + shift) % 26 + base
                ency_list.append(chr(shifted))
            else:
                # Leave spaces and punctuation unchanged
                ency_list.append(char)

        return "".join(ency_list)

    @staticmethod
    def decrypt(shift, message):
        decy_list = []
        for char in message:
            if char.isalpha():
                base = ord("A") if char.isupper() else ord("a")
                shifted = (ord(char) - base - shift) % 26 + base
                decy_list.append(chr(shifted))
            else:
                decy_list.append(char)

        return "".join(decy_list)


encrypt_message = CeasarCipher.encrypt(8, "This is test message")
print(encrypt_message)
decrypt_message = CeasarCipher.decrypt(8, encrypt_message)
print(decrypt_message)
