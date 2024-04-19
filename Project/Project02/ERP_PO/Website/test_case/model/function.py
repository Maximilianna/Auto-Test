import csv


# 截图方法
def get_screenshot(driver, filename):
    path = f"D:\\Code\\PyCharm\\Auto_Test04\\ERP_PO\\Website\\test_report\\screenshots\\{filename}.png"
    driver.get_screenshot_as_file(path)


# 数据驱动
def get_csv_data():
    List = []
    stream = open(f"D:\\Code\\PyCharm\\Auto_Test04\\ERP_PO\\Website\\test_data\\test_csv.csv")
    reader = csv.reader(stream)
    for now in reader:
        List.append(now)
    return List
