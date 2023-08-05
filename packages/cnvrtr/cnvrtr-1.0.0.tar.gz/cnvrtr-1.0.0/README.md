# Description

Different functions to convert between hex, dec, bin, ascii etc.

# Installation

`pip install cnvrtr`

# Usage


```python

from cnvrtr.Converter import Converter

cnvrtr = Converter()

leHex = cnvrtr.toLittleEndian("af d0 fe")
# fed0af

hexToBin = cnvrtr.hexToBin("fed0af")
# 111111101101000010101111

hexToDec = cnvrtr.hexToDec("fed0af")
# 16699567

binToDec = cnvrtr.binToDec("11010101")
# 213

decToAscii = cnvrtr.decToAscii(65)
# A
```


# License

MIT