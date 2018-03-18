import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1)
pixels.fill((0,0,0))
pixels.show()

while True:
    pixels.fill((255,255,255))