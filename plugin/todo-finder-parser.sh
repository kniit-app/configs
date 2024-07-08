#!/bin/bash
grep --with-filename --line-number --ignore-case todo "${1}" | \
sed -E 's/(.*):([0-9]+):(.*)/\1:\2:0: [error] Found todo in \"\3\" (found-todo)/'"