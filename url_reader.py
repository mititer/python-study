import os
from os import path

filename = "urls.py"
print(os.path.isfile(filename))

mod = __import__(filename)
print(mod)