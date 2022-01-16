from libqtile.config import Group


class Groups(object):
    def setup_groups(self):
        groups = [Group(i) for i in "123456789"]

        return groups
