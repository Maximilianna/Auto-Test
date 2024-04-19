import csv


def get_screenshot(driver,filename):
    driver.get_screenshot_as_file(f"D:\\Code\\PyCharm\\Auto_Test03\\ERP_PO\\Website\\test_report\\srceenshot\\{filename}.png")

def get_csv_data():
    stream = open("D:/Code/Pycharm/Auto_Test03/ERP_PO/Website/test_data/test_csv.csv")
    reader = csv.reader(stream)
    list = []
    for row in reader:
        list.append(row)
    return list
