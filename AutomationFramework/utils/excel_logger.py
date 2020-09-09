import openpyxl
import os


class ExcelLogger:
    workbook_path = None
    workbook_name = None
    workbook_columns = None
    workbook = None
    sheet = None
    log_values = {}
    column_indexes = {}

    # logger = ExcelLogger(workbook_name='/excel_logs/existe.xlsx', columns=['jaja', 'sapo perro'])
    def __init__(self, workbook_name, columns):
        self.log_values = {}
        self.column_indexes = {}
        self.workbook_path = os.path.dirname(os.path.realpath(__file__)).replace('/utils', '') + workbook_name
        self.workbook_name = self.workbook_path.split('/')[-1]
        self.workbook_columns = columns

        try:
            self.workbook = openpyxl.load_workbook(self.workbook_path)
            self.sheet = self.workbook.active
        except:
            self.workbook = openpyxl.Workbook()
            self.sheet = self.workbook.active
            self.sheet.title = 'logs'
            for column in range(0, len(self.workbook_columns)):
                self.sheet.cell(row=1, column=column + 1, value=self.workbook_columns[column])

            # Tiene que ser en el write_log ???
            self.workbook.save(filename=self.workbook_path)

        self.set_column_indexes()
        self.clean_log_values()

        print('--------------------')
        print(self.workbook_path)
        print(self.workbook_name)
        print(self.workbook_columns)
        print(self.workbook)
        print(self.sheet)
        print(self.log_values)
        print(self.column_indexes)

    def set_column_indexes(self):
        for column in range(0, len(self.workbook_columns)):
            self.column_indexes[self.sheet.cell(row=1, column=column + 1).value] = column + 1

    def clean_log_values(self):
        for column in self.workbook_columns:
            self.log_values[column] = None

    def add_value_to_log_column(self, value, column):
        self.log_values[column] = value

    # TODO
    def write_log(self):
        self.clean_log_values()
