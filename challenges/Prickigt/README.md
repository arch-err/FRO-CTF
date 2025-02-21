# Prickigt
*Hitta flaggan!*

## Solution
1. We're given an archive with a few files in it, nothing that looks particularly interesting, except for the two keepass databases (`.kdbx`).
2. Without so much as a hint towards what the master passwords are, I'll try to crack them open. `keepass2john` doesn't seem to work, so I'll have to borrow some code I wrote up for the sollution of a similar CTF-challenge I made myself. A version of this code can be found in [crack-keepass.sh](crack-keepass.sh).
3. For some reason the `keepassxc-cli` tool that's powering the keepass-cracker is working really slowly, so I'll leave it running for a while targeting both files... Some time later it turns out that `files/Passwords.kdbx` was actually crackable, with the password being `penguins`. The second database wasn't crackable, at least not with `rockyou.txt`.
4. There are a bunch of credentials in `files/Passwords.kdbx`, following a pretty simple pattern. There is an empty entry for *"Second Database"*, but assuming the pattern will apply for that entry too, the second master password will be easy to figure out: `SeconddatabasEPassworD14`
5. Unlocking the `files/Granska snarast/Seconddatabase.kdbx` with the password above will give us the flag.


## Flag
**Flag:** `fro{hittade_du_mönstret?}`
