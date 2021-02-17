import unittest
import ctypes

from util import get_cursor
from util import get_tu
from util import ClangTest
import logging
import sys


class EnumTest(ClangTest):

    """Test if Enum are correctly generated.
    """

    def test_enum(self):
        """
        """
        flags = ['-target', 'i386-linux']
        self.gen('test/data/test-enum.c', flags)
        self.assertEqual(ctypes.sizeof(self.namespace.myEnum), 4)
        self.assertEqual(self.namespace.ZERO, 0)
        self.assertEqual(self.namespace.ONE, 1)
        self.assertEqual(self.namespace.FOUR, 4)


if __name__ == "__main__":
    # logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    # logging.getLogger('codegen').setLevel(logging.INFO)
    unittest.main()
