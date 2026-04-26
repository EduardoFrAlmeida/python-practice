#python-if-else-weird-not-weird

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input('Digite um Número: ').strip())

    # 1. Verifica se o número é ímpar
    if n % 2 != 0:
        print("Weird")
    else:
        # Se chegou aqui, o número é obrigatoriamente par
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")
