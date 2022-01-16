from libqtile.config import Key, Group, Drag, Click
from libqtile.command import lazy


class Bindings(object):
    def __init__(self) -> None:
        self.mod = "mod4"

    def setup_keys(self, setup_groups: bool = True):
        # Keybindings
        terminal = "alacritty"

        keys = [
            # A list of available commands that can be bound to keys can be found
            # at https://docs.qtile.org/en/latest/manwual/config/lazy.html
            # Switch between windows
            Key([self.mod], "h", lazy.layout.left(), desc="Move focus to left"),
            Key([self.mod], "l", lazy.layout.right(), desc="Move focus to right"),
            Key([self.mod], "j", lazy.layout.down(), desc="Move focus down"),
            Key([self.mod], "k", lazy.layout.up(), desc="Move focus up"),
            Key([self.mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
            # Move windows between left/right columns or move up/down in current stack.
            # Moving out of range in Columns layout will create new column.
            Key([self.mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
            Key([self.mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
            Key([self.mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
            Key([self.mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
            # Grow windows. If current window is on the edge of screen and direction
            # will be to screen edge - window would shrink.
            Key([self.mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
            Key([self.mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
            Key([self.mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
            Key([self.mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
            Key([self.mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
            # Toggle between split and unsplit sides of stack.
            # Split = all windows displayed
            # Unsplit = 1 window displayed, like Max layout, but still with
            # multiple stack panes
            Key(
                [self.mod, "shift"],
                "Return",
                lazy.layout.toggle_split(),
                desc="Toggle between split and unsplit sides of stack",
            ),
            Key([self.mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
            # Toggle between different layouts as defined below
            Key([self.mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
            Key([self.mod], "w", lazy.window.kill(), desc="Kill focused window"),
            Key([self.mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
            Key([self.mod, "control"], "t", lazy.restart(), desc="Reload the config"),
            Key([self.mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
            # Key([self.mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
            Key([self.mod], "r", lazy.spawn("rofi -show drun")),
        ]

        if setup_groups:
            from .groups import Groups

            groups_obj = Groups()
            groups = groups_obj.setup_groups()

            keys.extend(self.setup_group_keys(groups=groups))

        return keys

    def setup_group_keys(self, groups: list[Group]):

        group_keys = list()

        for i in groups:
            group_keys.extend(
                [
                    Key([self.mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),
                    Key(
                        [self.mod, "shift"],
                        i.name,
                        lazy.window.togroup(i.name, switch_group=True),
                        desc="Switch to & move focused window to group {}".format(i.name),
                    ),
                ]
            )

        return group_keys

    def setup_mouse(self):
        mouse = [
            Drag([self.mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
            Drag([self.mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
            Click([self.mod], "Button2", lazy.window.bring_to_front()),
        ]

        return mouse
