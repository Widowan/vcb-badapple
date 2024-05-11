#!/bin/python3
from PIL import Image
import os
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

SCALE = 32

frame_files = sorted(os.listdir('./1bit-frames'))
#frame_files = frame_files[frame_files.index('01960.png'):]

frame_buffer = [0,0,0,2]
for frame in frame_files:
    img = Image.open(f'./1bit-frames/{frame}').load()
    print_frame = False
    if frame == '00100.png':
        print(f'100th frame, frame_buffer has {len(frame_buffer)} bytes')
        print_frame = True
    for y in range(SCALE):
        actual_byte = 0
        for x in range(SCALE):
            bit = 1 if img[x,y] > 0 else 0
            if print_frame:
                print(bit, end=' ')
            actual_byte = (actual_byte << 1) | bit
            if (x + 1) % 8 == 0:
                frame_buffer.append(actual_byte)
                actual_byte = 0
        if print_frame:
            print()

with open('badapple.vcbmem', 'wb') as f:
    f.write(bytes(frame_buffer))
