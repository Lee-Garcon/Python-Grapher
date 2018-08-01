import Plot
import sys

print('Enter the dimensions of Graph\nFormat: (w, h)')
dimensions = [int(c) for c in input('> ').replace('(', '').replace(')', '').replace(' ','').split(',')]

qu = False

# SETUP
graph = Plot.Grid(dimensions[0], dimensions[1])


while True:
    print('Options:')
    print('(1) Plot a point')
    print('(2) Plot an equation')
    print('(3) Display graph')
    print('(4) Clear graph')
    print('(5) Settings')
    inp = input('> ')
    inpn = -1
    vcommand = True
    try:
        inpn = int(inp)
        if inpn not in [1, 2, 3, 4, 5]:
            vcommand = False
            print('Not a valid Option; please enter a valid command.')
    except TypeError:
        vcommand = False
        print('Not a valid Option; please enter a valid command.')
    except:
        print('FATAL ERROR: exiting...')
        sys.exit(1)
    if vcommand:
        if inpn == 1:
            print('Enter a point in coordinate form:')
            inp = input('> ')
            point = [int(c) for c in inp.replace('(', '').replace(')', '').replace(' ','').split(',')]
            graph.plot(point)
        elif inpn == 2:
            print('Enter an equation in postfix notation.')
            print('e.g. y = 2 x * 20 -')
            inp = input('> ')
            expression_str = inp.replace('y = ', '').replace('x', '%s')
            graph.equation(expression_str)
        elif inpn == 3:
            disp = graph.display()
            print(disp)
        elif inpn == 4:
            print('Graph Cleared')
            graph.clear()
        elif inpn == 5:
            vcommand = False
            print('SETTINGS')
            print('(1) Change Highlight Color (Current: %s)' % graph.highlight_color)
            print('(2) Change Marker (Current: %s)' % graph.marker)
            print('(3) Change Check Solutions (Current: %s)' % str(graph.check_solution))
            print('(4) Map lines to colors')
            print('(5) Print out intersections (Current: %s)' % str(graph.print_intersections))
            inp = input('> ')
            try:
                inpn = int(inp)
                vcommand = True
            except:
                print('Invalid command; returning to main menu.')
            if vcommand:
                if inpn == 1:
                    print('Enter Highlight Color:')
                    print('Options: \n%s' % '\n'.join(graph.colors.keys()))
                    inp = input('> ')
                    if inp not in graph.colors.keys():
                        print('Invalid input; returning to main menu.')
                    else:
                        graph.settings(highlight_color=inp)
                elif inpn == 2:
                    print('Enter Marker (Must be single-digit):')
                    inp = input('> ')
                    if len([c for c in inp]) == 1:
                        graph.marker = inp
                    else:
                        print('Invalid input; returning to main menu.')
                elif inpn == 3:
                    if graph.check_solution:
                        graph.settings(check_solution=False)
                    else:
                        graph.settings(check_solution=True)
                elif inpn == 4:
                    for idx, val in enumerate(graph.equations):
                        try:
                            print('line %s, index %s is mapped to %s' % ('y = %s' % val.str_equ % 'x', idx + 2, graph.id_colors[idx + 2]))
                        except KeyError:
                            print('line %s, index %s' % (('y = %s' % val.str_equ % 'x'), idx + 2))
                    print('\nInput id and color (e.g. (2 red))')
                    inp = input('> ').replace('(', '').replace(')', '').replace(' ','').split(',')
                    graph.map(int(inp[0]), inp[1])
                elif inpn == 5:
                    if graph.print_intersections:
                        graph.settings(print_intersections=False)
                    else:
                        graph.settings(print_intersections=True)

