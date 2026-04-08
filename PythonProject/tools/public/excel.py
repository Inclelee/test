import openpyxl
import os

default_data_path = os.path.dirname(__file__) + '\\data\\data.xlsx'


def write_data(sheet, row, column, value):
    sheet.cell(row, column).value = value


def get_data(sheet, row, column):
    return sheet.cell(row, column).value

