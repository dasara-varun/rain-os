# Rain OS Interactive Shell Configuration
[[ $- != *i* ]] && return

# Shell Options
shopt -s checkwinsize
shopt -s histappend
HISTCONTROL=ignoreboth:erasedups
HISTSIZE=5000
HISTFILESIZE=10000

# Useful Aliases
alias ls='ls --color=auto'
alias ll='ls -lah --color=auto'
alias la='ls -A --color=auto'
alias l='ls -CF --color=auto'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'
alias df='df -h'
alias free='free -h'
alias update='sudo pacman -Syu'
alias sysinfo='fastfetch'
alias guide='rain-guide'

# Colored Git Prompt
parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
PS1='\[\033[01;36m\]\u@rain-os\[\033[00m\]:\[\033[01;34m\]\w\[\033[01;33m\]$(parse_git_branch)\[\033[00m\]\$ '

# Fastfetch greeting on primary interactive shell
if [[ -z "${FASTFETCH_SHOWN:-}" && "$SHLVL" -eq 1 ]]; then
    export FASTFETCH_SHOWN=1
    if command -v fastfetch >/dev/null 2>&1; then
        fastfetch
    fi
fi

