# Utvecklingsmiljön
*Det finns en flagga i detta repository (se flag.zip).*

## Solution
1. The description mentions a repository, so I'll guess that this is a git-repo..
2. Unzip the `flag.zip`, go into the repo, open `lazygit` (cuz you know, I'm lazy)
3. Oh, there are only three commits, but one of them mentions a flag... what happened here? Wow, and there's the flag... I didn't even mean to find it just yet but it's just there in plain text...
4. Here's a oneliner to get the flag, if anyone wants it... `git grep -n "fro{" $(git rev-list --all)`


## Flag
**Flag:** `fro{dedikerad_att_återblicka}`
