# Följa_recept
*Grattis! Du har hittat ett mycket värdefullt recept, receptet till en flagga. Baka tårtan och hitta flaggan.*

## Solution
1. Uhhm, weird code... Esolang?! Yeah, apparently something called *"Chef"*
2. We found [this website](https://esolangpark.vercel.app/ide/chef) to interpret the chef-language, but [the given code](./original_files/recept) just gives us some mumbo-jumbo string as output...
3. After a bit of looking around at other interpretors and stuff I gave up and looked at the hint. Apparently there is apparently a key in the given code that I should use to decode/decrypt the mumbo-jumbo-output... Seriously? Alright, since `a7e` is the only weird word in the code I'll assume that this is the key we are supposed to use.
4. Some "cybercheffing" later, it turns out that the bullshit-output is xor:ed with `a7e`, and guess what?! That gives us the **reversed** flag, **WHY**?!? ***\*Sigh...\**** Alright, sure, why not?! I suppose it wouldn't be a CTF without a challenge with a completely illogical sollution...


## Flag
**Flag:** `fro{mormors_hemliga_recept}`
