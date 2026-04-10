from PIL import Image
import os
import time

ASCII = "@B%#●*+=-:. "

def to_ascii(img, width=120):
    img = img.convert("L")
    img = img.resize((width, int(width * 0.45)))

    pixels = img.getdata()
    chars = "".join(ASCII[pixel * len(ASCII) // 256] for p>

    lines = [chars[i:i+width] for i in range(0, len(chars)>
    return "\n".join(lines)

frames = sorted(os.listdir("frames"))

for f in frames:
    img = Image.open("frames/" + f)
    print("\033c", end="")   # clear screen
    print(to_ascii(img))
    time.sleep(1/30)
