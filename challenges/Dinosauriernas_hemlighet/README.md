# Dinosauriernas_hemlighet
*Vi vet att det finns en flagga på den här hemsidan.*

## Solution
1. So, we're given a link to a website that only has three images of dinosaurs and a tropical background...
2. My first instinct was that there could be something hidden in/around the images, but since they are pulled in from an external website it looks like they are just generic, boring, images.
3. Uhhh... I know you aren't *reeeaally* supposed to use brute-forcing tools for ctf's generally, but I don't see what else I could do here...
4. Let's run something like `feroxbuster`! Nope, there seems to be some sort of rate-limit in the way, ferox takes like 30s per request, that sucks!
5. Plan B: Let's do a manual check of possible files! `/robots.txt`, nope... `/security.txt`, nu-uh! `/hid`- no, I'm so stupid, I should just `/flag.txt`!
6. ***\*Sigh...\****, it really was just `/flag.txt`...


## Flag
**Flag:** `fro{andra_vägar}`
