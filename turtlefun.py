import turtle

t = turtle.Turtle()
t.shape('turtle')
for i in range(4):
  for i in range(1):
    t.forward(100)
    t.rt(90)
  for i in range(4):
    t.rt(-90)
    t.forward(20)



turtle.mainloop()      # should be last line of program