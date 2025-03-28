class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = 'yellow'

cookie1 = Cookie('green')
cookie2 = Cookie('blue')

print(f"cookie 1: {cookie1.get_color()}")
print(f"cookie 2: {cookie2.get_color()}")

cookie2.set_color("yellow")

print(f"cookie 1 updated: {cookie1.get_color()}")
print(f"cookie 2 updated: {cookie2.get_color()}")