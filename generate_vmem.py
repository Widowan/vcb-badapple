#!/bin/python3
from PIL import Image
import os

SCALE = 32

frame_files = sorted(os.listdir('./1bit-frames'))

frame_buffer = [0,0,0,2]
for frame in frame_files:
    img = Image.open(f'./1bit-frames/{frame}').load()
    for y in range(SCALE):
        actual_byte = 0
        for x in range(SCALE):
            bit = 1 if img[x,y] > 0 else 0
            actual_byte = (actual_byte << 1) | bit
            if (x + 1) % 8 == 0:
                frame_buffer.append(actual_byte)
                actual_byte = 0

with open('badapple.vcbmem', 'wb') as f:
    f.write(bytes(frame_buffer))
