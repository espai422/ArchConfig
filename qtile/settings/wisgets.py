from libqtile import widget

widget.GroupBox(
                    background=["#1e2127","#1e2127"],
                    foreground=["#ffffff","#ffffff"],

                    font='UbuntuMono Nerd Font',
                    fontsize=25,

                    active=["ffffff","ffffff"],
                    inactive=["#555555","#555555"],

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
                widget.WindowName(
                    background=["#1e2127","#1e2127"],
                    #foreground=['#a151d3','#a151d3'],
                    foreground=['#D4E6DA','#D4E6DA'],                    
                    font='mononoki Nerd Font',
                    fontsize= 20
                ),

                # widget.GenPollText(
                #     func=prueba,
                #     update_interval= 1,
                #     fontsize=30
                # ),
                #battery(),
                
                widget.WidgetBox([
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
                        update_interval = 1800,

                        background=['#ffd47e','#ffd47e'],
                        colour_have_updates=['#0f101a','#0f101a'],
                        colour_no_updates=['#0f101a','#0f101a'],

                        distro = "Arch_checkupdates",
                        display_format = "{updates}",
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')},

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

                    widget.Net(
                        foreground=['#0f101a','#0f101a'],
                        background=['#fb9f7f','#fb9f7f'],
                        interface='enp4s0f4u1u3',
                        font='UbuntuMono Nerd Font',
                        fontsize = 20
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
                        padding=10,
                        fontsize = 20
                    ),
                    widget.TextBox(
                        text='',
                        background=['#F07178',"#F07178"],#b6f81c
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
                        font='UbuntuMono Nerd Font',
                        fontsize = 20
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
__main__":
    battery()