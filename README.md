# imgbmp

Many popular display devices like Nokia 5110 LCD, LED matrices, etc. follow 8-bit lines format for bitmap data.

This utility converts any image to this format.

# Examples

![](https://i.imgur.com/7tZNPd2.png)

    $ imgbmp cat.png -x 16 -y 16

    const uint8_t cat[] = {
      0x0,0x1c,0x38,0xf8,0xdc,0xc0,0xc0,0xc0,
      0x80,0x0,0xf0,0x88,0x68,0x48,0x70,0x0,
      0x0,0x0,0x0,0x11,0x1f,0x7,0xf,0x1f,
      0x1f,0x1c,0x10,0x19,0xf,0x0,0x0,0x0,
      0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,
      0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,
    };

![](https://i.imgur.com/QBIGXNb.jpg)

# Installation

    $ git clone https://github.com/adzierzanowski/imgbmp
    $ cd imgbmp
    $ pip3 install .

# Usage
    usage: imgbmp [-h] [-r] [-x WIDTH] [-y HEIGHT] [-t HEADER_TYPE]
              files [files ...]

    Convert images to byte bitmap

    positional arguments:
      files                 File(s) to be converted

    optional arguments:
      -h, --help            show this help message and exit
      -r, --reverse-bytes   Reverse the order of the bits in a byte
      -x WIDTH, --width WIDTH
                            Width of an output image in pixels
      -y HEIGHT, --height HEIGHT
                            Height of an output image in pixels
      -t HEADER_TYPE, --header-type HEADER_TYPE
                            Wrap bytes in a C declaration (one of: none, default,
                            AVR)
