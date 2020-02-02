"""Proyecto #01 de la materia de Algoritmos"""


class CriptKicker():
    """Clase encargada de proporcionar metodos para desencriptar un codigo."""

    def __init__(self):
        """"""
        self.key = "Hola mundo"  # sj rtsj iduft jit - la amo
        self.key_length = len(self.key)

    def __del__(self):
        """"""
        pass

    def __same_characters(self, msg=""):
        """
        Compare characters to identify if msg can be the key (self.key).
        Variable 'msg' shall be of the same size of key to be compared.

        :param msg: String of the same size that key where to compare characters
        :return: Return False on failure
                 Return None on invalid message
                 Return True on success
        """
        if len(msg) == self.key_length:
            for msg_char, key_char in zip(msg, self.key):
                if msg_char.isalpha() != key_char.isalpha():
                    return False
            return True

        return None

    def __look_for_key(self, msg=""):
        """
        Loof for a specific string that is equivalent to the key (self.key).

        :param msg: String with the message where to look for.
        :return: Return None on failure.
                 Return a string with the equivalent key in message on succes.
        """
        msg_length = len(msg)
        for str_pos in range(0, msg_length):
            max_length = str_pos + self.key_length
            key = msg[str_pos: max_length]
            if self.__same_characters(key):
                # Does exist a next character?
                next_char = msg[max_length] if max_length < msg_length else ""
                # Does exist a before character?
                before_char = msg[str_pos - 1] if str_pos - 1 >= 0 else ""
                # If one or both exists, they shall be a white space ' '
                if (next_char == "" or next_char == " ") and\
                        (before_char == "" or before_char == " "):
                    return key

        return None

    def __match_characters(self, msg=""):
        """
        Compare characters from key crypted with real meaning of key (self.key) to get actual
        value of each character in the message.

        param msg_key: String with the message with you want to compare key

        return: None for error, Dictionary with matches of characters found
        """
        if len(msg) != self.key_length:
            print(len(msg), self.key_length)
            return None
        char_matches = {k: v for k, v in zip(msg, self.key)}
        if None in char_matches:
            char_matches.pop()
        for k, v in char_matches.items():
            print(k, ":", v)

        return char_matches

    def decrypt(self, msg):
        """
        Method to discover the meaning of an encrypted message.

        :param msg: String with the encrypted message
        :return: Return 'NO SE ENCONTRO SOLUCION' on failure.
                 Return string with the decrypted message on success.
                 Return None on invalid message
        """
        if isinstance(msg, str):
            msg_key = self.__look_for_key(msg)
            if msg_key is None:
                return "NO SE ENCONTRO SOLUCION"
            # return msg_key
            char_matches = self.__match_characters(msg_key)
            if char_matches is None:
                return "NO SE ENCONTRO SOLUCION"
            return char_matches

        return None


if __name__ == "__main__":
    CK = CriptKicker()
    cases = int(input("Número de casos a analizar? "))
    while cases > 0:
        encrypted_message = input("Mensaje a desencriptar: ")
        if encrypted_message != "":  # Ignore empty lines
            print(CK.decrypt(encrypted_message))
            cases -= 1
