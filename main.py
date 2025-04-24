import playsound3
import sys

print(playsound3.AVAILABLE_BACKENDS)
playsound3.playsound(sys.argv[1])
