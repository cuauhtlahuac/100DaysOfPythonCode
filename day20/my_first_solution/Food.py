from Body import Body

class Food(Body):
    def __init__(self, init_pos):
        super().__init__(init_pos)
        # self.penup()
        self.pencolor("red")
        self.pendown()
        self.color("red")
        self.setpos(init_pos, 0)
    
    def get_left_pos(self):
        return self.pos()[0] - 20
    def get_top_pos(self):
        return self.pos()[1]
    def get_right_pos(self):
        return self.pos()[0] + 20
    
    left_limit = property(get_left_pos)
    top_limit = property(get_top_pos)
    right_limit = property(get_right_pos)
