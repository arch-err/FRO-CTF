# PwnedCorpo
*MegaBolagAB har drabbats av en stor ransomware-attack av en hackare! Använd OSINT för att hitta den filen som innehåller de känsliga inloggningsdetaljer och flaggan!*

## Solution
1. So, we're basically just given a single name, `MegaBolagAB`. Let's OSINT this shit!
2. After some googling I can't find anything on `MegaBolagAB`. I highly doubt it, but we could treat the given string as a username and run sherlock on it.
3. Sure enough, sherlock found a user on X. Let's dig out our old OSINT account and look around on X then (cuz who tf actually has an X-account?!)
4. The account only seems to have a single post where a single user commented. The user appears to be "the hacker", and after a quick google-search on his name I found his github-account.
5. Ok, so, the hacker only has one [github repo](https://github.com/H4ck3rm4nn3n/MEGABOLAG_AB_DATA) with the stolen data in it... Alright, there's the flag, thanks! Realistic? No! A fun challenge? Uuhhhm... No, not that either. Sorry, but if you want to create a ransomware-attack inspired challenge you should take a look at [CERT-SE:s latest CTF](https://github.com/arch-err/CERT-SE-CTF-2024) they had a good challenge on this! Is it realistic? Eeh, not really, but at least a bit closer than this thing is...

## Flag
**Flag:** `fro{pwned_företag}`
