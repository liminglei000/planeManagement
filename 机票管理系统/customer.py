'''
2020.0304  0313 0315
@author: lml
'''

from Class import CUSTOMER, Reserve, Ticket

class Customer:
    def __init__(self, account, password):
        # self.name = name
        self.account = account
        self.password = password
        # self.email = email
        # self.had = had
        # self.reserved = reserved

    
    # 机票（航班）查询
    def query(self):
        print('------------机票查询-------------')
        data = []  # 文件中的数据存放之处
        Data = []  # 按城市查找时符合条件的先存到这里
        file = open(".vscode\\keshe\\tickets.txt", "r", encoding='utf-8')
        file.readline()   # readline进行读文件时第一行是数据表中的列，可以将文件移到第二行开始处
        for line in file:  # 实现了将文件信息全部读入列表data中，列表中的一个元素即是一个对象（在这里是机票对象）
            if line != '\n':
                lines = line.strip('\n').split(" ")
                # print(lines)
                obj = Ticket(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], lines[6], lines[7], lines[8], lines[9], lines[10], lines[11])
                data.append(obj)
        # Print(data)
        Data.append(data[0])
        
        a = int(input('输入查询条件：1、两城市间航班情况  2、指定航班号航班情况 ->> '))
        while((a != 1) and (a != 2)):
            a = input('请重新输入查询条件：>> ')
        if(a == 1): ############## 若两城市之间无直飞航班，设计算法提供转机航班 这个先不做了555
            b = input('输入起始城市->> ') 
            c = input('输入终点城市->> ')
            for i in range(0, len(data)):
                if ((data[i].takeoff_place == b) and (data[i].land_place == c)):
                    Data.append(data[i])
            # for x in Data:
            #     Print(x)
            if len(Data) > 1:
                print('-------------排序输出--------------')
                recommend(Data)
        else: ########### 有待补充其他查询条件
            d = input('输入航班号->> ')
            for x in data:
                if(x.id == d):
                    Print(x)
                    break
        ############### 按其他查询条件查完后还应当进行排序操作
        

    # 机票购买
    def buy(self):
        print('-------------机票购买-------------')
        data = []
        ticket_id = input('请输入航班号： ')
        file = open(".vscode\\keshe\\tickets.txt", "r", encoding='utf-8')
        file.readline()
        for line in file:
            if line != '\n':
                lines = line.strip('\n').split(" ")
                # print(lines)
                obj = Ticket(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], lines[6], lines[7], lines[8], lines[9], lines[10], lines[11])
                data.append(obj)
        for x in data:
            if x.id == ticket_id:
                if int(x.number) > 0:
                    x.number = int(x.number) - 1
                    break
                else:
                    return ticket_id
        # print(data[0].number)
        file.close()

        # for x in data:
        #     # Print(x)
        #     x = x.id + ' ' + x.company_name + ' ' + x.takeoff_time + ' ' + x.takeoff_place + ' ' + x.land_time + ' ' + x.land_place + ' ' + str(x.number)
        #     # print(x)
        file = open(".vscode\\keshe\\tickets.txt", "w", encoding='utf-8')
        file.write('航班编号 航空公司名称 起飞时间 起飞地点 降落时间 降落地点 余票 票价 经停站1名称 到达经停站1时间 经停站2名称 到达经停站2时间\n')
        for x in data:
            # 你要把那一大长串字符串作为一次一行的输入，所以要加括号。
            file.write('%s\n' %(x.id + ' ' + x.company_name + ' ' + x.takeoff_time + ' ' + x.takeoff_place + ' ' + x.land_time + ' ' + x.land_place + ' ' + str(x.number)
                                 + ' ' +  x.price + ' ' + x.stop1_place + ' ' + x.stop1_time + ' ' + x.stop2_place + ' ' + x.stop2_time))
        print('机票购买成功！')
        file.close()
        
        # 在用户数据库中把他刚刚买的票给添上
        data = []
        file = open(".vscode\\keshe\\customers.txt", "r", encoding='utf-8')
        file.readline()
        for line in file:
            if line != '\n':
                lines = line.strip('\n').split(' ')
                obj = CUSTOMER(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5])
                data.append(obj)
        file.close()
        # 应该再找出是谁要进行购买，也就是当前的操作对象是谁。
        for x in data:
            if x.account == self.account:
                x.had = ticket_id
                break
        file = open(".vscode\\keshe\\customers.txt", "w", encoding='utf-8')
        file.write('姓名 账号 密码 邮箱 已到手的机票 已预订的机票\n')
        for x in data:
            file.write('%s\n' %(x.name + ' ' + x.account + ' ' + x.password + ' ' + x.email + ' ' + x.had + ' ' + x.reserved))

        return 0


    # 机票预订
    def reserve(self):
        print('------------机票预订-------------')
        data = []
        ticket_id = input('请输入航班号： ')
        file = open(".vscode\\keshe\\customers.txt", "r", encoding='utf-8')
        file.readline()
        for line in file:
            if line != '\n':
                lines = line.strip('\n').split(' ')
                obj = CUSTOMER(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5])
                data.append(obj)
        file.close()
        # 应该再找出是谁要进行预订，也就是当前的操作对象是谁。
        for x in data:
            if x.account == self.account:
                x.reserved = ticket_id
                break
        file = open(".vscode\\keshe\\customers.txt", "w", encoding='utf-8')
        file.write('姓名 账号 密码 邮箱 已到手的机票 已预订的机票\n')
        for x in data:
            file.write('%s\n' %(x.name + ' ' + x.account + ' ' + x.password + ' ' + x.email + ' ' + x.had + ' ' + x.reserved))
        file.close()

        # ===================================================
        # 预订最后还要进入等待文件队列里去
        data = []
        file = open(".vscode\\keshe\\reserve.txt", "r", encoding="utf-8")
        file.readline()
        for line in file:
            if line != '\n':
                data.append(line)
        file.close()
        data.append(self.account + ' ' + ticket_id)
        file = open(".vscode\\keshe\\reserve.txt", "w", encoding='utf-8')
        file.write('用户账号 航班编号\n')
        for x in data:
            file.write('%s\n' %x)

        print('机票预订成功！')


    # 如果客户在进行买的操作时，想要买的机票没了，并且同意预订的话，此函数使得顾客不必再重新输入航班号
    # 正式转正 2333333
    def Reserve(self, ticket_id):
        print('------------机票预订-------------')
        data = []
        file = open(".vscode\\keshe\\customers.txt", "r", encoding='utf-8')
        file.readline()
        for line in file:
            if line != '\n':
                lines = line.strip('\n').split(' ')
                obj = CUSTOMER(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5])
                data.append(obj)
        file.close()
        # 应该再找出是谁要进行预订，也就是当前的操作对象是谁。
        for x in data:
            if x.account == self.account:
                x.reserved = ticket_id
                break
        file = open(".vscode\\keshe\\customers.txt", "w", encoding='utf-8')
        file.write('姓名 账号 密码 邮箱 已到手的机票 已预订的机票\n')
        for x in data:
            file.write('%s\n' %(x.name + ' ' + x.account + ' ' + x.password + ' ' + x.email + ' ' + x.had + ' ' + x.reserved))
        file.close()

        data = []
        file = open(".vscode\\keshe\\reserve.txt", "r", encoding="utf-8")
        file.readline()
        for line in file:
            if line != '\n':
                data.append(line)
        file.close()
        data.append(self.account + ' ' + ticket_id)
        file = open(".vscode\\keshe\\reserve.txt", "w", encoding='utf-8')
        file.write('用户账号 航班编号\n')
        for x in data:
            file.write('%s\n' %x)

        print('机票预订成功！')


    # 机票退订
    def cancel(self):
        print('------------机票退订-------------')
        data = []
        # 现在其实不管输不输航班号或者是输哪个航班号都没用，因为函数一执行就直接将该用户已购买的航班全删了，还没用考虑一个人购买多张机票的情况
        # ticket_id = input('请输入航班号： ') 
        ticket_id = ''
        file = open(".vscode\\keshe\\customers.txt", "r", encoding='utf-8')
        file.readline()
        for line in file:
            if line != '\n':
                lines = line.strip('\n').split(' ')
                obj = CUSTOMER(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5])
                data.append(obj)
        file.close()
        # 应该再找出是谁要进行退订，也就是当前的操作对象是谁。
        for x in data:
            if x.account == self.account:
                if x.had == '0':
                    print('您并没有购买任何机票')
                    return
                else:
                    ticket_id = x.had
                    x.had = '0'
                break
        file = open(".vscode\\keshe\\customers.txt", "w", encoding='utf-8')
        file.write('姓名 账号 密码 邮箱 已到手的机票 已预订的机票\n')
        for x in data:
            file.write('%s\n' %(x.name + ' ' + x.account + ' ' + x.password + ' ' + x.email + ' ' + x.had + ' ' + x.reserved))
        print('机票退订成功！')

        # ==================================================           
        # 机票退订之后应该直接让正在预订该航班的人按先后顺序接手
        data = []
        Account = ''  # 存着应该被让与票的客户账号
        file = open(".vscode\\keshe\\reserve.txt", "r", encoding="utf-8")
        file.readline()
        for line in file:
            if line != '\n':
                lines = line.strip('\n').split(' ')
                obj = Reserve(lines[0],lines[1])
                data.append(obj)
        file.close()
        Data = []
        for i in range(0, len(data)):   ### 一定要注意了，Python中的for循环默认取不到后面的值，range(0,1):就只取0，  1取不到。
            if data[i].id == ticket_id:
                Account = data[i].account
                break

        for x in data:
            if x.account != Account:
                Data.append(x)
                
        data = Data
        # 1.取消预订文件中的其他相关信息重新写入  
        file = open(".vscode\\keshe\\reserve.txt", "w", encoding='utf-8')
        file.write('用户账号 航班编号\n')
        for x in data:
            file.write('%s\n' %(x.account + ' ' + x.id))
        file.close()
        # 2.给所从预订人员中选出的进行预订抢票=>正式购买操作（顾客文件客户预订信息进行修改）   
        data = []
        file = open(".vscode\\keshe\\customers.txt", "r", encoding='utf-8')
        file.readline()
        for line in file:
            if line != '\n':
                lines = line.strip('\n').split(' ')
                obj = CUSTOMER(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5])
                data.append(obj)
        file.close()
        # 应该再找出是谁要进行预订，也就是当前的操作对象是谁。
        flag = False
        for x in data:
            if x.account == Account:
                x.had = x.reserved
                x.reserved = '0'
                flag = True
                break
        if flag == True:
            file = open(".vscode\\keshe\\customers.txt", "w", encoding='utf-8')
            file.write('姓名 账号 密码 邮箱 已到手的机票 已预订的机票\n')
            for x in data:
                file.write('%s\n' %(x.name + ' ' + x.account + ' ' + x.password + ' ' + x.email + ' ' + x.had + ' ' + x.reserved))
            file.close()
            print('管理端信息：您退订的机票已成功转让给最早预订该机票的客户了！')
        # =================================================
    

# 用户登录
def load():
    flag = False  
    account = input('账号： ')
    password = input('密码： ')
    file = open(".vscode\\keshe\\customers.txt", "r", encoding='utf-8')
    file.readline()
    for line in file:  # 只要提示下标越界肯定就是没去掉空行
        if line != '\n':
            lines = line.strip('\n').split(" ")
            # print(lines)
            if( (account == lines[1]) and (password == lines[2]) ):
                flag = True
    if(flag == False):
        print('登录失败，请重新登录')
        print('* * * * * * 重新登录 * * * * * * *')
        return load()
    else:
        print('登录成功！')
        return Customer(account,password)

# 新用户注册
def regist():
    data = []
    name = input('姓名： ')
    account = input('账号： ')
    password = input('密码： ')
    email = input('邮箱： ')
    file = open(".vscode\\keshe\\customers.txt", "r", encoding='utf-8')
    file.readline()
    for line in file:
        if line != '\n':
            data.append(line)
    file.close()
    # print(len(data))
    data.append(name + ' ' + account + ' ' + password + ' ' + email + ' ' + '0' + ' ' + '0')  # 放到这里是为了在文件最后添加信息
    file = open(".vscode\\keshe\\customers.txt", "w", encoding='utf-8')
    file.write('姓名 账号 密码 邮箱 已到手的机票 已预订的机票\n')
    for line in data:
        file.write('%s\n' %line)
    print('注册成功！请继续登录 ~ ')

# 将时间从字符串格式转到适合的格式
def time_trans(time):
    month = int(time[0:2])
    day = int(time[2:4])
    hour = (time[4:6])
    minute = (time[6:])
    Time = [month, day, hour, minute]
    return Time
    
# 打印机票（航班）信息函数
def Print(args):
    print('-------------------------------------------')
    print('|  航班编号    ：%s'  %args.id)
    print('|  航空公司名称：%s'  %args.company_name)
    print('|  起飞时间    ：%d月%d日 %s:%s'   %( time_trans(args.takeoff_time)[0], time_trans(args.takeoff_time)[1], time_trans(args.takeoff_time)[2], time_trans(args.takeoff_time)[3]))
    print('|  起飞地点    ：%s'  %args.takeoff_place)
    print('|  降落时间    ：%d月%d日 %s:%s'   %( time_trans(args.land_time)[0], time_trans(args.land_time)[1], time_trans(args.land_time)[2], time_trans(args.land_time)[3]))
    print('|  降落地点    ：%s'  %args.land_place)
    if args.stop1_place != '0':
        print('|  经停地点1   ：%s'  %args.stop1_place)
        print('|  经停时间1   ：%d月%d日 %s:%s'   %( time_trans(args.stop1_time)[0], time_trans(args.stop1_time)[1], time_trans(args.stop1_time)[2], time_trans(args.stop1_time)[3]))
    if args.stop2_place != '0':
        print('|  经停地点2   ：%s'  %args.stop2_place)
        print('|  经停时间2   ：%d月%d日 %s:%s'   %( time_trans(args.stop2_time)[0], time_trans(args.stop2_time)[1], time_trans(args.stop2_time)[2], time_trans(args.stop2_time)[3]))
    print('|  剩余机票    ：%s'  %args.number)
    print('|  机票票价    ：%s'  %args.price)
    print('--------------------------------------------')


# 牵扯到按对象的某属性对对象进行排序的问题了，归并排序的优化算法给出了思路
# 航班推荐
def recommend(data):
    a = input('票务查询到多个信息，请输入排序依据：1.票价 2.飞行时间 3.余票数量： ')
    if a == '1':
        sort_price(data)
    elif a == '2':
        sort_time(data)
    elif a == '3':
        sort_number(data)
    else:
        print('----------重新输入----------')
        recommend(data)
    # 按照link数组下标的提示打印data

# 查询结果价格排序函数
def sort_price(data):
    link = [i for i in range(0, len(data))]
    low = 1; high = len(data) - 1
    p = merge_sort1_price(data, link, low, high)
    while p != 0:
        Print(data[p])
        p = link[p]

def insert_sort_price(data, link, low, high):
    link[low] = 0; temp = low; p = low
    for j in range(low+1, high+1): 
        k = p
        if data[j].price <= data[p].price:
            link[j] = p; p = j
        while (data[j].price > data[k].price and (k != temp)) :
            if data[j].price > data[link[k]].price:
                k = link[k]
            else:
                r = link[k]; link[k] = j; link[j] = r
                k = r
        if data[j].price > data[temp].price:
            link[temp] = j; link[j] = 0; temp = j
    return p

def merge_sort1_price(data, link, low, high):
    if high - low + 1 < 6:
        return insert_sort_price(data, link, low, high)
    else:
        mid = (low + high) // 2
        q = merge_sort1_price(data, link, low, mid)
        r = merge_sort1_price(data, link, mid + 1, high)
        return merge1_price(data, link, q, r)

def merge1_price(data, link, q, r):
    i = q; j = r; k = 0
    while (i != 0) and (j != 0):
        if data[i].price <= data[j].price:
            link[k] = i; k = i; i = link[i]
        else:
            link[k] = j; k = j; j = link[j]
    if i == 0:
        link[k] = j
    else:
        link[k] = i
    p = link[0]
    return p
    
# 查询结果飞行时间排序函数(此时只用了优化的插入排序)
def sort_time(data):
    link = [i for i in range(0, len(data))]
    low = 1; high = len(data) - 1
    link[low] = 0; temp = low; p = low
    for j in range(low+1, high+1): 
        k = p
        if ((int(time_trans(data[j].land_time)[2]) - int(time_trans(data[j].takeoff_time)[2])) * 60 + (int(time_trans(data[j].land_time)[3]) - int(time_trans(data[j].takeoff_time)[3]))
        <= (int(time_trans(data[p].land_time)[2]) - int(time_trans(data[p].takeoff_time)[2])) * 60 + (int(time_trans(data[p].land_time)[3]) - int(time_trans(data[p].takeoff_time)[3]))):
            link[j] = p; p = j
        while ((int(time_trans(data[j].land_time)[2]) -int( time_trans(data[j].takeoff_time)[2])) * 60 + (int(time_trans(data[j].land_time)[3]) - int(time_trans(data[j].takeoff_time)[3])) 
        > (int(time_trans(data[k].land_time)[2]) - int(time_trans(data[k].takeoff_time)[2])) * 60 + (int(time_trans(data[k].land_time)[3]) - int(time_trans(data[k].takeoff_time)[3])) 
        and (k != temp)) :
            if ((int(time_trans(data[j].land_time)[2]) - int(time_trans(data[j].takeoff_time)[2])) * 60 + (int(time_trans(data[j].land_time)[3]) - int(time_trans(data[j].takeoff_time)[3])) 
            > (int(time_trans(data[link[k]].land_time)[2]) - int(time_trans(data[link[k]].takeoff_time)[2])) * 60 + (int(time_trans(data[link[k]].land_time)[3]) - int(time_trans(data[link[k]].takeoff_time)[3]))):
                k = link[k]
            else:
                r = link[k]; link[k] = j; link[j] = r
                k = r
        if ((int(time_trans(data[j].land_time)[2]) - int(time_trans(data[j].takeoff_time)[2])) * 60 + (int(time_trans(data[j].land_time)[3]) - int(time_trans(data[j].takeoff_time)[3])) 
        > (int(time_trans(data[temp].land_time)[2]) - int(time_trans(data[temp].takeoff_time)[2])) * 60 + (int(time_trans(data[temp].land_time)[3]) - int(time_trans(data[temp].takeoff_time)[3]))):
            link[temp] = j; link[j] = 0; temp = j
    while p != 0:
        Print(data[p])
        p = link[p]

# 查询结果余票数量排序函数
def sort_number(data):
    Data = []
    link = [i for i in range(0, len(data))]
    low = 1; high = len(data) - 1
    p = merge_sort1_number(data, link, low, high)
    while p != 0:
        Data.append(data[p])
        p = link[p]
    for i in range(len(Data)-1, -1, -1):
        Print(Data[i])

def insert_sort_number(data, link, low, high):
    link[low] = 0; temp = low; p = low
    for j in range(low+1, high+1): 
        k = p
        if data[j].number <= data[p].number:
            link[j] = p; p = j
        while (data[j].number > data[k].number and (k != temp)) :
            if data[j].number > data[link[k]].number:
                k = link[k]
            else:
                r = link[k]; link[k] = j; link[j] = r
                k = r
        if data[j].number > data[temp].number:
            link[temp] = j; link[j] = 0; temp = j
    return p

def merge_sort1_number(data, link, low, high):
    if high - low + 1 < 6:
        return insert_sort_number(data, link, low, high)
    else:
        mid = (low + high) // 2
        q = merge_sort1_number(data, link, low, mid)
        r = merge_sort1_number(data, link, mid + 1, high)
        return merge1_number(data, link, q, r)

def merge1_number(data, link, q, r):
    i = q; j = r; k = 0
    while (i != 0) and (j != 0):
        if data[i].number <= data[j].number:
            link[k] = i; k = i; i = link[i]
        else:
            link[k] = j; k = j; j = link[j]
    if i == 0:
        link[k] = j
    else:
        link[k] = i
    p = link[0]
    return p
    

'''''''''''''''''''''''''''''''''''
函数执行区
'''''''''''''''''''''''''''''''''''
############# 客户端主页面操作流程的问题

if __name__=="__main__":
    print('\n'); print('* * * * * * * * * 机票管理系统 * * * * * * * * *')
    a = input('请登录或注册：1、登录 2、注册 ->> ')
    if a == '1':
        customer01 = load()
    else:
        regist()
        customer01 = load()
    while(1):
        print('\n'); print('--------------------------------------------------------------------')
        behavior = input('选择后续操作：1.航班查询  2.机票购买  3.预约机票  4.退订机票 ===> '); print()
        if behavior == '1':
            customer01.query()
        elif behavior == '2':
            ticket_id = customer01.buy()
            if ticket_id != 0:
                b = int(input('票已经被抢够完，是否去预约抢票：1、预约抢票  2、离开 ->> '))
                if b == 1:
                    customer01.Reserve(ticket_id)
        elif behavior == '3':
            # 才发现预约抢票不是一个单独的功能来，它是与买票耦合的，即：只有当买票没买到后才能预约抢票啥的。
            customer01.reserve()
        elif behavior == '4':
            customer01.cancel()
        else:
            print('输入有误.....')
            