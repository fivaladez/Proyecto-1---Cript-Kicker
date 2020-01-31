import unittest
import crypt_kicker as CK


class TestCriptKicker(unittest.TestCase):

    def test_CK(self):
        ck = CK.CriptKicker()
        self.assertEqual(ck.decrypt("sj rtsj iduft jit"), "rtsj iduft")
        self.assertEqual(ck.decrypt("sj rtsj iduftt jit"), "NO SE ENCONTRO SOLUCION")
        self.assertEqual(ck.decrypt("sj rtsjw iduft jit"), "NO SE ENCONTRO SOLUCION")
        self.assertEqual(ck.decrypt("rtsj iduft jit"), "rtsj iduft")  # Al inicio
        self.assertEqual(ck.decrypt("sj rtsj iduft"), "rtsj iduft")  # Al final
        self.assertEqual(ck.decrypt(" rtsj iduft jit"), "rtsj iduft")  # Al inicio con un espacio
        self.assertEqual(ck.decrypt("sj rtsj iduft "), "rtsj iduft")  # Al final con un espacio
