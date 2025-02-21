# Fyrkantigt
*Flaggans innehåll har krypterats, dekryptera den och lägg till flaggformatet.*
*Chiffertext - `rheesaaraoqve`*

## Solution
1. We get a ciphertext, a key, and a challenge name hinting towards a square. If you start off by googling square cipher...
2. After a bit of googling and trying a few online tools to decipher the given text I finally found that this apparently is a *bifid*-cipher, and that the key given was a *polybius-square*. Using [this online tool](https://cryptii.com/pipes/bifid-cipher) we can decipher the given message, and get the result `fairandsquare`. We'll wrap this string in `fro{}` and get the flag.

## Flag
**Flag:** `fro{fairandsquare}`
