import numpy as np
import pyscreenshot as ps
import time


if __name__ == "__main__":
    try:
        f = open('config.txt')
        screen_coords = f.readline()[33:]
        numb_sq_hori = f.readline()[20:]
        numb_sq_vert = f.readline()[19:]
        color = f.readline()[15:]
        print(screen_coords)
        print(numb_sq_hori)
        print(numb_sq_vert)
        print(color)
        f.close()
    except IOError:
        print("No file")
        screen_coords = [10, 10, 1920, 1080]
        numb_sq_hori = 7
        numb_sq_vert = 6
        color = [237, 27, 36]

    screen_len_x = int(screen_coords[2]) - int(screen_coords[0])
    screen_len_y = screen_coords[3] - screen_coords[1]
    len_sq_x = screen_len_x / numb_sq_hori
    len_sq_y = screen_len_y / numb_sq_vert
    print(screen_len_x, screen_len_y)

    while True:
        im = np.array(ps.grab(screen_coords))
        arrays = np.array(im)
        for x in range(int(len_sq_x/2) +20, screen_len_x, int(len_sq_x)):
            for y in range(int(len_sq_y/2) +50,screen_len_y, int(len_sq_y)):
                if x > screen_len_x or y > screen_len_y:
                    break
                else:
                    a = arrays[y][x]
                    b = arrays[y+15][x+15]
                    c = arrays[y-15][x-15]
                    if a[0] >= color[0]-10 and a[0] <= color[0]+10 \
                        and a[1] >= color[1]-10 and a[1] <= color[1]+10 \
                            and a[2] >= color[2]-10 and a[2] <= color[2]+10:
                        #print("!!! Dashboard is RED !!!")
                        print("!!! Dashboard is RED !!!\n",x//len_sq_x+1, y//len_sq_y+1)
                        #print(x, y)
                    elif b[0] >= color[0]-10 and b[0] <= color[0]+10 \
                        and b[1] >= color[1]-10 and b[1] <= color[1]+10 \
                            and b[2] >= color[2]-10 and b[2] <= color[2]+10:
                        #print("!!! Dashboard is RED !!!")
                        print("!!! Dashboard is RED !!!\n",x//len_sq_x+1, y//len_sq_y+1)
                    elif c[0] >= color[0]-10 and c[0] <= color[0]+10 \
                        and c[1] >= color[1]-10 and c[1] <= color[1]+10 \
                            and c[2] >= color[2]-10 and c[2] <= color[2]+10:
                        #print("!!! Dashboard is RED !!!")
                        print("!!! Dashboard is RED !!!\n",x//len_sq_x+1, y//len_sq_y+1)
        time.sleep(1)