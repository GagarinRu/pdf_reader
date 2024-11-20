import pdfplumber
import xlsxwriter

path_pdf = '4tokr.pdf'


def wrt_xlsx(table):
    workbook = xlsxwriter.Workbook('file.xlsx')
    worksheet = workbook.add_worksheet()
    for row, el in enumerate(table):
        for column, data in enumerate(el):
            worksheet.write(row, column, data)
    workbook.close()


def add_table(page, table):
    text = page.extract_text()
    task_indexs = text.count('Задача ')
    for index in range(task_indexs):
        task = (text.split('Задача ')[index+1]
                .replace('-\n', '').replace('\n', ' '))
        task_num = task.split('. ', 1)[0]
        task_null = task.split('. ', 1)[1]
        if task_null[0] != '(':
            table.append([task_num, task_null])
        else:
            task = task.split(')', 1)[1].rsplit('.', 1)[0]
            table.append([task_num, task+'.'])


def rezult(pdf):
    table = [['№ Задачи', 'Задача'],]
    with pdfplumber.open(pdf) as pdf:
        count_page = len(pdf.pages)
        for value in range(count_page):
            page = pdf.pages[value]
            add_table(page, table)
        wrt_xlsx(table)


if __name__ == '__main__':
    rezult(path_pdf)
