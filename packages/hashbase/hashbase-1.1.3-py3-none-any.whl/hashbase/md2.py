from typing import List


class MD2:
    def __init__(self) -> None:
        """The MD2 algorithm is a cryptographic hashing function used to produce a 128-bit hash.
        https://en.wikipedia.org/wiki/MD2
        """
        self.S: List[int] = [
            41,
            46,
            67,
            201,
            162,
            216,
            124,
            1,
            61,
            54,
            84,
            161,
            236,
            240,
            6,
            19,
            98,
            167,
            5,
            243,
            192,
            199,
            115,
            140,
            152,
            147,
            43,
            217,
            188,
            76,
            130,
            202,
            30,
            155,
            87,
            60,
            253,
            212,
            224,
            22,
            103,
            66,
            111,
            24,
            138,
            23,
            229,
            18,
            190,
            78,
            196,
            214,
            218,
            158,
            222,
            73,
            160,
            251,
            245,
            142,
            187,
            47,
            238,
            122,
            169,
            104,
            121,
            145,
            21,
            178,
            7,
            63,
            148,
            194,
            16,
            137,
            11,
            34,
            95,
            33,
            128,
            127,
            93,
            154,
            90,
            144,
            50,
            39,
            53,
            62,
            204,
            231,
            191,
            247,
            151,
            3,
            255,
            25,
            48,
            179,
            72,
            165,
            181,
            209,
            215,
            94,
            146,
            42,
            172,
            86,
            170,
            198,
            79,
            184,
            56,
            210,
            150,
            164,
            125,
            182,
            118,
            252,
            107,
            226,
            156,
            116,
            4,
            241,
            69,
            157,
            112,
            89,
            100,
            113,
            135,
            32,
            134,
            91,
            207,
            101,
            230,
            45,
            168,
            2,
            27,
            96,
            37,
            173,
            174,
            176,
            185,
            246,
            28,
            70,
            97,
            105,
            52,
            64,
            126,
            15,
            85,
            71,
            163,
            35,
            221,
            81,
            175,
            58,
            195,
            92,
            249,
            206,
            186,
            197,
            234,
            38,
            44,
            83,
            13,
            110,
            133,
            40,
            132,
            9,
            211,
            223,
            205,
            244,
            65,
            129,
            77,
            82,
            106,
            220,
            55,
            200,
            108,
            193,
            171,
            250,
            36,
            225,
            123,
            8,
            12,
            189,
            177,
            74,
            120,
            136,
            149,
            139,
            227,
            99,
            232,
            109,
            233,
            203,
            213,
            254,
            59,
            0,
            29,
            57,
            242,
            239,
            183,
            14,
            102,
            88,
            208,
            228,
            166,
            119,
            114,
            248,
            235,
            117,
            75,
            10,
            49,
            68,
            80,
            180,
            143,
            237,
            31,
            26,
            219,
            153,
            141,
            51,
            159,
            17,
            131,
            20,
        ]

    @staticmethod
    def apply_message_padding(message: str) -> List[int]:
        """Converts the input message to a List of integer values and applies padding.

        Args:
            message (str): The input message.

        Returns:
            List[int]: The padded message as a List of integers.
        """
        message_ascii = [ord(m) for m in message]
        pad_count = 16 - (len(message_ascii) % 16)
        return message_ascii + [pad_count] * pad_count

    def append_checksum(self, message: List[int]) -> List[int]:
        """Appends a 16-byte checksum to the end of the message.

        Args:
            message (List[int]): The padded message as a List of integer values.

        Returns:
            List[int]: The entire message with the appended 16-byte checksum.
        """
        checksum = [0] * 16
        l = 0
        for i in range(len(message) // 16):
            for j in range(16):
                l = self.S[(message[i * 16 + j] ^ l)] ^ checksum[j]
                checksum[j] = l
        return message + checksum

    def generate_hash(self, message: str) -> str:
        """Generates a 128-bit MD2 hash of the input message.

        Args:
            message (str): The input message/text.

        Returns:
            str: The 128-bit MD2 hash of the message.
        """
        padded_message = self.apply_message_padding(message)
        padded_message_checksum = self.append_checksum(padded_message)
        md_buffer = [0] * 48

        for i in range(len(padded_message_checksum) // 16):
            for j in range(16):
                md_buffer[16 + j] = padded_message_checksum[i * 16 + j]
                md_buffer[32 + j] = md_buffer[16 + j] ^ md_buffer[j]

            t = 0
            for j in range(18):
                for k in range(48):
                    t = md_buffer[k] ^ self.S[t]
                    md_buffer[k] = t
                t = (t + j) % 256

        return "".join([f"{i:02x}" for i in md_buffer[:16]])
