from setuptools import setup
import ctypes

def show_popup():
    try:
        ctypes.windll.user32.MessageBoxW(
            0,
            "PIP Detection Test Triggered",
            "Hello from pip install",
            0x1
        )
    except:
        pass

# Run popup during install
show_popup()

setup(
    name="pip-detection-test-v3",
    version="3.0",
  packages=["pip_detection_test_v3"],
)
