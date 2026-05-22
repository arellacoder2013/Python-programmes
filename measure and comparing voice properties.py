import threading
import sys

try:
    import pyaudio
    import numpy as np
    import matplotlib.pyplot as plt
    import speech_recognition as sr
    from speech_recognition import AudioData
except ImportError as e:
    print(f"❌Missing library:{e.name}")
    print("\n Install commands:")
    print(" Windows:")
