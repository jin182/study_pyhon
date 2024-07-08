import inspect
import random

print(inspect.getfile(random)) # random 모듈 위치(경로)


import inspect
from travel import *

print(inspect.getfile(thailand)) # thailand 모듈 위치