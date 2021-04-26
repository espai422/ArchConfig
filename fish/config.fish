set fish_greeting ""

# Aliases
alias discord "/home/espai422/discord/discord.sh" &
alias grep "grep --color=auto"
alias cat "ccat -G Plaintext="blink" -G Keyword="purple" -G String="darkgreen" -G Punctuation="brown" -G Comment="faint""
alias ls "exa --group-directories-first"
alias tree "exa -T"
alias Writer "/usr/bin/libreoffice --writer" &
alias Calc "/usr/bin/libreoffice --calc" &
alias 100%hacker "neofetch" &

# Agnoste

set -g theme_display_user yes
set -g theme_hide_hostname yes
set -g color_user_bg a151d3
set -g color_user_str black
set -g color_dir_bg f07178
set -g color_git_bg fb9f7f
set -g color_git_dirty_bg yellow

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
