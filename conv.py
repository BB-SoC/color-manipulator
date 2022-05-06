# script to take any given color value and manipulate it in some desired fashion as taken by argument

class Color:
    def __init__(self, data):
        if data[0] == "rgb":
            self.r = data[1]
            self.g = data[2]
            self.b = data[3]
        elif data[0] == "hsv":
            self.h = data[1]
            self.s = data[2]
            self.v = data[3]
        else:
            print("You done fucked up A-A-Ron.")
            quit()
    
    def rgb_to_hsv(self):
        self.rh = self.r / 255
        self.gh = self.g / 255
        self.bh = self.b / 255

        cmax = max(self.rh, self.gh, self.bh)
        cmin = min(self.rh, self.gh, self.bh)

        self.diff = cmax - cmin

        if self.diff == 0:
            self.h = 0
        elif cmax == self.rh:
            self.h = (60 * ((self.gh - self.bh) / self.diff) + 360) % 360
        elif cmax == self.gh:
            self.h = (60 * ((self.bh - self.rh) / self.diff) + 120) % 360
        elif cmax == self.bh:
            self.h = (60 * ((self.rh - self.gh) / self.diff) + 240) % 360

        if cmax == 0:
            self.s = 0
        else: 
            self.s = (self.diff / cmax) * 100

        self.v = cmax * 100

#make a function to easily print values

c_red = ["rgb", 255, 0, 0]

new_color = Color(c_red)

new_color.rgb_to_hsv()

print(new_color.r, new_color.g, new_color.b)
print(new_color.h, new_color.s, new_color.v)