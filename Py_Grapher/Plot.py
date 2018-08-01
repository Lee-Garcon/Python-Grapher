import postfix
import sys

class Equation(object):
    def __init__(self, y_in_x, y_high, x_high):
        self.str_equ = y_in_x
        self.y_high = y_high
        self.x_high = x_high
        self.points = []
        self.find_all_points()

    def solve(self, x):
        if self.str_equ.count('%s') > 0:
            equ_string = self.str_equ % x
        else:
            equ_string = self.str_equ
        return postfix.Stack_Postfix(equ_string)

    def find_all_points(self):
        for x in range(self.x_high):
            y = self.solve(x)
            self.points.append([x, y])

class Grid(object):
    def __init__(self, w, l, marker='x', space=' ', highlight_color='red'):
        self.colors = {'black': '\03[30m',
                       'red': '\033[31m',
                       'green': '\033[32m',
                       'yellow': '\033[33m',
                       'blue': '\033[34m',
                       'magenta': '\033[35m',
                       'cyan': '\033[36m'}
        self.width = w
        self.length = l
        self.total_plot = w*l
        self.check_solution = False
        self.equations = []
        self.equation_graph = False
        self.failed_plots = 0
        self.highlight = []
        self.highlight_color = highlight_color
        self.id_colors = {}
        self.marker = marker
        self.pointlist = [[0 for x in range(self.width)] for i in range(self.length)]
        self.print_intersections = False
        self.reset_color = '\033[0m'
        self.space = space

    def clear(self):
        self.pointlist = [[0 for x in range(self.width)] for i in range(self.length)]
        self.highlight = []
        self.equations = []
        self.failed_plots = 0
        self.id_colors = {}
    def display(self, print_plots=False):
        retstr = ''
        retstr += '-' * (self.width + 2) + '\n'
        for idx, x in enumerate(self.pointlist[::-1]):
            disptext = '|'
            for idxy, valy in enumerate(x):
                if valy:
                    if [idx, idxy] in self.highlight:
                        pstring = self.colors[self.highlight_color] + self.marker + self.reset_color
                    elif valy in self.id_colors.keys():
                        pstring = self.colors[self.id_colors[valy]] + self.marker + self.reset_color
                    else:
                        pstring = self.marker
                    disptext += pstring
                else:
                    disptext += self.space
            disptext += '|'
            retstr += disptext + '\n'
        retstr += '-' * (self.width + 2)
        if print_plots:
            if self.print_intersections == True:
                retstr += '\nIntersections: \n%s' % '\n'.join([', '.join(val) for idx, val in enumerate(self.highlight)])
            print(retstr)
        else:
            return retstr

    def equation(self, inp):
        self.equation_graph = True
        self.equations.append(Equation(inp, self.width, self.length))
        for x in self.equations[-1].points:
            self.plot(x, id=len(self.equations)+1)

    def map(self, id, color):
        self.id_colors[id] = color

    def plot(self, point, id=1):
        if type(point) is tuple or type(point) is list:
            try:
                if point[0] >= 0 and point[1] >= 0:
                    if self.check_solution:
                        if self.pointlist[point[1]][point[0]] != 1:
                            self.highlight.append(point)
                    self.pointlist[point[1]][point[0]] = id
                else:
                    print('%s, %s is out of range.' % (point[0], point[1]))
            except IndexError:
                self.failed_plots += 1
                print('%s plot errors; recent: %s, %s' % (self.failed_plots, point[0], point[1]))

    def settings(self, check_solution=None, highlight_color=None, print_intersections=None):
        if check_solution != None:
            self.check_solution = check_solution
        if highlight_color != None:
            self.highlight_color = highlight_color
        if print_intersections != None:
            self.print_intersections = print_intersections

