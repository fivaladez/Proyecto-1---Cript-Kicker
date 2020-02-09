"""Proyecto #01 de la materia de Algoritmos"""


class CryptKicker():
    """Clase encargada de proporcionar metodos para desencriptar un codigo."""

    def __init__(self):
        """"""
        self.key = "El veloz murciélago hindú comía feliz cardillo y kiwi cuando la cigüeña tocaba el saxofón detrás del palenque de paja"
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
            return None
        match_characters = {k: v for k, v in zip(msg, self.key)}

        return match_characters

    def __replace_chars(self, msg, match_characters):
        """
        Replace characters from message with found in dictionary(match_characters).
        It substitute one at the time, to avoid substitute a valid character.

        param msg: String with the characters to Replace
        param match_characters: Dictionary with keys found from self.key and with its real value

        return: None for error, String with the values of dictionary insted of keys
        """
        if isinstance(match_characters, dict) is False:
            return None

        msg_decrypted = msg[:]
        tem_msg = list()
        for char in msg_decrypted:
            if char in match_characters.keys():
                tem_msg.append(match_characters[char])
            else:
                tem_msg.append(char)
        msg_decrypted = "".join(tem_msg)

        return msg_decrypted

    def decrypt(self, msg):
        """
        Method to discover the meaning of an encrypted message.

        :param msg: String with the encrypted message
        :return: Return 'NO SE ENCONTRO SOLUCION' on failure.
                 Return string with the decrypted message on success.
                 Return None on invalid message
        """
        if isinstance(msg, str) is False:
            return None

        # Get piece of msg that represents the key
        msg_key = self.__look_for_key(msg)
        if msg_key is None:
            return "NO SE ENCONTRO SOLUCION"
        print("\n - Message key: {}".format(msg_key))
        print(" - Message key: {}\n".format(self.key))

        # Get dictionary with meaning of crypted characters
        match_characters = self.__match_characters(msg_key)
        if match_characters is None:
            return "NO SE ENCONTRO SOLUCION"
        print("\n - Dictionary: {}".format(match_characters))

        # Remove msg_key and white spaces
        msg = msg.replace(msg_key, "")
        msg = msg.replace("  ", " ")
        msg = msg.strip()

        # Substitute characters in messages based on dictionary
        msg_decrypted = self.__replace_chars(msg, match_characters)
        if msg_decrypted is None:
            return "NO SE ENCONTRO SOLUCION"
        print("\n - Message decrypted: {}\n\n".format(msg_decrypted))
        return msg_decrypted


if __name__ == "__main__":
    CK = CryptKicker()
    cases = int(input())
    for n in range(cases):
        paragraph, continue_cycle, msg_saved = list(), True, False
        while continue_cycle:
            line = input()
            if line != "":  # Ignore empty lines
                paragraph.append(line)
                msg_saved = True
            elif msg_saved:
                continue_cycle = False
        msg = " ".join(paragraph)
        CK.decrypt(msg)
