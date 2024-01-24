class Turtle():
    x = 0
    y = 0
    s = 1
    
    
         
    def go_up(self):
        self.y = self.y + self.s
        
    def go_down(self):
         self.y = self.y -self.s
         
    def go_left(self):
         self.x = self.x - self.s
         
    def go_right(self):
         self.x = self.x + self.s
         
    def evolve(self):
         self.s += 1
         
    def degrade(self):
         if self.s - 1 <= 0:
             print('error')
         self.s = self.s - 1
         
    #def count_moves(self):
        #не понимаю, что значит х2, у2
        
h1 = Turtle()

h1.go_up()
h1.go_left()
h1.degrade()
print(h1.y, h1.x)

        
        