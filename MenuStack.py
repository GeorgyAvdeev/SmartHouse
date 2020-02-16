class MenuStack:

    def __init__(self, first_menu):
        self.menus = [first_menu]
        self.selected = [0]

    def push(self, menu):
        self.menus.append( menu)
        self.selected.append(0)

    def pop(self):
        if len(self.menus) > 1:
            return self.menus.pop()

    def get_menu(self):
        return self.menus[-1]

    def get_position(self):
        return self.selected[-1]

    def set_position(self, new_pos):
        self.selected[-1] = new_pos

