from bomb import explosives, bomb

class my_explosives(explosives):
    def trigger(self):
        print("Lol, not today, buddo")

class my_wrapper(bomb, my_explosives):
    def trigger(self):
        super().trigger()

bob = my_wrapper()
bob.trigger()
