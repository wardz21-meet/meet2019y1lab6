import turtle

num_pts=10
for i in range(num_pts):
    turtle.left(360/num_pts)
    turtle.forward(100)

turtle.mainloop()
print(range(num_pts))
