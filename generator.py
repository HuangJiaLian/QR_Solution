#!/usr/bin/env python
'''
@Description: QR generator
@Author: Jack Huang
@Date: 2019-05-22 10:33:42
@LastEditTime: 2019-05-22 14:57:34
@LastEditors: Please set LastEditors
'''
import clipboard
import qrcode
# 1. Get clipboard data
text = clipboard.paste()

# 2. Make a QR code according to the data 
result = qrcode.make(text)

# 3. Disiplay the data
result.show()
