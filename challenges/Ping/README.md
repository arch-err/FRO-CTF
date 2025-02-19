# Ping
*Kan du hitta sårbarheten på den här webbsidan?*

## Solution
1. This is a web challenge, and I'm given an input field. My first reaction is that this is supposed to be a "ping-service", you input an address and it pings it, but it doesn't seem to work... I input a valid address and it doesn't give me any response...
2. So, obviously this is just a simple command injection, terminate the ping command by inserting a `;`, since this most likely is just running `ping <user input>` in a shell. So, we should be able to run commands? Maybe a simple `cat flag.txt`?
3. Nope, of course there is a blacklist of commands. I try out some useful commands to see if they work: things like `cat` and `ls` are obviously blacklisted, but `base64` isn't!
4. Since the `base64` command is meant to be used on a file (or stdin) I can simply try to insert `; base64 flag.txt`, which *theoretically* should give me the contents of `flag.txt` encoded in base64.
5. Oh, whould you look at that! It actually worked!!

## Flag
**Flag:** `fro{svag_inmatningsfält}`
