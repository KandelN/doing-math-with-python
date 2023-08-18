from math import radians, cos, sin

def coord_manual(u, theta):
    """
    Return list of coordinates when intital velocity
    and firing angle of projectile is given.
    Process does not involve the derivation
    of formaula final time.
    """
    theta = radians(theta)
    g = 9.81

    # Analytical time of flight
    analytical_T = 2*u*sin(theta)/g

    # Set initial condition
    t, x, y = 0.0, 0.0, 0.0
    vx = u*cos(theta)
    vy = u*sin(theta)
    del_t = 3/1000
    coords = x_coords, y_coords = [], []

    # Loop for the motion.
    while True:
        del_x = vx * del_t
        del_y = vy * del_t - 0.5 * g * del_t**2
        t += del_t
        x += del_x
        y += del_y
        vx = del_x/del_t
        vy = del_y/del_t

        if y < 0:
            break

        x_coords.append(x)
        y_coords.append(y)
        print(t, x, y, vx, vy, abs(complex(vx, vy)), sep ='\t')

    print(analytical_T, t)
    return coords
coord_manual(20, 50)
