from nd_maze import *

class MazeGraph2D(MazeGraphND):
    def __init__(self, width, height, gen_method="prims"):
        self.width, self.height = width, height
        super().__init__([height, width], gen_method)
    
    def __str__(self):
        deadend, left, right, above, below = 0, 1, 2, 4, 8
        boxdrawchar = [" ",  # no connections       0 = 0+0
                        "═", # deadend from left    1 = 0+1
                        "═", # deadend from right   2 = 0+2
                        "═", # left to right        3 = 1+2
                        "║", # deadend from above   4 = 0+4
                        "╝", # left to above        5 = 1+4
                        "╚", # right to above       6 = 2+4
                        "╩", # left, right, above   7 = 1+2+4
                        "║", # deadend from below   8 = 0+8
                        "╗", # left to below        9 = 1+8
                        "╔", # right to below      10 = 2+8
                        "╦", # left, right, below  11 = 1+2+8
                        "║", # above, below        12 = 4+8
                        "╣", # left, above, below  13 = 1+4+8
                        "╠", # right, above, below 14 = 2+4+8
                        "╬", # all connections     15 = 1+2+4+8
                        ]
    
        ret = ""
        for r in range(self.height):
            for c in range(self.width):
                neighbors = self.connections[(c,r)]
                bdc = deadend   # initialize the bdc to draw as 'no connections'
                
                if not c and not r:
                    bdc |= left     # start node
                if c == self.width-1 and r == self.height-1:
                    bdc |= right    # terminal node
                    
                # determine connections
                if (c, r-1) in neighbors:
                    bdc |= above
                if (c, r+1) in neighbors:
                    bdc |= below
                if (c-1, r) in neighbors:
                    bdc |= left
                if (c+1, r) in neighbors:
                    bdc |= right
                
                ret += boxdrawchar[bdc]  # draw junctions as boxdrawing characters
            ret += "\n"
        return ret

if __name__=="__main__":
    import sys
    
    if len(sys.argv) > 1:
        assert len(sys.argv) == 3, "Please specify a width and height"
        w,h = sys.argv[1:]
        try:
            width, height = int(w), int(h)
        except ValueError:
            print("Width and height should be passed as integers")
            sys.exit(0)
        m = MazeGraph2D(width, height)
    else:
        m = MazeGraph2D(80, 40)
    print(m)


