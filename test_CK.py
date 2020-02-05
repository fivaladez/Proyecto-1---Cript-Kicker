# -*- coding: 850 -*-
import unittest
import crypt_kicker as CK


class TestCriptKicker(unittest.TestCase):

    # def test_initial(self):
    #     ck = CK.CriptKicker()
    #     self.assertEqual(ck.decrypt("sj rtsj iduft jit"), "la amo")
    #     self.assertEqual(ck.decrypt("sj rtsj iduftt jit"), "NO SE ENCONTRO SOLUCION")
    #     self.assertEqual(ck.decrypt("sj rtsjw iduft jit"), "NO SE ENCONTRO SOLUCION")
    #     self.assertEqual(ck.decrypt("rtsj iduft jit"), "amo")  # Al inicio
    #     self.assertEqual(ck.decrypt("sj rtsj iduft"), "la")  # Al final
    #     self.assertEqual(ck.decrypt(" rtsj iduft jit"), "amo")  # Al inicio con un espacio
    #     self.assertEqual(ck.decrypt("sj rtsj iduft "), "la")  # Al final con un espacio
    #     self.assertEqual(ck.decrypt(2), None)
    #     self.assertEqual(ck.decrypt("123456789123456789"), "NO SE ENCONTRO SOLUCION")

    def test_final(self):
        ck = CK.CryptKicker()
        # with open("Crypted_msg_example.txt", "r") as cmf:
        #     encrypted_msg = cmf.read()
        # with open("Decrypted_msg_example.txt", "r") as dmf:
        #     decrypted_msg = dmf.read()
        encrypted_msg = "cx kuyxnkfu úrj hcxujxqx hxlx jc qbx qj cx pdáx qj odókjlud ju hrjócx jc yjcdü árlskacxod mkuqt sdábx újckü sxlqkccd z ikík srxuqd cx skovjex pdsxóx jc nxñdúfu qjplwn qjc hxcjuérj qj hxgx qj cdn wuojcjn sdu xrpdlküxskfu qjc jgjlskpd qj cx uxskfu sdu jc úku qj ljsrhjlxl cx hcxüx qj cdn ukedn"
        decrypted_msg = "El veloz murciélago hindú comía feliz cardillo y kiwi cuando la cigüeña tocaba el saxofón detrás del palenque de paja"
        self.assertEqual(ck.decrypt(encrypted_msg), decrypted_msg)
