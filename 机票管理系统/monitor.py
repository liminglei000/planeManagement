'''
2020.0306 0313 0315
@author: lml
'''

import smtplib
import datetime
from Class import CUSTOMER, Infor, Ticket
from email.mime.text import MIMEText
from email.utils import formataddr

class Monitor:
    def query(self):
        print('------------机票查询-------------')
        data = []  # 文件中的数据存放之处
        file = open(".vscode\\keshe\\tickets.txt", "r", encoding='utf-8')
        file.readline()   # readline进行读文件时第一行是数据表中的列，可以将文件移到第二行开始处
        for line in file:  # 实现了将文件信息全部读入列表data中，列表中的一个元素即是一个对象（在这里是机票对象）
            if line != '\n':
                lines = line.strip('\n').split(" ")
                # print(lines)
                obj = Ticket(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], lines[6], lines[7], lines[8], lines[9], lines[10], lines[11])
                data.append(obj)
        # Print(data)
        
        a = int(input('输入查询条件：1、两城市间航班情况  2、航班班号  3、航空公司名称->> '))
        while((a != 1) and (a != 2) and (a != 3)):
            a = input('请重新输入查询条件：>> ')
        if a == 1: ############## 若两城市之间无直飞航班，设计算法提供转机航班 这个先不做了555
            b = input('输入起始城市->> ') 
            c = input('输入终点城市->> ')
            for x in data:
                if ((x.takeoff_place == b) and (x.land_place == c)):
                    Print(x)
        elif a == 2: ########### 有待补充其他查询条件
            d = input('输入航班号->> ')
            for x in data:
                if(x.id == d):
                    Print(x)
                    break
        elif a == 3:
            d = input('输入航空公司名称 ->> ')
            for x in data:
                if(x.company_name == d):
                    Print(x)

    def add(self):
        print('-------------------增加航班------------------')
        data = []
        id = input('输入航班号 ：')
        name = input('输入航空公司名称：')
        takeoff_time = input('输入起飞时间：')
        takeoff_place = input('输入起飞地点：')
        land_time = input('输入降落时间：')
        land_place = input('输入降落地点：')
        number = input('输入余票数量：')
        price = input('输入机票价格：')
        stop1_place = input('输入第一个经停站：')
        stop1_time = input('输入第一次经停时间：')
        stop2_place = input('输入第二个经停站：')
        stop2_time = input('输入第二次经停时间：')
        file = open(".vscode\\keshe\\tickets.txt", "r", encoding='utf-8')
        file.readline()
        for line in file:
            if line != '\n':
                data.append(line)
        file.close()
        data.append(id + ' ' + name + ' ' + takeoff_time + ' ' + takeoff_place + ' ' + land_time + ' ' + land_place + ' ' + number
                     + ' ' + price + ' ' + stop1_place + ' ' + stop1_time + ' ' + stop2_place + ' ' + stop2_time)
        file = open(".vscode\\keshe\\tickets.txt", "w", encoding='utf-8')
        file.write('航班编号 航空公司名称 起飞时间 起飞地点 降落时间 降落地点 余票 票价 经停站1名称 到达经停站1时间 经停站2名称 到达经停站2时间\n')
        for line in data:
            file.write('%s\n' %line)
        print('航班添加成功！')

    def delete(self):  # 同时也是航班的取消操作吗 ????
        print('-------------------删除航班------------------')
        data = []; takeoff_place=''; land_place=''; takeoff_time=''; land_time=''
        Id = input('输入所要取消航班的班号：')
        file = open(".vscode\\keshe\\tickets.txt", "r", encoding='utf-8')
        file.readline()
        for line in file:
            if line != '\n':
                lines = line.strip('\n').split(' ')
                obj = Ticket(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], lines[6], lines[7], lines[8], lines[9], lines[10], lines[11])
                data.append(obj)
        file.close()
        # print(len(data))
        for i in range(0, len(data)):
            if data[i].id == Id:
                # del data[i]
                if i < len(data):
                    takeoff_time = data[i].takeoff_time
                    takeoff_place = data[i].takeoff_place
                    land_time = data[i].land_time
                    land_place = data[i].land_place
                    del data[i]
                 ###### what, why can't delete the last element ? why why why why why why why why why why why why why  
                break               #### I have found the reasons ~~~ for...
        file = open(".vscode\\keshe\\tickets.txt", "w", encoding='utf-8')
        file.write('航班编号 航空公司名称 起飞时间 起飞地点 降落时间 降落地点 余票 票价 经停站1名称 到达经停站1时间 经停站2名称 到达经停站2时间\n')
        for line in data:
            file.write('%s\n' %(line.id + ' ' + line.company_name + ' ' + line.takeoff_time + ' ' + line.takeoff_place + ' ' + line.land_time + ' ' + line.land_place + ' ' + line.number
                         + ' ' + line.price + ' ' + line.stop1_place + ' ' + line.stop1_time + ' ' + line.stop2_place + ' ' + line.stop2_time))
        print('航班删除成功！')
        ### 航班删除成功之后还要通知乘坐该航班的乘客 ~  还得推荐个航班
        qifei = recommend(takeoff_place, land_place, takeoff_time, land_time)
        infor(Id, 'delete', qifei)

    def change(self):  ## 单独拿出来了延期和取消的话，那这个修改航班的功能不就被抢的差不多了就  有待商榷   还是应该可以改时间的，因为时间也可以提前的
        print('-------------------修改航班------------------')
        data = []
        Id = input('输入所要修改航班的班号：')
        attribute = input('输入所要修改的属性：1.起飞时间 2.起飞地点 3.降落时间 4.降落地点 5.余票 6.票价 7.经停站1名称 8.到达经停站1时间 9.经停站2名称 10.到达经停站2时间 =>> ')
        value = input('输入修改后的值：')
        file = open(".vscode\\keshe\\tickets.txt", "r", encoding='utf-8')
        file.readline()
        for line in file:
            lines = line.strip('\n').split(' ')
            # print(lines)
            if len(lines) > 1:  ## 专为处理空行的情况
                obj = Ticket(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], lines[6], lines[7], lines[8], lines[9], lines[10], lines[11])
                data.append(obj)
        file.close()
        for i in range(0, len(data)):
            if data[i].id == Id:
                if attribute == '1':
                    data[i].takeoff_time = value
                elif attribute == '2':
                    data[i].takeoff_place = value
                elif attribute == '3':
                    data[i].land_time = value
                elif attribute == '4':
                    data[i].land_place = value
                elif attribute == '5':
                    data[i].number = value
                elif attribute == '6':
                    data[i].price = value
                elif attribute == '7':
                    data[i].stop1_place = value
                elif attribute == '8':
                    data[i].stop1_time = value
                elif attribute == '9':
                    data[i].stop2_place = value
                elif attribute == '10':
                    data[i].stop2_time = value
                break
        file = open(".vscode\\keshe\\tickets.txt", "w", encoding='utf-8')
        file.write('航班编号 航空公司名称 起飞时间 起飞地点 降落时间 降落地点 余票 票价 经停站1名称 到达经停站1时间 经停站2名称 到达经停站2时间\n')
        for line in data:
            file.write('%s\n' %(line.id + ' ' + line.company_name + ' ' + line.takeoff_time + ' ' + line.takeoff_place + ' ' + line.land_time + ' ' + line.land_place + ' ' + line.number
             + ' ' + line.price + ' ' + line.stop1_place + ' ' + line.stop1_time + ' ' + line.stop2_place + ' ' + line.stop2_time))
        print('航班修改成功！')

    def late(self):
        print('-------------------推迟航班------------------')
        data = []; takeoff_place=''; takeoff_time=''; land_place=''; land_time=''
        Id = input('输入要延期航班的班号：')
        # Time2 = input('输入延期到达时间：')
        file = open(".vscode\\keshe\\tickets.txt", "r", encoding='utf-8')
        file.readline()
        for line in file:
            lines = line.strip('\n').split(' ')
            # print(lines)
            ###########################################
            if len(lines) > 1:  ## 专为处理空行的情况###  好像也不用，因为空行没空格？ ？ ？
            ###########################################
                obj = Ticket(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], lines[6], lines[7], lines[8], lines[9], lines[10], lines[11])
                data.append(obj)
        file.close()
        for x in data:
            if x.id == Id:
                takeoff_time = x.takeoff_time
                takeoff_place = x.takeoff_place
                land_time = x.land_time
                land_place = x.land_place

                x.takeoff_time = input('输入延期起飞时间：')
                x.land_time = input('输入延期到达时间：')
                if x.stop1_time != '0':
                    x.stop1_time = input('输入经停站1的到达时间：')
                if x.stop2_time != '0':
                    x.stop2_time = input('输入经停站2的到达时间：')
                break
        file = open(".vscode\\keshe\\tickets.txt", "w", encoding='utf-8')
        file.write('航班编号 航空公司名称 起飞时间 起飞地点 降落时间 降落地点 余票 票价 经停站1名称 到达经停站1时间 经停站2名称 到达经停站2时间\n')
        for line in data:
            file.write('%s\n' %(line.id + ' ' + line.company_name + ' ' + line.takeoff_time + ' ' + line.takeoff_place + ' ' + line.land_time + ' ' + line.land_place + ' ' + line.number
             + ' ' + line.price + ' ' + line.stop1_place + ' ' + line.stop1_time + ' ' + line.stop2_place + ' ' + line.stop2_time))
        print('航班推延操作成功！')
        file.close()
        ### 延期的话最终还要通知乘坐该航班的乘客延期了 ~  还得推荐个航班
        qifei = recommend(takeoff_place, land_place, takeoff_time, land_time)
        infor(Id, 'late', qifei)


def infor(ticket_id, Type, qifei):
    if Type == 'late':  # 通知是航班延期类型时（这是通知航班推迟的）
        data = []
        file = open(".vscode\\keshe\\customers.txt", "r", encoding='utf-8')
        file.readline()
        for line in file:
            lines = line.strip('\n').split(' ')
            if len(lines) > 1:
                obj = CUSTOMER(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5])
                data.append(obj)
        file.close()
        File = open(".vscode\\keshe\\info_1.txt", "w", encoding='utf-8')
        File.write('姓名 邮箱\n')
        for x in data:
            if x.had == ticket_id:
                File.write('%s\n' %(x.name + ' ' + x.email))
        File.close()  # 震惊！没关闭file竟然就不能再读了！   留个疑问吧在这里，单独测试时没问题啊~~
                ### 将其放进通知文件1里（即那些已经买到了这些票的乘客）
    else:  # 这是通知航班取消的
        data = []
        file = open(".vscode\\keshe\\customers.txt", "r", encoding='utf-8')
        file.readline()
        for line in file:
            lines = line.strip('\n').split(' ')
            if len(lines) > 1:
                obj = CUSTOMER(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5])
                data.append(obj)
        file.close()
        File = open(".vscode\\keshe\\info_2.txt", "w", encoding='utf-8')
        File.write('姓名 邮箱\n')
        for x in data:
            if x.had == ticket_id:
                File.write('%s\n' %(x.name + ' ' + x.email))
                ### 将其放进通知文件2中
        File.close()
    info(Type, qifei)
    # print('看看我织没执行info函数')


def info(Type, qifei):  # 接下来就是给指定的顾客邮箱发通知以通知他们
    if Type == 'late':
        data = []
        file = open(".vscode\\keshe\\info_1.txt", "r", encoding='utf-8')
        file.readline()
        for line in file:
            # print(line)
            lines = line.strip('\n').split(' ')
            # print(lines)
            if len(lines) > 0:
                obj = Infor(lines[0], lines[1]) # 从文件中提取出所要通知顾客的姓名和邮箱
                data.append(obj)
        # print(len(data))
        for x in data:
            if qifei == "好自为之吧，没有很合适的航班。":
                message ='尊敬的顾客：' + x.name + '您好。   您所在航班已推迟，请登录以查看具体信息。' + '没有其他合适的航班推荐，建议顺应推迟。'
            else:
                message ='尊敬的顾客：' + x.name + '您好。   您所在航班已推迟，请登录以查看具体信息。' + ' 推荐乘坐具有相同出发点、终点、不延误并且最近乘坐航班：' +  qifei
            # print(message)
            send(x.email, message)
    else:
        data = []
        file = open(".vscode\\keshe\\info_2.txt", "r", encoding='utf-8')
        file.readline()
        for line in file:
            lines = line.strip('\n').split(' ')
            if len(lines) > 1:
                obj = Infor(lines[0], lines[1]) # 从文件中提取出所要通知顾客的姓名和邮箱
                data.append(obj)
        file.close()
        for x in data:
            if qifei == "好自为之吧，没有很合适的航班。":
                 message ='尊敬的顾客：' + x.name + '您好。   您所在航班已推迟，请登录以查看具体信息。' + '没有其他合适的航班推荐，建议顺应推迟。'
            else:
                message ='尊敬的顾客：' + x.name + '您好。   您所在航班已取消，请登录以查看具体信息。' + ' 推荐乘坐具有相同出发点、终点、不延误并且最近乘坐航班：' +  qifei
            send(x.email, message)
    

def send(email, message):
    my_sender = '2963876107@qq.com'    # 管理员邮箱账号密码
    my_pass = 'jeolzcecdirldffd'       # 发件人邮箱密码
    my_user = email      # 收件人邮箱账号，我这边发送给自己
    def mail():
        ret = True
        try:
            msg = MIMEText(message, 'plain' ,'utf-8')
            msg['From'] = formataddr(["航空公司管理员",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["顾客",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = email               # 邮件的主题，也可以说是标题
    
            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret = False
        return ret
    
    ret = mail()
    if ret:
        print("已经通过邮件成功通知购买该航班的所有乘客~")
    else:
        print("通知邮件发送失败")


def recommend(takeoff_place, land_place, takeoff_time, land_time):
    data = []
    Data = []
    file = open(".vscode\\keshe\\tickets.txt", "r", encoding='utf-8')
    file.readline()
    for line in file:
        if line != '\n':
            lines = line.strip('\n').split(" ")
            obj = Ticket(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], lines[6], lines[7], lines[8], lines[9], lines[10], lines[11])
            data.append(obj)

    for i in range(0, len(data)):   # 这里的处理其实应该是提前到达的航班也行的！同时排除时间地点相同到达时间也不延误但是不和被取消航班在同一天的航班
        if ((time_trans(data[i].takeoff_time)[1] == time_trans(takeoff_time)[1]) and (data[i].takeoff_place == takeoff_place) and (data[i].land_place == land_place) and 
        ((int(time_trans(data[i].land_time)[2]) - int(time_trans(land_time)[2])) * 60 + (int(time_trans(data[i].land_time)[3]) - int(time_trans(land_time)[3])) <= 0 )):
            Data.append(data[i])
    if len(Data) == 0:
        return "好自为之吧，没有很合适的航班。"

    now = datetime.datetime.now()
    now_hour = now.hour
    now_minute = now.minute
    min_ticket = ' '
    minzhi = 1000000
    for x in Data:
        x_hour = int(time_trans(x.takeoff_time)[2])
        x_minute = int(time_trans(x.takeoff_time)[3])
        delt = (x_hour - now_hour) * 60 + (x_minute - now_minute)
        if minzhi > delt:
            minzhi = delt
            min_ticket = x.id
    return min_ticket
    

def time_trans(time):    # 将时间从字符串格式转到适合的格式
    month = int(time[0:2])
    day = int(time[2:4])
    hour = (time[4:6])
    minute = (time[6:])
    Time = [month, day, hour, minute]
    return Time
    

def Print(args):    # 打印机票（航班）信息函数
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
    print('|  余票        ：%s'  %args.number)
    print('|  票价        ：%s'  %args.price)
    print('--------------------------------------------')


if __name__ == "__main__":
    print('\n'); print('* * * * * * * * * 机票管理系统 * * * * * * * * *')
    monitor01 = Monitor()
    while(1):
        print('-----------------------------------------------------------------------------')
        behavior = input('选择后续操作：1.查询航班  2.增加航班  3.删除航班  4.修改航班  5.推迟航班 ===> '); print()
        if behavior == '1':
            monitor01.query()
        elif behavior == '2':
            monitor01.add()
        elif behavior == '3':
            monitor01.delete()
        elif behavior == '4':
            monitor01.change()
        elif behavior == '5':
            monitor01.late()
        else:
            print('输入有误.....')
