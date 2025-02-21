# Tomt
*Finns det ens någonting här?*

## Solution
1. We get a file ([message.txt](./original_files/message.txt)) that only includes 00s and 20s (hex)
2. Let's assume that this is just in a binary format, so we can change out all 22s to 1s and 00s to 0s. Nope, that didn't decode to anything useful. Let's reverse it then: 00 = 1, 20 = 0. Yay, there is the flag!
3. `./solve.py`


## Flag
**Flag:** `fro{d0td0tspaced0t}`
