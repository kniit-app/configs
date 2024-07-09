#!/bin/bash
# trunk-ignore(shellcheck/SC2312)
grep --with-filename --line-number --ignore-case TODO "${1}" |
	sed -E 's/(.*):([0-9]+):(.*)/\1:\2:0: [error] Found TODO in "\3" (found-todo)/'
