def force_function(x, y, vx, vy):
    k =1
    m= 1000
    g = 9.8
    v = (vx**2 + vy**2)**(1/2)
    Fx= -(k*v*vx)
    Fy= -(k*v*vy + m*g)
    return(Fx, Fy)

def position_function(x, y, vx, vy, Fx, Fy,t):
    xf =x + vx*t
    yf =y +vy*t
    vxf = vx + (Fx*t)/m
    vyf = vy + (Fy*t)/m
    return(xf, yf, vxf, vyf)
m = 1000

