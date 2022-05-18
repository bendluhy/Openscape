#TODO Create settings manager
from win32api import GetSystemMetrics

windowX = GetSystemMetrics(0)
windowY = GetSystemMetrics(1)
fps = 60