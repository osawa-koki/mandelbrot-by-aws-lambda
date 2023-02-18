import json
import base64
import io
from PIL import Image

width = 512
height = 512
x_min = -2.5
x_max = 1.5
y_min = -2.0
y_max = 2.0
iterations = 100
threshold = 10

# 画像を作成
image = Image.new('RGB', (width, height), (0, 0, 0))

for py in range(height):
    y = py / height * (y_max - y_min) + y_min
    for px in range(width):
        x = px / width * (x_max - x_min) + x_min
        z = complex(x, y)
        v = complex(0, 0)
        color = 0
        for n in range(iterations):
            v = v * v + z
            if abs(v) > threshold:
                color = 255 - threshold * n
                break
        image.putpixel((px, py), (color, color, color))

image.save('image.png')
