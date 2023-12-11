class Ship:
    def __init__(self, size, cells):
        self.size = size
        self.cells = cells

    def print_ship(self):
        print_list = "".join([cell.print_cell() for cell in self.cells])
        return f"[S={self.size} {print_list}]"


class Cell:
    left, right, top, bottom = "left", "right", "top", "bottom"

    def __init__(self, pos_x, pos_y, value):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.value = value

    def step_to(self, direction, maze):
        if direction == Cell.top:
            if self.pos_y == 0:
                return False, self
            else:
                return True, maze.cell_array[self.pos_y - 1][self.pos_x]
        if direction == Cell.bottom:
            if self.pos_y + 1 > maze.size - 1:
                return False, self
            else:
                return True, maze.cell_array[self.pos_y + 1][self.pos_x]
        if direction == Cell.left:
            if self.pos_x == 0:
                return False, self
            else:
                return True, maze.cell_array[self.pos_y][self.pos_x - 1]
        if direction == Cell.right:
            if self.pos_x + 1 > maze.size - 1:
                return False, self
            else:
                return True, maze.cell_array[self.pos_y][self.pos_x + 1]

    def print_cell(self):
        return f"({self.pos_x},{self.pos_y}:{self.value})"

    def start_ship(self, max_ship_size, maze):
        ship_size = 0
        ship_cells = []
        ship_broken = False
        is_direction_defined = False
        ship_direction = None
        ship_other_direction = None
        current_cell = self
        while ship_size <= max_ship_size and not ship_broken:
            ship_size += 1
            ship_cells.append(current_cell)
            step_left = current_cell.step_to(Cell.left, maze)
            step_bottom = current_cell.step_to(Cell.bottom, maze)
            step_right = current_cell.step_to(Cell.right, maze)

            step_right_bottom = current_cell.step_to(Cell.right, maze)[1].step_to(Cell.bottom, maze)
            step_left_bottom = current_cell.step_to(Cell.bottom, maze)[1].step_to(Cell.left, maze)
            step_bottom_res = current_cell.step_to(Cell.bottom, maze)[0]
            step_right_res = current_cell.step_to(Cell.right, maze)[0]
            step_left_res = current_cell.step_to(Cell.left, maze)[0]
            # end of ship
            if ((step_right[1].value == Field.empty or not step_right_res)
                    and (step_bottom[1].value == Field.empty or not step_bottom_res)
                    and ((step_left_bottom[1].value == Field.empty or step_left_bottom[
                        1].value == Field.visited) or not step_left_res)
                    and (step_right_bottom[1].value == Field.empty or (not step_right_res and not step_bottom_res))):
                maze.set_visited(current_cell.pos_x, current_cell.pos_y, True)
                maze.set_visited(step_right[1].pos_x, step_right[1].pos_y, True)
                maze.set_visited(step_bottom[1].pos_x, step_bottom[1].pos_y, True)
                maze.set_visited(step_right_bottom[1].pos_x, step_right_bottom[1].pos_y, True)
                return True, ship_size, ship_cells

            # define direction
            if not is_direction_defined:
                if step_right[1].value == Field.ship and (step_bottom[1].value == Field.empty or not step_bottom[0]):
                    ship_direction = Cell.right
                    ship_other_direction = Cell.bottom
                    is_direction_defined = True
                if step_bottom[1].value == Field.ship and (step_right[1].value == Field.empty or not step_right[0]):
                    ship_direction = Cell.bottom
                    ship_other_direction = Cell.right
                    is_direction_defined = True
            # diagonal cell from ship
            if (step_right[0] and step_right[1].value == Field.ship) and \
                    (step_bottom[0] and step_bottom[1].value == Field.ship):
                return False, ship_size, ship_cells
            if step_right[0] and step_bottom[0] and step_right_bottom[1].value == Field.ship:
                return False, ship_size, ship_cells
            if (step_left[0] and step_bottom[0]) and step_left_bottom[1].value == Field.ship:
                return False, ship_size, ship_cells

            next_ship_cell = current_cell.step_to(ship_direction, maze)
            neighbor_cell = current_cell.step_to(ship_other_direction, maze)
            # wrong direction cell
            if neighbor_cell[0] and neighbor_cell[1].value == Field.ship:
                return False, ship_size, ship_cells
            # next ship cell
            maze.set_visited(current_cell.pos_x, current_cell.pos_y, True)
            if neighbor_cell is not None:
                maze.set_visited(neighbor_cell[1].pos_x, neighbor_cell[1].pos_y, True)
            current_cell = next_ship_cell[1]

        return True, ship_size, ship_cells


class Field:
    empty = 0
    ship = 1
    visited = 2

    def __init__(self, size, array):
        self.size = size
        self.cell_array = \
            [[Cell(num_x, num_y, array[num_y][num_x]) for num_x in range(0, size)] for num_y in range(0, size)]

    def set_visited(self, pos_x, pos_y, is_set_visited=True):
        cell_visited = Cell(pos_x, pos_y, Field.visited)
        if is_set_visited:
            self.cell_array[pos_y][pos_x] = cell_visited
        return cell_visited

    def print_maze(self):
        for num_x in range(0, self.size):
            for num_y in range(0, self.size):
                cell_printed = self.cell_array[num_x][num_y]
                print(str(cell_printed.value) + " ", end="")
            print()


def convert_ships_to_dic(ships):
    list_sizes = [ship.size for ship in ships]
    set_sizes = set(list_sizes)
    list_tuples = [(size, list_sizes.count(size)) for size in set_sizes]
    dict_sizes = dict(list_tuples)
    print(list_sizes)
    print(set(list_sizes))
    print(dict_sizes)
    return dict_sizes


def validate_battlefield(field):
    ship_config = {1: 4, 2: 3, 3: 2, 4: 1}
    max_ship_size = max(ship_config.keys())
    cell_field = Field(10, field)
    cell_field.print_maze()

    # iterate and find one-cell ships
    print("-----------------------------------------")
    ships = []
    validation_result = True
    for num_x in range(0, cell_field.size):
        for num_y in range(0, cell_field.size):
            current_cell = cell_field.cell_array[num_x][num_y]
            cell_field.set_visited(num_y, num_x, True)
            if current_cell.value == Field.ship:
                ship_calculation = current_cell.start_ship(max_ship_size, cell_field)
                if ship_calculation[0]:
                    ships.append(Ship(ship_calculation[1], ship_calculation[2]))
                else:
                    validation_result = False
            if not validation_result:
                return False
        print()

    print(f"SHIPS:>")
    for ship in ships:
        print(ship.print_ship())

    res_dict = convert_ships_to_dic(ships)

    # write your magic here
    return res_dict == ship_config


battleFieldSm = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

battleFieldSmForTestV1 \
    = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 1, 0, 1, 1, 0, 1, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 0, 0, 0, 1]]

battleFieldSmForTest \
    = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

battleFieldTs = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

battleFieldRndTs = [[0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 1, 1, 1, 0, 0, 1, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0]]

# maze_var = Field(10, battleFieldSmForTest)
# maze_var.set_visited(0, 0, True)
# maze_var.print_maze()

# FAILS on more than 1 last line ships
# FAILS on bottom left diagonal

# print(f"result={validate_battlefield(battleFieldSmForTestV1)}")
print(f"result={validate_battlefield(battleFieldRndTs)}")
# print(f"result={validate_battlefield(battleFieldSm)}")

# field = Field(10, battleFieldSmForTestV1)
# cell = Cell(1, 1, 0)
# field.print_maze()
# print(cell.step_to(Cell.right, field)[1].print_cell())
# print(cell.step_to(Cell.left, field)[1].print_cell())
# print(cell.step_to(Cell.top, field)[1].print_cell())
# print(cell.step_to(Cell.bottom, field)[1].print_cell())
