import os
import shutil
import time

def os_clear_screen(printText=''):
    os.system('cls' if os.name == 'nt' else 'clear')
    if printText != '':
        print(printText)

def os_delay(seconds):
    time.sleep(seconds)

def os_delete_directory(directoryPath):
    shutil.rmtree(directoryPath)

def os_delete_file(filePath):
    os.remove(filePath)

def os_get_date_time(mode='')
    dateTimeData = datetime.datetime.now()
    if mode == '':
        return dateTimeData
    else:
        dateTimeData = dateTimeData.strftime(f'{mode}')

def os_read_file(filePath):
    fileData = open(filePath, 'r', encoding="utf-8")
    try:
        data = fileData.read()
        fileData.close()
        return data
    except:
        return 'null'

def os_write_file(filePath, fileData, writingMode='w'):
    with open(filePath, writingMode, encoding="utf-8")as file:
        file.write(fileData)
        file.close()
