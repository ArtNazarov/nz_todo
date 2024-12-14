import curses
from lib_nz_model import load_full_model, extract_table_projects_from_model
from lib_nz_config_attributes import attributes_of_project


class Drawer:
    def __init__(self, output):

        self.start_x = 0
        self.start_y = 0
        self.started_index = 0
        self.started_column = 0
        self.selected_column = 0
        self.selected_row = 0
        self.lines_per_window = 0
        self.columns_per_window = 0
        self.width = 0

        self.o = output
        self.set_selected_row(0)
        self.set_lines_per_window(20)
        self.set_column_per_window(10)
        self.set_width(10)

    def set_selected_row(self, selected_row):
        self.selected_row = selected_row

    def set_selected_column(self, selected_column):
        self.selected_column = selected_column

    def set_lines_per_window(self, lines_per_window):
        self.lines_per_window = lines_per_window

    def set_column_per_window(self, columns_per_window):
        self.columns_per_window = columns_per_window

    def set_width(self, width):
        self.width = width

    def render(self, data):
        """
        Отображает lines_per_window строк начиная с позиции экрана start_x строки и start_y столбца
        из списка списков data. Начальный отображаемый индекс данных в первой строке - started_index (сдвиг)
        """
        for i in range(self.started_index, min(self.started_index + self.lines_per_window, len(data))):
            for j in range(self.started_column, min(len(data[i]), self.started_column + self.columns_per_window)):
                if j >= len(data[0]):
                    continue
                if j < 0:
                    continue

                if i == self.selected_row and j == self.selected_column:
                    self.o.addstr(self.start_y + (i - self.started_index),
                                  self.start_x + (j - self.started_column) * self.width, f"[{data[i][j]}]", curses.A_REVERSE)
                else:
                    self.o.addstr(self.start_y + (i - self.started_index),
                                  self.start_x + (j - self.started_column) * self.width, data[i][j])

class GenerateData:

    def __init__(self, col_count=100, row_count=100):
        self.col_count = col_count
        self.row_count = row_count

    def get_matrix(self):
        lst = []
        for i in range(self.row_count):
            row = []
            for j in range(self.col_count):
                row.append(f"Item {i} {j}")
            lst.append(row)
        return lst

class UserInterface:
    def __init__(self, data, output):
        self.data = data
        self.ui = Drawer(output)
        self.max_columns = len(data[0])
        self.max_rows = len(data)

    def event_loop(self):
        curses.curs_set(0)  # Hide cursor
        self.ui.o.nodelay(1)   # Non-blocking input
        height, width = self.ui.o.getmaxyx()
        needRedraw = True
        while True:
            if needRedraw:
                self.ui.o.clear()
                self.ui.render(self.data)
                self.ui.o.refresh()
                needRedraw = False

            key = self.ui.o.getch()

            # scrolling left-right
            if key == curses.KEY_LEFT and self.ui.selected_column > 0:
                self.ui.selected_column -= 1
                if self.ui.selected_column < self.ui.started_column and self.ui.started_column > 0:
                    self.ui.started_column -= 1
                needRedraw = True
            elif key == curses.KEY_RIGHT and self.ui.selected_column < self.max_columns - 1:
                self.ui.selected_column += 1
                if self.ui.selected_column > (max(self.max_columns-1, self.ui.started_column+self.ui.columns_per_window)) and self.ui.started_column < (self.max_columns - 1):
                    self.ui.started_column += 1
                needRedraw = True
            # scrolling up-down
            elif key == curses.KEY_UP and self.ui.selected_row > 0:
                self.ui.selected_row -= 1
                if self.ui.selected_row < self.ui.started_index:  # Scroll up
                    self.ui.started_index -= 1
                    if self.ui.started_index < 0:
                        self.ui.started_index = 0
                needRedraw = True
            elif key == curses.KEY_DOWN and self.ui.selected_row < len(self.data) - 1:
                self.ui.selected_row += 1
                if self.ui.selected_row >= self.ui.started_index + 10:  # Scroll down
                    self.ui.started_index += 1
                    # Prevent going out of bounds
                    if self.ui.started_index >= len(self.data) - 10:
                        self.ui.started_index = len(
                            self.data) - 10 if len(self.data) > 10 else len(self.data) - 1
                needRedraw = True
            elif key == ord('q'):  # Quit on 'q'
                break


def run_app(cs, data):

    def main(stdscr):
        ui = UserInterface(data, stdscr)
        # Получение максимальных размеров окна
        max_y, max_x = stdscr.getmaxyx()
        ui.ui.set_width(max_x // min(3, len(data[0])))
        ui.event_loop()

    cs.wrapper(main)


def exampleApp():
    data_generator = GenerateData()
    data = data_generator.get_matrix()
    run_app(curses, data)

   
def scroll_mode_projects():
    model = load_full_model()
    # print(model)
    # k = input('press enter')
    data = extract_table_projects_from_model(model, attributes_of_project())
    data.insert(0, attributes_of_project())
    run_app(curses, data)
