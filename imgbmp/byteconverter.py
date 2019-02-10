import os
from PIL import Image

def rgba_to_bin(rgba):
  return 1 if sum(rgba) < 639 else 0

def reverse_byte(b):
  c = (b & 0xf0) >> 4 | (b & 0x0f) << 4
  c = (c & 0xcc) >> 2 | (c & 0x33) << 2
  c = (c & 0xaa) >> 1 | (c & 0x55) << 1
  return c

header_types = {
  'default': 'const uint8_t {}[] = {{',
  'AVR': 'const uint8_t {}[] PROGMEM = {{',
}

class Img:
  def __init__(self, path):
    self.path = path
    self.image = Image.open(path)

  def to_byte_array(self, width, height, reverse_bytes=False):
    img = self.image.resize((width, height))
    pix = img.load()
    bytes_ = []

    dy = 0
    while dy <= height:
      for x in range(width):
        byte = 0
        for y in range(dy, dy+8):
          try:
            byte |= (rgba_to_bin(pix[x, y]) << (y - dy))
          except IndexError:
            pass # wuut
        if reverse_bytes:
          byte = reverse_byte(byte)
        bytes_.append(byte)

      dy += 8

    return bytes_

  def to_c_expression(self, width, height, reverse_bytes=False, header_type=None):
    bytes_ = self.to_byte_array(width, height, reverse_bytes)

    i = 0

    if header_type == 'none':
      out = ''
    else:
      out = header_types[header_type].format(os.path.basename(self.path).split('.')[0])

    for b in bytes_:
      if i % 8 == 0:
        out += '\n  '
      out += '{0:#02x},'.format(b)
      i += 1

    if header_type != 'none':
      out += '\n};'

    return out
