# Rain OS Default .bashrc
if [[ $- != *i* ]]; then
    return
fi

alias ls='ls --color=auto'
alias ll='ls -la --color=auto'
alias grep='grep --color=auto'

# Rain OS prompt
PS1='\[[01;31m\]? RainOS\[[00m\]:\[[01;34m\]\w\[[00m\]\$ '

# Run fastfetch on interactive launch if available
if command -v fastfetch >/dev/null 2>&1; then
    fastfetch
fi
