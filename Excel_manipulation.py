import openpyxl
import os
os.chdir('C://Users//George//python_scripts//Scripts//DataScience Projects')

workbook = openpyxl.load_workbook('survey_results_public.xlsx')
sheet = workbook.get_sheet_by_name('survey_results_public')

for i in range(2, 10):
    sheet['G' + str(i)].value
