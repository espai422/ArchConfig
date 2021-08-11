#!/bin/pyhton
from typing import List  # noqa: F401
from libqtile import qtile

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import subprocess
from time import sleep, time
import random
import Mywidget
import widgetNet
##### My imports #####


background = ["#1e2127","#1e2127"]
foreground = ['#D4E6DA','#D4E6DA']

audio = '/home/espai422/.config/qtile/scripts/volume.sh'


try:
    subprocess.run('/home/espai422/.config/qtile/autostart.sh')
except:
    pass

mod = "mod4"
terminal = guess_terminal()
myTerm = 'alacritty'


keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),

    # rezize windows
    Key([mod, "shift"], "l", lazy.layout.shrink()),
    Key([mod, "shift"], "h", lazy.layout.grow()),

    #change focused window

    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    #flotating windows
    Key([mod, "shift"], "f", lazy.layout.toggle_floating()),

    #Terminal
    Key([mod], "Return", lazy.spawn("alacritty")),
    
    #browser
    Key([mod], "b", lazy.spawn("firefox")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    #restart shutdown
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),

    #menu
    Key([mod], "m", lazy.spawn("rofi -show drun")),
    Key([mod,"shift"], "m", lazy.spawn("rofi -show")),

    #window
    Key([mod], "s", lazy.spawn("scrot")),
    Key([mod,"shift"], "s", lazy.spawn("flameshot")),
    Key([mod], "f", lazy.spawn("thunar")),

    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),
]
# XF86AudioLowerVolume
groups = [Group(i) for i in [" "," "," ", " ","", "שּׁ ", " "," "]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])


layout_conf = {
    'border_focus':'#2f3238',
    'border_width':1,
    'margin':7
}
layout_conf2 = {
    'border_focus':'#00c0d9',
    'border_width':1,
    'margin':4
}

def prueba():
    pass

layouts = [
    #layout.Columns(**layout_conf,border_focus_stack='#d75f5f'),
    layout.MonadTall(**layout_conf),
    layout.Max(**layout_conf),
    #Try more layouts by unleashing below layouts.
    #layout.Stack(num_stacks=2),
    #layout.Bsp(**layout_conf),
    #layout.Matrix(**layout_conf),
    #layout.MonadWide(**layout_conf),
    layout.RatioTile(**layout_conf2),
    #layout.Tile(**layout_conf),
    #layout.TreeTab(**layout_conf),
    #layout.Zoomy(**layout_conf),
    #layout.VerticalTile(**layout_conf),
]

widget_defaults = dict(
    font='UbuntuMono Nerd Font',
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

widgets = [


],

screens = [
    Screen(
        top=bar.Bar([
            widget.GroupBox(
                background=["#62656b","#62656b"],
                foreground=["#ffffff","#ffffff"],

                font='UbuntuMono Nerd Font',
                fontsize=25,

                active=["ffffff","ffffff"],
                inactive=["#1e2127","#1e2127"],

                rounded=False,
                highlight_method='text',
                urgent_alert_method='block',

                urgent_border=["#E06C75","#E06C75"],

                this_current_screen_border=["#9DC0E3","#9DC0E3"],
                #this_current_screen_border=["#2f3238","#5f656a"],
                #this_current_screen_border=["#1e2127","#1e2127"],
                this_screen_border=["#FFFFFF","#FFFFFF"],
                #this_screen_border=["#ABB2BF","#ABB2BF"],

                other_current_screen_border=["#1e2127","#1e2127"],
                other_screen_border=["#1e2127","#1e2127"],

                disable_drag=True
                ),

            widget.TextBox(
                text=' ',
                font = 'mononoki Nerd Font',
                fontsize=50,
                padding=-6,
                background = ["#62656b","#62656b"], 
                #foreground = ["#404349","#404349"],
                #foreground = ["#2f3238","#2f3238"],
                foreground = ["#62656b","#62656b"],
            ),

            widget.Clipboard(
                background=["#62656b","#62656b"],
                foreground=['#D4E6DA','#D4E6DA'],
                max_width=28,
                font='mononoki Nerd Font',
                fontsize= 23,
                timeout= 40,
                blacklist = '',
            ),

            widget.TextBox(
                text=' ',
                font = 'mononoki Nerd Font',
                fontsize=50,
                padding=-6,
                background = ["#2f3238","#2f3238"], 
                #foreground = ["#404349","#404349"],
                #foreground = ["#2f3238","#2f3238"],
                foreground = ["#62656b","#62656b"],
            ),
            #255.255.255.255

            widget.Spacer(
                background=["#2f3238","#2f3238"],
            ),

            widget.TextBox(
                text=' ',
                background=["#1e2127","#1e2127"],
                font = 'mononoki Nerd Font',
                fontsize = 35,
                padding = -3,
                foreground = ["#2f3238","#2f3238"]
            ),

            Mywidget.Hack(
                background=["#1e2127","#1e2127"],
                foreground=['#D4E6DA','#D4E6DA'],
                update_interval = 0.07,
                font = 'HEAVYDATA Nerd Font ',
                #font = 'mononoki Nerd Font',
                fontsize = 25,

            
            ),
            widget.TextBox(
                text=' ',
                #text=' ',
                background=["#1e2127","#1e2127"],
                font = 'mononoki Nerd Font',
                fontsize = 40,
                padding = -3,
                foreground = ["#2f3238","#2f3238"]
            ),
            # widget.GenPollText(
            #     background=["#1e2127","#1e2127"],
            #     foreground=['#D4E6DA','#D4E6DA'],
            #     func=prueba,
            #     update_interval = 1
            # ),

            widget.Spacer(
                background=["#2f3238","#2f3238"]
            ),
            widget.TextBox(
                text='',
                font = 'mononoki Nerd Font',
                fontsize=50,
                padding=-6,
                #mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('pavucontrol')},
                background = ["#2f3238","#2f3238"], 
                #foreground = ["#404349","#404349"],
                #foreground = ["#2f3238","#2f3238"],
                foreground = ["#62656b","#62656b"],
            ),
            # 墳 
            widget.WidgetBox(
                [
                widgetNet.NetworkIP(
                    font = 'mononoki Nerd Font',
                    fontsize=23,
                    update_interval = 5,
                    foreground = ['#D4E6DA','#D4E6DA'], 
                    background = ["#62656b","#62656b"],
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('nm-connection-editor')}
                ),

                widget.TextBox(
                    text='',
                    font = 'mononoki Nerd Font',
                    fontsize=50,
                    padding=-6,
                    foreground = ["#2f3238","#2f3238"], 
                    background = ["#62656b","#62656b"],),

                widget.TextBox(
                    text='墳 ',
                    font = 'mononoki Nerd Font',
                    fontsize=30,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('pavucontrol')},
                    background = ["#2f3238","#2f3238"], 
                    foreground = ['#D4E6DA','#D4E6DA'],),

                widget.PulseVolume(
                    background=["#2f3238","#2f3238"],
                    foreground=['#D4E6DA','#D4E6DA'],
                    font='mononoki Nerd Font',
                    fontsize= 20,
                    step = 5,

                ),
                widget.TextBox(
                    text='',
                    font = 'mononoki Nerd Font',
                    fontsize=50,
                    padding=-6,
                    background = ["#2f3238","#2f3238"], 
                    foreground = ["#62656b","#62656b"],
                ),
                widget.TextBox(
                    text='',
                    font = 'mononoki Nerd Font',
                    fontsize=30,
                    background = ["#62656b","#62656b"], 
                    foreground = ['#D4E6DA','#D4E6DA'],
                ),
                widget.Battery(
                    background=["#62656b","#62656b"],
                    foreground=['#D4E6DA','#D4E6DA'],
                    font='mononoki Nerd Font',
                    fontsize= 20,
                    battery= 0,
                ),


                widget.TextBox(
                    text='',
                    font = 'mononoki Nerd Font',
                    fontsize=50,
                    padding=-6,
                    foreground = ["#2f3238","#2f3238"], 
                    background = ["#62656b","#62656b"],
                ),

                widget.TextBox(
                    text=' ',
                    font = 'mononoki Nerd Font',
                    fontsize=30,
                    padding=2,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e htop')},
                    background = ["#2f3238","#2f3238"], 
                    foreground = ['#D4E6DA','#D4E6DA'],
                ),

                widget.Memory( # Hardcoded formatR
                    background=["#2f3238","#2f3238"],
                    foreground=['#D4E6DA','#D4E6DA'],
                    font='mononoki Nerd Font',
                    fontsize= 20,
                ),

                widget.TextBox(
                    text='',
                    font = 'mononoki Nerd Font',
                    fontsize=50,
                    padding=-6,
                    background = ["#2f3238","#2f3238"], 
                    foreground = ["#62656b","#62656b"],
                ),

                widget.ThermalSensor(
                    background=["#62656b","#62656b"],
                    foreground=['#D4E6DA','#D4E6DA'],
                    font='mononoki Nerd Font',
                    fontsize= 20,
                    battery= 0
                ),

                ],
                foreground=["#FFFFFF","#FFFFFF"],
                background=["#62656b","#62656b"],#["#2f3238","#2f3238"],
                font='mononoki Nerd Font',
                fontsize= 20,
                text_open= '  ',
                text_closed= '  ',
            ),

            widget.CurrentLayoutIcon(
                background=["#62656b","#62656b"],
                foreground=["#FFFFFF","#FFFFFF"],
                scale= 0.55
            ),
            
            widget.CapsNumLockIndicator(
                background=["#62656b","#62656b"],
                foreground=["#FFFFFF","#FFFFFF"],
                font='mononoki Nerd Font',
                fontsize= 20,
            ),

            widget.Clock(
                background=["#62656b","#62656b"],
                foreground=["#FFFFFF","#FFFFFF"],
                format='%H:%M',
                font='mononoki Nerd Font',
                fontsize = 20
                ),

            widget.Systray(
                background=["#62656b","#62656b"],
                foreground=["#FFFFFF","#FFFFFF"],
            ),



        ],
            33, opacity = 0.9
        ),
    ),

]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
], border_focus="FF00FF")
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
