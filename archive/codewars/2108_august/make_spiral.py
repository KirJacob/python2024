import time


class Cell:
    right, bottom, left, top = "right", "bottom", "left", "top"
    directions = [right, bottom, left, top]

    def __init__(self, pos_x, pos_y, value):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.value = value

    def change_direction(self, directions_index):
        if directions_index == 3:
            return 0
        else:
            return directions_index + 1

    def print_cell(self):
        return f"cell({self.pos_x},{self.pos_y},{self.value})"

    def neighbors_num(self, maze):
        result_num = 0
        if maze.cell_array[self.pos_x][self.pos_y + 1].value == Maze.visited:
            result_num = result_num + 1
        if maze.cell_array[self.pos_x][self.pos_y - 1].value == Maze.visited:
            result_num = result_num + 1
        if maze.cell_array[self.pos_x + 1][self.pos_y].value == Maze.visited:
            result_num = result_num + 1
        if maze.cell_array[self.pos_x - 1][self.pos_y].value == Maze.visited:
            result_num = result_num + 1
        return result_num

    def step_to(self, maze, direction, set_visited=True):
        if direction == Cell.right:
            if self.pos_y + 1 == maze.size - 1 or maze.cell_array[self.pos_x][self.pos_y + 2].value == Maze.visited:
                return False, self
            else:
                step_cell = maze.set_visited(self.pos_x, self.pos_y + 1, set_visited)
                return True, step_cell
        elif direction == Cell.bottom:
            if self.pos_x + 1 == maze.size - 1 or maze.cell_array[self.pos_x + 2][self.pos_y].value == Maze.visited:
                return False, self
            else:
                step_cell = maze.set_visited(self.pos_x + 1, self.pos_y, set_visited)
                return True, step_cell
        elif direction == Cell.left:
            if self.pos_y - 1 == 0 or maze.cell_array[self.pos_x][self.pos_y - 2].value == Maze.visited:
                return False, self
            else:
                step_cell = maze.set_visited(self.pos_x, self.pos_y - 1, set_visited)
                return True, step_cell
        elif direction == Cell.top:
            if self.pos_x - 1 == 0 or maze.cell_array[self.pos_x - 2][self.pos_y].value == Maze.visited:
                return False, self
            else:
                step_cell = maze.set_visited(self.pos_x - 1, self.pos_y, set_visited)
                return True, step_cell


class Maze:
    visited = 0
    empty = 1

    def __init__(self, size, ):
        self.size = size
        self.cell_array = [[Cell(num_x, num_y, Maze.empty) for num_x in range(0, size)] for num_y in range(0, size)]
        self.start_point = Cell(0, 0, Maze.empty)

    def print_maze(self):
        for num_x in range(0, self.size):
            for num_y in range(0, self.size):
                print(str(self.cell_array[num_x][num_y].value) + " ", end="")
            print()

    def set_visited(self, pos_x, pos_y, is_set_visited = True):
        cell_visited = Cell(pos_x, pos_y, Maze.visited)
        if is_set_visited:
            self.cell_array[pos_x][pos_y] = cell_visited
        return cell_visited

    def set_start(self, start_x, start_y):
        self.start_point = Cell(start_x, start_y, Maze.visited)
        self.set_visited(start_x, start_y)


def spiralize(size):
    # Make a snake
    maze = Maze(size)
    maze.set_start(1, 0)
    maze_current_point = maze.start_point.step_to(maze, Cell.right)[1]
    is_dead_end = True
    directions_index = 0
    step_result = True, maze_current_point
    direction_changed = False

    while is_dead_end:
        #maze.print_maze()
        #print(
            # f"directions_index={directions_index} {Cell.directions[directions_index]} cell={step_result[1].print_cell()} res={step_result[0]} "
            # f"maze_cp={maze_current_point.print_cell()}")
        if step_result[0]:
            step_result = maze_current_point.step_to(maze, Cell.directions[directions_index])
            maze_current_point = step_result[1]
            if direction_changed and not step_result[0]:
                is_dead_end = False
            else:
                direction_changed = False
        else:
            directions_index = maze_current_point.change_direction(directions_index)
            more_than_one = maze_current_point.step_to(maze, Cell.directions[directions_index], False)[1].neighbors_num(maze)
            if more_than_one > 2:
                is_dead_end = False
            else:
                step_result = True, step_result[1]
                direction_changed = True

    maze.print_maze()
    res = [[maze.cell_array[num_y][num_x].value for num_x in range(0, size)] for num_y in range(0, size)]
    return res

#1,2,3,5,7,9
#4,6,8

print(spiralize(17))

# 0000000000
# .........0
# 00000000.0
# 0......0.0
# 0.0000.0.0
# 0.0..0.0.0
# 0.0....0.0
# 0.000000.0
# 0........0
# 0000000000

# 00000
# ....0
# 000.0
# 0...0
# 00000


# assert spiralize(5) == [[1, 1, 1, 1, 1],
#                         [0, 0, 0, 0, 1],
#                         [1, 1, 1, 0, 1],
#                         [1, 0, 0, 0, 1],
#                         [1, 1, 1, 1, 1]]
# assert spiralize(8) == [[1, 1, 1, 1, 1, 1, 1, 1],
#                         [0, 0, 0, 0, 0, 0, 0, 1],
#                         [1, 1, 1, 1, 1, 1, 0, 1],
#                         [1, 0, 0, 0, 0, 1, 0, 1],
#                         [1, 0, 1, 0, 0, 1, 0, 1],
#                         [1, 0, 1, 1, 1, 1, 0, 1],
#                         [1, 0, 0, 0, 0, 0, 0, 1],
#                         [1, 1, 1, 1, 1, 1, 1, 1]]
