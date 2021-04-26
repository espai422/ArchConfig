from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

#from os import path
#import subprocess

#def autostart():
#    subprocess.call([path.join(path.expanduser(~), '.config','qtile','autostart.sh')])



mod = "mod4"
terminal = guess_terminal()

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
    Key([mod,"shift"], "s", lazy.spawn("scrot -s")),
    Key([mod], "f", lazy.spawn("thunar")),
]

groups = [Group(i) for i in ["   ","   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])



layout_conf = {
    'border_focus':'#00c0d9',
    'border_width':1,
    'margin':10
}
layout_conf2 = {
    'border_focus':'#00c0d9',
    'border_width':1,
    'margin':4
}

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

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    background=["#1e2127","#1e2127"],
                    foreground=["#ffffff","#ffffff"],
                    font='UbuntuMono Nerd Font',
                    fontsize=19,
                    active=["ccffff","ffffcc"],
                    inactive=["#555555","#555555"],
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    urgent_border=["#E06C75","#E06C75"],
                    this_current_screen_border=["#a151d3","#a151d3"],
                    this_screen_border=["#ABB2BF","#ABB2BF"],
                    other_current_screen_border=["#1e2127","#1e2127"],
                    other_screen_border=["#1e2127","#1e2127"],
                    disable_drag=True
                ),
                widget.WindowName(
                    background=["#1e2127","#1e2127"],
                    #foreground=['#a151d3','#a151d3'],
                    foreground=['#FF5555','#FF5555'],
                    font='UbuntuMono Nerd Font',

                ),
                widget.TextBox(
                    text='',
                    background=['#1e2127','#1e2127'],
                    foreground=['#ffd47e','#ffd47e'],
                    fontsize=43,
                    padding=-3
                ),

                widget.TextBox(
                    text=' ',
                    background=['#ffd47e','#ffd47e'],
                    foreground=['0f101a',"0f101a"],
                    fontsize=18,
                    padding=-3
                ),
                widget.CheckUpdates(
                    background=['#ffd47e','#ffd47e'],
                    colour_have_updates=['#0f101a','#0f101a'],
                    colour_no_updates=['#0f101a','#0f101a'],
                    no_update_string='0',
                    display_format= "{updates}",
                    update_interval=60,
                    distro='Arch', 
                    font='UbuntuMono Nerd Font',
                    fontsize=18
                ),
                widget.TextBox(
                    text='',
                    background=['#ffd47e','#ffd47e'],
                    foreground=['#fb9f7f','#fb9f7f'],
                    fontsize=43,
                    padding=-3
                ),
                widget.TextBox(
                    text='  ',
                    background=['#fb9f7f','#fb9f7f'],
                    foreground=['0f101a',"0f101a"],
                    fontsize=18,
                    padding=-3
                ),
                widget.Net(
                    foreground=['#0f101a','#0f101a'],
                    background=['#fb9f7f','#fb9f7f'],
                    interface='enp39s0',
                    font='UbuntuMono Nerd Font'
                ),
                widget.TextBox(
                    text=' ',
                    background=['#fb9f7f','#fb9f7f'],
                    foreground=['#F07178',"#F07178"],
                    fontsize=43,
                    padding=-3
                ),

                widget.CurrentLayoutIcon(
                    background=['#F07178',"#F07178"],
                    foreground=['#cbacff',"#eeffff"],
                    font='UbuntuMono Nerd Font',
                    scale=0.65
                ),
                widget.CurrentLayout(
                    background=['#F07178',"#F07178"],
                    foreground=['#0f101a',"#0f101a"],
                    font='UbuntuMono Nerd Font',
                    padding=10
                ),
                widget.TextBox(
                    text='',
                    background=['#F07178',"#F07178"],
                    foreground=['#a151d3',"#a151d3"],
                    fontsize=39,
                    padding=-3
                ),
                widget.Chord(
                    background=["#1e2127","#1e2127"],
                    foreground=['#cbacff',"#eeffff"],
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                    font='UbuntuMono Nerd Font'
                ),
                widget.TextBox(
                    text=' ',
                    background=["#a151d3","#a151d3"],
                    foreground=['#0f101a',"#0f101a"],
                    padding=5
                ),
                widget.Clock(
                    background=["#a151d3","#a151d3"],
                    foreground=['#0f101a',"#0f101a"],
                    format='%d/%m/%Y - %H:%M',
                    font='UbuntuMono Nerd Font'
                ),
                widget.TextBox(
                    text='',
                    background=["#a151d3","#a151d3"],
                    foreground=["#1e2127","#1e2127"],
                    fontsize=39,
                    padding=-3
                ),
                widget.Systray(
                    background=["#1e2127","#1e2127"],
                    foreground=['#cbacff',"#eeffff"],
                    font='UbuntuMono Nerd Font',
                    padding=13
                ),
                widget.TextBox(
                    text='',
                    background=["#1e2127","#1e2127"],
                    foreground=["#1e2127","#1e2127"],
                    fontsize=40,
                    padding=-3),
                    
            ],
            26, opacity = 0.95
        ),
    ),
    Screen(
        top=bar.Bar(
            [ 
                widget.GroupBox(
                    background=["#1e2127","#1e2127"],
                    foreground=["#ffffff","#ffffff"],
                    font='UbuntuMono Nerd Font',
                    fontsize=19,
                    active=["ccffff","ffffcc"],
                    inactive=["#555555","#555555"],
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    urgent_border=["#E06C75","#E06C75"],
                    this_current_screen_border=["#a151d3","#a151d3"],
                    this_screen_border=["#ABB2BF","#ABB2BF"],
                    other_current_screen_border=["#1e2127","#1e2127"],
                    other_screen_border=["#1e2127","#1e2127"],
                    disable_drag=True
                ),
                widget.WindowName(
                    background=["#1e2127","#1e2127"],
                    #foreground=['#a151d3','#a151d3'],
                    foreground=['#FF5555','#FF5555'],
                    font='UbuntuMono Nerd Font',
                ),

                widget.TextBox(
                    text='',
                    background=["#1e2127","#1e2127"],
                    foreground=['#F07178',"#F07178"],
                    fontsize=43,
                    padding=-3
                ),

                widget.CurrentLayoutIcon(
                    background=['#F07178',"#F07178"],
                    foreground=['#cbacff',"#eeffff"],
                    font='UbuntuMono Nerd Font',
                    scale=0.65
                ),
                widget.CurrentLayout(
                    background=['#F07178',"#F07178"],
                    foreground=['#0f101a',"#0f101a"],
                    font='UbuntuMono Nerd Font',
                    padding=10
                ),
                widget.TextBox(
                    text='',
                    foreground=['#1e2127',"#1e2127"],
                    background=['#F07178',"#F07178"],
                    fontsize=36,
                    padding=-3
                ),
                
            ],
            26, opacity = 0.95
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
