#!/usr/bin/env python

with open("./message.txt", "rb") as f:
    message = f.read()
print(message)

res = ""
for i in message:
    if i == 32:
        res += "0"
    if i == 0:
        res += "1"

print(res)
