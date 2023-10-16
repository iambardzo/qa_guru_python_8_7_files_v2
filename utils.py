import os


PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
RESOURCES_PATH = os.path.join(PROJECT_ROOT_PATH, 'resources')
TMP_PATH = os.path.join(PROJECT_ROOT_PATH, 'tmp')
ZIP_PATH = os.path.join(TMP_PATH, 'archive.zip')

PDF_FILE = 'HelloPDF.pdf'
TXT_FILE = 'TextDocument.txt'
XLS_FILE = 'xlsExcel.xls'
XLSX_FILE = 'xlsxExcel.xlsx'