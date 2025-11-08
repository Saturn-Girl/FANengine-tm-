# FANengine.py
from ursina import *
import ctypes

# Keep a reference to the app so it's not garbage collected
_app = None

print("GNU FANengine™ version 1.0 — © Saturn Computing Topic")

def Init():
    """Initialize FANengine and start Ursina."""
    global _app
    _app = Ursina()
    print("FANengine™ initialized successfully!")

    try: 
        FanPlayer = ctypes.CDLL("FanPlayer.dll")
        result = FanPlayer._Init()
        print(f"[INFO] {FanPlayer}")
        print(f"[INFO] result from dll {result}")
    except Exception as e:
        print(f"[INFO] {e}")


def LoadModel(model_name: str):
    """Load a 3D model into the scene."""
    print(f"[INFO] Loading model {model_name}")
    Entity(model=model_name)


def PlaySound(sound_path: str, loop: bool = False, volume: float = 1.0):
    """Play a sound using Ursina's Audio system."""
    print(f"[INFO] Playing sound: {sound_path}")
    try:
        sound = Audio(sound_path, loop=loop, autoplay=True)
        sound.volume = volume
        return sound
    except Exception as e:
        print(f"[ERROR] Could not play sound: {e}")
        return None


def Run():
    """Start the main game loop."""
    if _app is None:
        print("Error: FANengine not initialized. Call Init() first!")
        return
    print("FANengine™ is now running...")
    _app.run()
