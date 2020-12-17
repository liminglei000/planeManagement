
class CUSTOMER:  # 该类仅作为数据存储结构（类实例化对象后的容器作用）使用；方便读写customers.txt文件到列表中
    def __init__(self, name, account, password, email, had, reserved):
        self.name = name
        self.account = account
        self.password = password
        self.email = email
        self.had = had
        self.reserved = reserved


class Reserve:  # 机票预订类，包括预订者的账户，以及机票的航班号
    def __init__(self, account, id):
        self.account = account
        self.id = id


class Ticket:  # 机票类，包括机票的各种信息
    def __init__(self, id, company_name, takeoff_time, takeoff_place, land_time, land_place, number, price, stop1_place, stop1_time, stop2_place, stop2_time):
        self.id = id
        self.company_name = company_name
        self.takeoff_time = takeoff_time
        self.takeoff_place = takeoff_place
        self.land_time = land_time
        self.land_place = land_place
        self.number = number
        self.price = price
        self.stop1_place = stop1_place
        self.stop1_time = stop1_time
        self.stop2_place = stop2_place
        self.stop2_time = stop2_time

class Infor:  # 通知类，用于存储所要通知者的姓名和邮箱，便于发消息通知
    def __init__(self, name, email):
        self.name = name
        self.email = email