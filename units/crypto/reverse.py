from unit import BaseUnit
from collections import Counter
import sys
from io import StringIO
import argparse
from pwn import *
import os
import units.crypto

import string
import collections


class Unit(units.PrintableDataUnit):

	PROTECTED_RECURSE = True

	def evaluate(self, katana, case):

		result = self.target[::-1]
		katana.locate_flags(self, result)
		katana.recurse(self, result)
		katana.add_results(self, result)

	
