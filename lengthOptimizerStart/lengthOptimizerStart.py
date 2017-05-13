from xlrd import open_workbook
from BasicClasses.Beam import *

if __name__ == "__main__":

    excel_file_name = "input/thermowood.xlsx"

    wb = open_workbook(excel_file_name)
    sh = wb.sheet_by_index(0)

    beam_list = []

    for row_index in range(sh.nrows):
        length = sh.cell(row_index, 0).value
        try:
            float(length)
            num = int(sh.cell(row_index, 1).value)
            for i in range(num):
                beam = BeamSegment(length)
                beam_list.append(beam)
        except ValueError:
            continue

    print("Number of beams:" + str(len(beam_list)))
    beam_list.sort(key=lambda x: x.get_length(), reverse=True)

    for beam in beam_list:
        print(beam.get_length())



    
        

