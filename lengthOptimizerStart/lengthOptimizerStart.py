from xlrd import open_workbook
import xlwt
from BasicClasses import *

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

    container_list = [BeamContainer(6000)]

    for beam in beam_list:
        if isinstance(beam, BeamSegment):
            added_to_container = False
            for container in container_list:
                if isinstance(container, BeamContainer):
                    if container.add_segment(beam):
                        added_to_container = True
                        break
            if added_to_container:
                continue
            print("no container can hold current element, creating new container instance")
            new_container = BeamContainer(6000)
            new_container.add_segment(beam)
            container_list.append(new_container)
            added_to_container = True

    print(len(container_list))

    output_wb = xlwt.Workbook("utf-8")
    out_sheet = output_wb.add_sheet("sheet1")

    row = 0
    for container in container_list:
        out_sheet.write(row, 0, str(container.get_length()))
        col = 1
        for seg in container.beamSegments:
            if isinstance(seg, BeamSegment):
                out_sheet.write(row, col, str(seg.get_length()))
                col += 1
        row += 1

    output_wb.save("out.xls")
