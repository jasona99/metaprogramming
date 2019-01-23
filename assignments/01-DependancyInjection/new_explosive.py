import bomb


class my_explosives:
    def explosives(self):
        print("Lol, not today, buddo")


class my_wrapper(bomb, my_explosives):
    def trigger(self):
        super().trigger()
