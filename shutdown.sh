#!/bin/bash

choices=("shutdown" "lock" "reboot" "logout" "cancel")

chosen=$(printf '%s\n' "${choices[@]}" | dmenu -p "Shutdown menu:")

case "$chosen" in
    "shutdown") doas poweroff ;;
    "lock") slock ;;
    "reboot") doas reboot ;;
    "logout") doas pkill -KILL -u "$USER" ;;
    *) exit 0 ;;
esac
