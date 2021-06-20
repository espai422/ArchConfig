set fish_greeting ""

# Aliases
alias discord "/home/espai422/discord/discord.sh" &
alias grep "grep --color=auto"
alias ccat "ccat -G Plaintext="blink" -G Keyword="purple" -G String="darkgreen" -G Punctuation="brown" -G Comment="faint""
alias ls "exa --group-directories-first"
alias tree "exa -T"
alias Writer "/usr/bin/libreoffice --writer" &
alias Calc "/usr/bin/libreoffice --calc" &
alias 100%hacker "neofetch" &
alias pycritty "//home/espai422/.config/alacritty/pycritty.py"

alias cat "bat --theme ansi -f --paging=never"
alias dump "echo hola"


# hacker alias
alias mkt "mkdir nmap content scripts tmp exploits"
alias mapear "nmap -p- --open -v -n -oG allPorts"
    # must be in the allPorts directory
alias extractPorts "cat allPorts | grep -oP '\d{1,5}/open' | cut -d '/' -f 1 | xargs | tr ' ' ','" 


# Agnoste

set -g theme_display_user yes
set -g theme_hide_hostname yes
set -g color_user_bg a151d3
set -g color_user_str black
set -g color_dir_bg f07178
set -g color_git_bg fb9f7f
set -g color_git_dirty_bg yellow
set -U AGNOSTER_ICON_ROOT \u26a1 # unicode high voltage sign (⚡)
# Spacefish

set SPACEFISH_PROMPT_ADD_NEWLINE false
set SPACEFISH_PROMPT_PREFIXES_SHOW false
set SPACEFISH_PROMPT_DEFAULT_PREFIX " "
set SPACEFISH_PROMPT_DEFAULT_SUFFIX " "
set SPACEFISH_USER_SHOW always
set SPACEFISH_USER_COLOR green
set SPACEFISH_HOST_SHOW always
set SPACEFISH_HOST_COLOR cyan
set SPACEFISH_DIR_COLOR blue
set SPACEFISH_PROMPT_ORDER time user host dir git package node ruby golang php rust haskell julia elixir docker aws venv conda pyenv dotnet kubecontext exec_time line_sep battery vi_mode jobs exit_code char  

# __________functions_____________
#           colours
set red "\033[0;31m"
set nc "\033[0m"
set green "\33[0;32m"
#           hack
function extractPorts
    echo 
    set ip_address (cat allPorts | grep -oP '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' | sort -u)
    set open_ports (cat allPorts | grep -oP '\d{1,5}/open' | cut -d '/' -f 1 | xargs | tr ' ' ',')
    echo -e "$green [*] IP Address: $nc $ip_address"
    echo -e "$green [*] Open ports: $nc $open_ports \n"
    echo $open_ports | tr -d "/n" | xclip -sel clip
    echo -e "$red Open ports has been copyed to clipboard $nc \n"
end


