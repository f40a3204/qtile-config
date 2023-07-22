
from libqtile import bar, layout, command
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.widget.decorations import PowerLineDecoration
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
# from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "wezterm"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows


    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod, "shift"], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "q", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "p", lazy.spawn("j4-dmenu-desktop"), desc="Spawn a command using a prompt widget"),

    # audio

    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer -i 5")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer -d 5")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer -t")),

    # flameshot
    Key([], "Print", lazy.spawn("flameshot gui")),
]

# groups = [Group(i) for i in "123456789"]
groups = [Group(i, label="") for i in "123456789"]


# workspaces = [
#        ("", "alacritty"),
#        ("", "chromium"),
#        ("", "alacritty"),
#        ("", "alacritty"),
#        ("", "alacritty"),
#        ("", "alacritty"),
#        ("", "alacritty"),
#        ("", "alacritty"),
#        ("", "alacritty"),
#        ]

# groups = []

#for i, workspace in enumerate(workspaces):
#    groups.append(Group(workspace[0]))
#    keys.extend(
#            [
#                Key(
#                    [mod],
#                    str(i + 1),
#                    lazy.group[workspace[0]].toscreen(),
#                    desc = f"switch to group {i + 1}"
#                    ),
#                Key(
#                    [mod, "shift"],
#                    str(i + 1),
#                    lazy.window.togroup(workspace[0], switch_group=True),
#                    desc = f"switch to and move window to group {i + 1}"
#                    )
#                ]
#            )

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
           # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(#border_focus_stack=["#0F090A", "#DC2644"],
                   border_normal = "#0F090A",
                   border_focus = "#e6381e",
                   # border_focus = "#FFFFFF",
                   border_width=5,
                   margin=10),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Hack Nerd Font",
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

decor = {
    "decorations": [
        RectDecoration(colour="#000000", radius=14, filled=True, group=True, padding_y=4)
    ],
    "padding": 5,
}

powerlineR = {
    "decorations": [
        PowerLineDecoration(path="rounded_right")
    ],
}
powerlineL = {
    "decorations": [
        PowerLineDecoration(path="rounded_left")
    ],
}


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    background = "#000000",
                    fmt = " "
                    ),

                widget.TextBox(
                    background = "#000000",
                    fmt = "󰮫 ",
                    mouse_callbacks = {
                        "Button1": lazy.spawn("j4-dmenu-desktop"),
                        },
                    fontsize = 25,
                    ),

                widget.AGroupBox(
                    background = "#000000",
                    **powerlineL
                    ),


                widget.TextBox(
                    format = " ",
                    ),


                widget.GroupBox(
                    highlight_method = "text",
                    fontsize = 30,
                    hide_unused = True,
                    this_current_screen_border="#FFFFFF", 
                    active = "#808080",

                    **decor),

                 widget.TextBox(
                    # format = "     ",
                    ),
                
                widget.WindowName(
                    max_chars = 50
                    ),

                widget.TextBox(
                    format = " ",
                    ),



                #widget.Visualizer(
                    # autostart = True,
                #    ),
               

                widget.Spacer(
                        length = 30,
                    ),

                widget.CPU(
                    format = "   {load_percent}% ", 
                    **decor
                    ),
                widget.TextBox(
                    format = "  ",
                    ),
                widget.Memory(
                    format = "   {MemPercent}% ",
                    **decor
                    ),
                widget.TextBox(
                    format = "  ",
                        ),
                widget.DF(
                    visible_on_warn = False,
                    format = "   {r:.00f}% ",
                    **decor
                        ),

                widget.Spacer(
                        length = 500
                        ),


                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),

                
                widget.Volume(
                        fmt="󰖀 {}" 
                        ),

                widget.TextBox(
                        format = " ",
                        ),
                widget.UPowerWidget(
                        battery_name = "BAT0",
                        ),

                widget.Battery(
                    battery = 0,
                    format = "{percent:2.0%}",
                    ),


                widget.WiFiIcon(
                        padding = 10,
                        mouse_callbacks = {
                            "Button1": lazy.spawn("networkmanager_dmenu"),
                        },
                        interface = "wlan0",
                        ),



                widget.Systray(
                        background="#1f1f1f99",
                        ),


                widget.TextBox(
                    format=" ",
                    **powerlineR
                    ),
                widget.Clock(
                    format="  %I:%M %p",
                    background = "#000000",
                    **powerlineR
                    ),
                widget.TextBox(
                    fmt="⏻ ",
                    mouse_callbacks = {
                        "Button1": lazy.spawn("bash /home/oxynoe/.config/qtile/shutdown.sh"),
                        },
                    fontsize=18,
                    background = "#000000" 
                    )
            ],
            35,
            background="#1f1f1f99",
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None

wmname = "LG3D"
