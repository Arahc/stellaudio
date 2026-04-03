from re import sub
import subprocess
import threading

class SimplePlayer:
    def __init__(self):
        self.process = None

    def load(self, path: str):
        self.path = path

    def play(self):
        self.process = subprocess.Popen(
            ["ffplay", "-nodisp", "-autoexit", self.path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    def stop(self):
        if self.process:
            self.process.terminate()
