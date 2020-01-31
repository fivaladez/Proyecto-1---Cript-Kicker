"""Proyecto #01 de la materia de Algoritmos"""


class CriptKicker():
    """Clase encargada de proporcionar metodos para desencriptar un codigo."""

    def __init__(self):
        """"""
        # self.__key = "El veloz murciélago hindú comía feliz cardillo y kiwi cuando la cigüeña tocaba el saxofón detrás del palenque de paja"
        self.__key = "Hola mundo"  # sj rtsj iduft jit - la amo
        self.__key_length = len(self.__key)

    def __del__(self):
        """"""
        pass

    def validate_text(self, text):
        """Validate character by character that the text can be the key (self.__key)

            :param text: String of the same size that key where to compare characters
            :return: Return False in case of failure.
                     Return True in case of success."""
        position = 0
        while position < self.__key_length:
            # Compare character by character to identify y the length of the words is the same
            if text[position].isalpha() == self.__key[position].isalpha():
                position += 1
            else:  # If one character is different, the text is discarted as a possible key
                return False

        return True

    def look_for_key(self, msg=""):
        """Loof for a specific string that is equivalent to the key to decrypt (self.__key).

            :param msg: String with the message where to look for.
            :return: Return 'NO SE ENCONTRO SOLUCION' on failure.
                     Return a string with the equivalent key in message"""
        length_msg = len(msg)
        position = 0
        while position + self.__key_length <= length_msg:
            key = msg[position: position + self.__key_length]  # Check strings of the same size
            if self.validate_text(key):
                if position + self.__key_length < length_msg:  # Can exist the next character?
                    next_char = msg[position + self.__key_length]
                    before_char = ""
                    if position - 1 >= 0:  # Check if there is a before character
                        before_char = msg[position - 1]
                    if next_char == " " and before_char == "":
                        # You are at the begining of the message
                        return key
                    elif next_char == " " and before_char == " ":
                        # You are somewhere in the midle of message
                        return key
                else:  # You are at the end of the message
                    before_char = ""
                    if position - 1 >= 0:  # Check if there is a before character
                        before_char = msg[position - 1]
                    if before_char == " " or before_char == "":  # Valid message
                        return key
            position += 1

        return "NO SE ENCONTRO SOLUCION"

    def decrypt(self, msg="sj rtsj iduft jit"):  # rtsj iduft = hola mundo
        """Method to discover real meaning of an encrypted message.

            :param msg: String with the encrypted message
            :return: Return 'NO SE ENCONTRO SOLUCION' on failure.
                     Return string with the decrypted message on success.
        """
        decrypted_message = self.look_for_key(msg)
        # Or return "NO SE ENCONTRO SOLUCIÓN"
        return decrypted_message


if __name__ == "__main__":
    CK = CriptKicker()
    cases = int(input("Número de casos a analizar? "))
    while cases > 0:
        encrypted_message = input("Mensaje a desencriptar: ")
        if encrypted_message != "":  # Ignore empty lines
            print(CK.decrypt(encrypted_message))
            cases -= 1
