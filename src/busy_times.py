from datetime import datetime;


def subtract(value1, value2):
    return value1.toordinal() - value2.toordinal()


def solve(dates):
    zeroData = datetime.date(datetime(2018, 1, 1))
    list = [0] * 30
    accList = [0] * 30
    acc = 0

    for mydate in dates[2:]:
        data1 = datetime.date(datetime(int(mydate[:4]), int(mydate[6:7]), int(mydate[9:10])))
        data2 = datetime.date(datetime(int(mydate[11:15]), int(mydate[16:18]), int(mydate[19:21])))
        list[subtract(data1, zeroData)] = list[subtract(data1, zeroData)] + 1
        list[subtract(data2, zeroData) + 1] = list[subtract(data2, zeroData) + 1] - 1

    for number in range(len(list)):
        acc = acc + list[number]
        accList[number] = acc

    return datetime.fromordinal(zeroData.toordinal() + accList.index(max(accList))).date()
