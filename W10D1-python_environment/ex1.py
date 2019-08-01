# 1. Find out what are the built-in modules available for you.
print(locals())
import sys
print(sys.builtin_module_names)


# 2. Import 3 built-in modules.
import marshal
import time
import errno

# 3. import 1 function from another built-in module
import zlib
from zlib import compress

# 4. In 1 line import 3 functions from a built-in module
from math import sqrt, cos, degrees
# 5. use a universal import to import all functions of a built-in module

from math import *


assert(calcFactorial(5) == 120)
print(exponent(3))
print(ceiling(3.2))