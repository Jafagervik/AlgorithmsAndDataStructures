from graph import *
from priority_queue import *


def Huffman(C):
    """
    Computes binarycodes for letters such that the most common ones get lowest number possible
    :param C:
    :return:
    """
    n = len(C)
    Q = C

    for i in range(1, n):
        z = HuffmanNode()
        z.left = x = Q.Extract_Min()
        z.right = y = Q.Extrac_Min()
        z.freq = x.freq + y.freq
        Q.insert(z)

    # Returns the root of the three
    return Q.Extract_Min()
