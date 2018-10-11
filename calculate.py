import pandas as pd


def count_cells(sheet, search_for):
    num_occurances = 0
    for name, col in sheet.items():
        for cell in col:
            if cell == search_for:
                num_occurances += 1
    return num_occurances


s = pd.read_csv('./data/FL_insurance_sample.csv')
# s = pd.read_csv('./data/simple_data.csv')
thing_to_search = 0
print("Number of '{0}'s in sheet: {1}".format(
    thing_to_search, count_cells(s, thing_to_search)))
