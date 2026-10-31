"""File locations when NetworkGuard runs on its own (the PowerGuard AI platform has its own pg_paths)."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(ROOT, 'logo.png')


def model(name):
    return os.path.join(ROOT, name)
