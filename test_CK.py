import unittest
import Crypt_Kicker as CK


class TestCriptKicker(unittest.TestCase):

    def test_CK(self):
        ck = CK.CriptKicker()
        self.assertEqual(ck.decrypt("sj rtsj iduft jit"), "la amo")
        self.assertEqual(ck.decrypt("sj rtsj iduftt jit"), "NO SE ENCONTRO SOLUCION")
        self.assertEqual(ck.decrypt("sj rtsjw iduft jit"), "NO SE ENCONTRO SOLUCION")
        self.assertEqual(ck.decrypt("rtsj iduft jit"), "amo")  # Al inicio
        self.assertEqual(ck.decrypt("sj rtsj iduft"), "la")  # Al final
        self.assertEqual(ck.decrypt(" rtsj iduft jit"), "amo")  # Al inicio con un espacio
        self.assertEqual(ck.decrypt("sj rtsj iduft "), "la")  # Al final con un espacio
        self.assertEqual(ck.decrypt(2), None)
        self.assertEqual(ck.decrypt("123456789123456789"), "NO SE ENCONTRO SOLUCION")
