import unittest
from vigenereCipherer import vigenereCipherer


class TestClass(unittest.TestCase):
    def test_encryption(self):
        message = "superduper"
        key = "xyzzy"
        encoder_decoder = vigenereCipherer(message, key)

        self.assertEqual(
            encoder_decoder.encode_message(),
            "qtpeqbtpeq",
            f"Encrypted message shown is {encoder_decoder.encode_message()}",
        )


if __name__ == "__main__":
    unittest.main()
