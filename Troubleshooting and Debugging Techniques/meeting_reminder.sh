#!/bin/bash

meeting_info=$(yad --forms \
  --title 'Meeting' --text "Reminder information" \
  --calendar "Date" --entry 'Title' \
  --entry 'Emails' \
  --forms-date-format='%Y-%m-%d' \
  2>/dev/null)

echo $meeting_info

if [[ -n "$meeting_info" ]]; then
  python3 send_reminders.py "$meeting_info"
fi
