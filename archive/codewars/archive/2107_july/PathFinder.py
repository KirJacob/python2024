class Cell:
    def __init__(self, tuple, value):
        self.tuple = tuple
        self.value = value

    def print_cell(self):
        return f"cell({self.tuple},{self.value})"

    def add_neighbors(self, result, cell_step):
        if cell_step.value != Maze.wall_char and cell_step.value != Maze.visited:
            result.append(cell_step)
        return result

    def find_neighbors(self, maze):
        result = []
        x_size = maze.size_x
        y_size = maze.size_y
        if self.tuple[0] < x_size - 1:
            result = Cell.add_neighbors(self, result, maze.get_cell(self.tuple[0] + 1, self.tuple[1]))
        if self.tuple[0] > 0:
            result = Cell.add_neighbors(self, result, maze.get_cell(self.tuple[0] - 1, self.tuple[1]))
        if self.tuple[1] < y_size - 1:
            result = Cell.add_neighbors(self, result, maze.get_cell(self.tuple[0], self.tuple[1] + 1))
        if self.tuple[1] > 0:
            result = Cell.add_neighbors(self, result, maze.get_cell(self.tuple[0], self.tuple[1] - 1))
        return result


class Maze:
    wall_char = 'W'
    empty_char = '.'
    visited = 'O'

    def __init__(self, arr_str):
        self.size_x = len(arr_str[0])
        self.size_y = len(arr_str)
        self.arr_str = arr_str
        self.cell_arr = []

    def print_maze(self):
        for num_x in range(0, len(self.cell_arr)):
            for num_y in range(0, len(self.cell_arr[num_x])):
                print(self.cell_arr[num_x][num_y].value, end='')
            print()

    def print_maze_detailed(self):
        for num_x in range(0, len(self.cell_arr)):
            for num_y in range(0, len(self.cell_arr[num_x])):
                print(self.cell_arr[num_x][num_y].print_cell())
        print()

    def load_lines(self):
        cell_arr_init = []
        for num in range(0, self.size_y):
            list_lines = list(self.arr_str[num])
            line_len = len(list_lines)
            list_cells = [Cell((num, line_num), list_lines[line_num]) for line_num in range(0, line_len)]
            cell_arr_init.append(list_cells)
        self.cell_arr = cell_arr_init

    def get_cell(self, x, y):
        return self.cell_arr[x][y]

    def set_visited(self, x, y):
        self.cell_arr[x][y].value = Maze.visited


def print_path(cell_list):
    result = ""
    for cell in cell_list:
        result = result + f"({cell.tuple[0]},{cell.tuple[1]})"
    return result


def path_finder_recursive(maze):
    def loop(list_paths, loop_maze):
        for path in list_paths:
            cell_active = path[len(path) - 1]
            neighbors = cell_active.find_neighbors(loop_maze)
            loop_maze.set_visited(cell_active.tuple[0], cell_active.tuple[1])
        return True

    maze_lines = maze.split("\n")
    maze_model = Maze(maze_lines)
    maze_model.load_lines()
    cell_start = Cell((0, 0), Maze.empty_char)
    cell_end = Cell((maze_model.size_x - 1, maze_model.size_y - 1), Maze.empty_char)
    exit_condition = True
    paths = [[cell_start]]
    loop(paths, maze_model)
    return True


def path_finder(maze):
    maze_lines = maze.split("\n")
    maze_model = Maze(maze_lines)
    maze_model.load_lines()
    cell_start = Cell((0, 0), Maze.empty_char)
    cell_end = Cell((maze_model.size_x - 1, maze_model.size_y - 1), Maze.empty_char)
    exit_condition = True
    paths = [[cell_start]]
    while exit_condition:
        result = []
        empty_neighbors = True
        for path in paths:
            cell_active = path[len(path) - 1]
            neighbors = cell_active.find_neighbors(maze_model)
            maze_model.set_visited(cell_active.tuple[0], cell_active.tuple[1])
            for neighbor in neighbors:
                path_temp = path.copy()
                path_temp.append(neighbor)
                result.append(path_temp)
                if neighbor is not None:
                    empty_neighbors = False
            if cell_active.tuple[0] == cell_end.tuple[1] and cell_active.tuple[1] == cell_end.tuple[1]:
                exit_condition = False
        if exit_condition and empty_neighbors:
            return False
        paths = result
        maze_model.print_maze()
    return True


a_true = "\n".join([
    ".W...",
    ".W...",
    ".W.W.",
    "...W.",
    "...W."])

a_false = "\n".join([
    "..W",
    ".W.",
    "W.."])

a_false2 = "\n".join([
    ".W...",
    ".W...",
    ".W.W.",
    "...WW",
    "...W."])

a_false3 = "\n".join([
    "..W.W..........",
    ".W.W....W.WW.WW",
    "W..W.W...W..W..",
    "W.....W.....WW.",
    "..........W....",
    "....W....W.....",
    ".W...."
])

# recursive solution - loop(), list(list(cell(0,0)))

print(f"PATH_FINDER={path_finder(a_false3)}")
