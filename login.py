import wx  # 导入wxpyhton，pyhton自带的GUI库
import wx.xrc

import pymysql  # 用于操作数据库

user = ''
shop = ''
raider = ''
admin = ''
dish=''
order=''

class Myframe(wx.Frame):

    def __init__(self, parent):
        # Wx.Frame (parent, id, title, pos, size, style, name)
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"饱了么外卖平台", pos=wx.DefaultPosition, size=wx.Size(610, 400),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.Center()  # 居中显示
        '''
        # 小构件，如按钮，文本框等被放置在面板窗口。 wx.Panel类通常是被放在一个wxFrame对象中。这个类也继承自wxWindow类。
        self.m_panel1 = wx.Panel(self)
        
        # 标签，一行或多行的只读文本，Wx.StaticText(parent, id, label, position, size, style)
        self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"关于店铺：", (20, 20))
        self.m_button1 = wx.Button(self.m_panel1, wx.ID_ANY, u"店铺信息", (130, 20), wx.DefaultSize,
                                   style=wx.BORDER_MASK)
        self.m_button2 = wx.Button(self.m_panel1, wx.ID_ANY, u"店铺上架", (250, 20), wx.DefaultSize,
                                   style=wx.BORDER_MASK)
        self.m_button3 = wx.Button(self.m_panel1, wx.ID_ANY, u"店铺下架", (370, 20), wx.DefaultSize,
                                   style=wx.BORDER_MASK)
        '''
        # 利用wxpython的GridBagSizer()进行页面布局
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(10, 20)  # 列间隔为10，行间隔为20

        # 添加账号字段，并加入页面布局，为第一行，第一列
        text = wx.StaticText(panel, label="账号")
        sizer.Add(text, pos=(0, 0), flag=wx.ALL, border=5)

        # 添加文本框字段，并加入页面布局，为第一行，第2,3列
        self.tc = wx.TextCtrl(panel)
        sizer.Add(self.tc, pos=(0, 1), span=(1, 2), flag=wx.EXPAND | wx.ALL, border=5)

        # 添加密码字段，并加入页面布局，为第二行，第一列
        text1 = wx.StaticText(panel, label="密码")
        sizer.Add(text1, pos=(1, 0), flag=wx.ALL, border=5)

        # 添加文本框字段，以星号掩盖,并加入页面布局，为第二行，第2,3列
        self.tc1 = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        sizer.Add(self.tc1, pos=(1, 1), span=(1, 2), flag=wx.EXPAND | wx.ALL, border=5)

        # 添加登录按钮，并加入页面布局，为第四行，第2列
        btn0 = wx.Button(panel, -1, "用户登录")
        sizer.Add(btn0, pos=(2, 0), flag=wx.ALL, border=5)

        # 添加登录按钮，并加入页面布局，为第四行，第2列
        btn2 = wx.Button(panel, -1, "商家登录")
        sizer.Add(btn2, pos=(3, 0), flag=wx.ALL, border=5)

        # 添加登录按钮，并加入页面布局，为第四行，第2列
        btn4 = wx.Button(panel, -1, "骑手登录")
        sizer.Add(btn4, pos=(4, 0), flag=wx.ALL, border=5)

        # 添加登录按钮，并加入页面布局，为第四行，第2列
        btn1 = wx.Button(panel, -1, "用户注册")
        sizer.Add(btn1, pos=(2, 1), flag=wx.ALL, border=5)

        # 添加登录按钮，并加入页面布局，为第四行，第2列
        #btn3 = wx.Button(panel, -1, "商家注册")
        #sizer.Add(btn3, pos=(3, 1), flag=wx.ALL, border=5)

        # 添加登录按钮，并加入页面布局，为第四行，第2列
        #btn5 = wx.Button(panel, -1, "骑手注册")
        #sizer.Add(btn5, pos=(4, 1), flag=wx.ALL, border=5)

        # 为登录按钮绑定login_process事件
        self.Bind(wx.EVT_BUTTON, self.login_processu, btn0)
        self.Bind(wx.EVT_BUTTON, self.login_processs, btn2)
        self.Bind(wx.EVT_BUTTON, self.login_processr, btn4)
        # 为登录按钮绑定login_process事件
        self.Bind(wx.EVT_BUTTON, MyDialogru(None).OnClick, btn1)
        #self.Bind(wx.EVT_BUTTON, Mydialogrs(None).OnClick, btn3)
        # 将Panmel适应GridBagSizer()放置
        panel.SetSizerAndFit(sizer)

    def login_processu(self, event):
        global user
        user = self.tc.GetValue()  # 获取验证码文本框的输入文字
        self.pwd = self.tc1.GetValue()  # 获取验证码文本框的输入文字
        # print(self.user)
        # print(self.pwd)
        conn = pymysql.connect("localhost", "root", "password", "baoleme", charset='utf8')
        # print("connect")
        cursor = conn.cursor()
        # print("sc")

        data = (user, self.pwd)

        try:
            sql = "select * from user where userid = %s and keyword = %s"
            result = cursor.execute(sql, data)
            print(result)
            if result == 0:
                print('用户名或密码错误')
                dial = wx.MessageDialog(None, '用户名或密码错误!', '错误信息', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
                dial.ShowModal()  # 显示对话框
            else:
                print('登陆成功')
                self.Close()
                Mydialogmu.OnCreate(None)
                # MyDialogru
                # self.Close()

            conn.commit()
            # print('1')
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def login_processs(self, event):
        global shop
        shop = self.tc.GetValue()  # 获取验证码文本框的输入文字
        self.pwd = self.tc1.GetValue()  # 获取验证码文本框的输入文字
        # print(self.user)
        # print(self.pwd)
        conn = pymysql.connect("localhost", "root", "password", "baoleme", charset='utf8')
        # print("connect")
        cursor = conn.cursor()
        # print("connect")

        data = (shop, self.pwd)

        try:
            sql = "select * from shop where shopid = %s and keyword = %s"
            result = cursor.execute(sql, data)
            print(result)
            if result == 0:
                print('用户名或密码错误')
                dial = wx.MessageDialog(None, '用户名或密码错误!', '错误信息', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
                dial.ShowModal()  # 显示对话框
            else:
                print('登陆成功')
                self.Close()
                Mydialogms.OnCreate(None)
                #print('open')
                # MyDialogru
                # self.Close()

            conn.commit()
            # print('1')
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def login_processr(self, event):
        global raider
        raider = self.tc.GetValue()  # 获取验证码文本框的输入文字
        self.pwd = self.tc1.GetValue()  # 获取验证码文本框的输入文字
        # print(self.user)
        # print(self.pwd)
        conn = pymysql.connect("localhost", "root", "password", "baoleme", charset='utf8')
        # print("connect")
        cursor = conn.cursor()
        # print("connect")

        data = (raider, self.pwd)

        try:
            sql = "select * from raider where raiderid = %s and keyword = %s"
            result = cursor.execute(sql, data)
            print(result)
            if result == 0:
                print('用户名或密码错误')
                dial = wx.MessageDialog(None, '用户名或密码错误!', '错误信息', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
                dial.ShowModal()  # 显示对话框
            else:
                print('登陆成功')
                self.Close()
                MyDialogmr.OnCreate(None)
                #print('open')
                # MyDialogru
                # self.Close()
            conn.commit()
            # print('1')
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


class MyDialogru(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"注册", pos=wx.DefaultPosition, size=wx.Size(400, 400),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "请输入id：", (20, 20))
        self.t1 = wx.TextCtrl(self.panel, pos=(150, 20), size=(120, 25))

        #wx.StaticText(self.panel, -1, "请输入姓名：", (20, 80))
        #self.t2 = wx.TextCtrl(self.panel, pos=(150, 80), size=(120, 25))

        wx.StaticText(self.panel, -1, "请输入地址：", (20, 140))
        self.t3 = wx.TextCtrl(self.panel, pos=(150, 140), size=(120, 25))

        wx.StaticText(self.panel, -1, "请输入电话号码：", (20, 200))
        self.t4 = wx.TextCtrl(self.panel, pos=(150, 200), size=(120, 25))

        wx.StaticText(self.panel, -1, "请输入密码：", (20, 260))
        self.t5 = wx.TextCtrl(self.panel, pos=(150, 260), size=(120, 25))

    def OnClick(self, e):
        dialog42 = MyDialogru(None)
        btn = wx.Button(parent=dialog42.panel, label="注册", pos=(20, 310), size=(100, 45))
        btn.Bind(wx.EVT_BUTTON, dialog42.insert)
        dialog42.ShowModal()

    def insert(self, e):
        conn = pymysql.connect("localhost", "root", "password", "baoleme", charset='utf8')
        cursor = conn.cursor()

        student_phone = self.t1.GetValue()
        #server_id = self.t2.GetValue()
        order_id = self.t3.GetValue()
        order_money = self.t4.GetValue()
        order_way = self.t5.GetValue()

        data = (student_phone, order_id, order_money, order_way)

        try:
            print(data)
            sql = "insert into user (userid,address,phone,keyword) values(%s,%s,%s,%s)"
            t = cursor.execute(sql, data)
            print(t)
            conn.commit()
            if t == 1:
                dial = wx.MessageDialog(None, '注册成功，请登录！', '结果', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
                dial.ShowModal()  # 显示对话框
                self.Close()
            #else:
                #dial = wx.MessageDialog(None, 'id重复!', '结果', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
                #dial.ShowModal()  # 显示对话框
        except:
            conn.rollback()
            dial = wx.MessageDialog(None, 'id重复!', '结果', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
            dial.ShowModal()  # 显示对话框
        finally:
            cursor.close()
            conn.close()


class Mydialogmu(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"我的主页", pos=wx.DefaultPosition, size=wx.Size(289, 319),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"欢迎使用", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer1.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, user, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        # self.m_staticText2.SetLabel(user)
        # print(user)
        bSizer1.Add(self.m_staticText2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"查询菜品", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button1, 0, wx.ALL, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"查询商家", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button2, 0, wx.ALL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"未完成订单", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button3, 0, wx.ALL, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"评价订单", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"修改密码", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button5, 0, wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button1.Bind(wx.EVT_BUTTON, Mydialogsd(None).OnClick)
        self.m_button2.Bind(wx.EVT_BUTTON, Mydialogss(None).OnClick)
        self.m_button3.Bind(wx.EVT_BUTTON, MyDialogso(None).OnClick)
        self.m_button4.Bind(wx.EVT_BUTTON, MyDialogco(None).OnClick)
        self.m_button5.Bind(wx.EVT_BUTTON, MyDialogpu(None).OnClick)

    # Virtual event handlers, overide them in your derived class
    # def OnDish(self, event):
    # Mydialogsd(None).OnClick()

    def OnShop(self, event):
        event.Skip()

    def OnCart(self, event):
        event.Skip()

    def OnComment(self, event):
        event.Skip()

    def OnOrder(self, event):
        event.Skip()

    def OnCreate(self):
        dialog4 = Mydialogmu(None)
        # print(user)
        dialog4.ShowModal()
        #print('yes')
        print(user)
        #print('yes')

    def __del__(self):
        pass

class MyDialogco(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"订单", pos=wx.DefaultPosition, size=wx.Size(500, 400),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        #wx.StaticText(self.panel, -1, "买家电话：", (20, 20))
        #self.t1 = wx.TextCtrl(self.panel, pos=(90, 20), size=(120, 25))
        # btn = wx.Button(parent=self.panel, label="查询", pos=(240, 20), size=(70, 25))
        # btn.Bind(wx.EVT_BUTTON, self.find)
        wx.StaticText(self.panel, -1, "订单编号", (20, 60))
        wx.StaticText(self.panel, -1, "订单金额", (120, 60))
        wx.StaticText(self.panel, -1, "配送骑手", (220, 60))
        wx.StaticText(self.panel, -1, "接单商店", (320, 60))

    def OnClick(self, e):
        dialogco = MyDialogco(None)
        btn = wx.Button(parent=dialogco.panel, label="评价配送", pos=(240, 20), size=(70, 25))
        #btn.Bind(wx.EVT_BUTTON, dailogco.OnCR)
        btn.Bind(wx.EVT_BUTTON, MyDialogcr(None).OnClick)
        btn1 = wx.Button(parent=dialogco.panel, label="评价菜品", pos=(120, 20), size=(70, 25))
        btn1.Bind(wx.EVT_BUTTON, MyDialogcs(None).OnClick)
    #def find(self, event):
        conn = pymysql.connect("localhost", "root", "password", "baoleme", charset='utf8')
        cursor = conn.cursor()
        #data=(user,'0')
        #print('shu')
        #print(shop)
        #print(user)
        try:
            #sql = "select orders.orderid , dishid from order_detail join orders on order_detail.orderid=orders.orderid where shopid=%s "
            sql = "select orderid,cost,raiderid,shopid from orders where userid=%s and ok='1' and com='0'"

            t=cursor.execute(sql,user)
            rs = cursor.fetchall()
            print('rs')
            #print('tt')
            print(user)
            #print(rs)
            h = 80
            for row in rs:
                h = h + 20
                dish_id = str(row[0])
                dishname = str(row[1])
                shopname = str(row[2])
                price = str(row[3])
                m_radioBtn5 = wx.RadioButton(dialogco.panel, wx.ID_ANY, dish_id, (20, h))
                wx.StaticText(dialogco.panel, -1, dishname, (120, h))
                wx.StaticText(dialogco.panel, -1, shopname, (220, h))
                wx.StaticText(dialogco.panel, -1, price, (320, h))
            # self.panel.Refresh()
            dialogco.Bind(wx.EVT_RADIOBUTTON, dialogco.OnRadio)
            #print(data)
            conn.commit()
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
        dialogco.Show()
    def OnRadio(self, e):
            r = e.GetEventObject()
            self.oid = r.GetLabel()
            global order
            order=self.oid
            #print('ra')

class MyDialogcr(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"评价配送", pos=wx.DefaultPosition, size=wx.Size(400, 400),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "评价：", (20, 20))
        self.t1 = wx.TextCtrl(self.panel, pos=(150, 20), size=(120, 25))

        #wx.StaticText(self.panel, -1, "请输入姓名：", (20, 80))
        #self.t2 = wx.TextCtrl(self.panel, pos=(150, 80), size=(120, 25))

        #wx.StaticText(self.panel, -1, "请输入地址：", (20, 140))
        #self.t3 = wx.TextCtrl(self.panel, pos=(150, 140), size=(120, 25))

        #wx.StaticText(self.panel, -1, "请输入电话号码：", (20, 200))
        #self.t4 = wx.TextCtrl(self.panel, pos=(150, 200), size=(120, 25))

        #wx.StaticText(self.panel, -1, "请输入价格：", (20, 260))
        #self.t5 = wx.TextCtrl(self.panel, pos=(150, 260), size=(120, 25))

    def OnClick(self, e):
        dialogcr = MyDialogcr(None)
        btn = wx.Button(parent=dialogcr.panel, label="确定", pos=(20, 310), size=(100, 45))
        btn.Bind(wx.EVT_BUTTON, dialogcr.insert)
        dialogcr.ShowModal()

    def insert(self, e):
        conn = pymysql.connect("localhost", "root", "password", "baoleme", charset='utf8')
        cursor = conn.cursor()

        student_phone = self.t1.GetValue()#.encode('utf8')
        #server_id = self.t2.GetValue()
        #order_id = self.t3.GetValue()
        #order_money = self.t4.GetValue()
        #order_way = self.t5.GetValue()
        sql = "select raiderid from orders  where orderid=%s"
        t = cursor.execute(sql, order)
        rs = cursor.fetchone()
        global raider
        raider=rs[0]
        data = (user,raider,order,student_phone)
        try:
            print(data)
            sql = "insert into raider_comment  values(%s,%s,%s,%s)"
            t = cursor.execute(sql, data)
            sql = "update orders set com='1' where orderid=%s"
            t = cursor.execute(sql, order)
            print(t)
            conn.commit()
            if t == 1:
                dial = wx.MessageDialog(None, '评价成功！', '结果', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
                dial.ShowModal()  # 显示对话框
                self.Close()
            #else:
                #dial = wx.MessageDialog(None, 'id重复!', '结果', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
                #dial.ShowModal()  # 显示对话框
        except:
            conn.rollback()
            #dial = wx.MessageDialog(None, 'id重复!', '结果', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
            #dial.ShowModal()  # 显示对话框
        finally:
            cursor.close()
            conn.close()

class MyDialogcs(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"评价菜品", pos=wx.DefaultPosition, size=wx.Size(400, 400),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "评价：", (20, 20))
        self.t1 = wx.TextCtrl(self.panel, pos=(150, 20), size=(120, 25))

        #wx.StaticText(self.panel, -1, "请输入姓名：", (20, 80))
        #self.t2 = wx.TextCtrl(self.panel, pos=(150, 80), size=(120, 25))

        #wx.StaticText(self.panel, -1, "请输入地址：", (20, 140))
        #self.t3 = wx.TextCtrl(self.panel, pos=(150, 140), size=(120, 25))

        #wx.StaticText(self.panel, -1, "请输入电话号码：", (20, 200))
        #self.t4 = wx.TextCtrl(self.panel, pos=(150, 200), size=(120, 25))

        #wx.StaticText(self.panel, -1, "请输入价格：", (20, 260))
        #self.t5 = wx.TextCtrl(self.panel, pos=(150, 260), size=(120, 25))

    def OnClick(self, e):
        dialogcs = MyDialogcs(None)
        btn = wx.Button(parent=dialogcs.panel, label="确定", pos=(20, 310), size=(100, 45))
        btn.Bind(wx.EVT_BUTTON, dialogcs.insert)
        dialogcs.ShowModal()

    def insert(self, e):
        conn = pymysql.connect("localhost", "root", "password", "baoleme", charset='utf8')
        cursor = conn.cursor()

        student_phone = self.t1.GetValue()
        #server_id = self.t2.GetValue()
        #order_id = self.t3.GetValue()
        #order_money = self.t4.GetValue()
        #order_way = self.t5.GetValue()
        sql = "select shopid from orders  where orderid=%s"
        t = cursor.execute(sql, order)
        rs = cursor.fetchone()
        global shop
        shop = rs[0]
        data = (user,shop,student_phone,order)

        try:
            print(data)
            sql = "insert into shop_comment  values(%s,%s,%s,%s)"
            t = cursor.execute(sql, data)
            print('ok')
            sql = "update orders set com='1' where orderid=%s"
            t = cursor.execute(sql, order)
            print(t)
            conn.commit()
            if t == 1:
                dial = wx.MessageDialog(None, '评价成功！', '结果', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
                dial.ShowModal()  # 显示对话框
                self.Close()
            #else:
                #dial = wx.MessageDialog(None, 'id重复!', '结果', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
                #dial.ShowModal()  # 显示对话框
        except:
            conn.rollback()
            #dial = wx.MessageDialog(None, 'id重复!', '结果', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
            #dial.ShowModal()  # 显示对话框
        finally:
            cursor.close()
            conn.close()

class Mydialogms(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"商家界面", pos=wx.DefaultPosition, size=wx.Size(235, 307),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"欢迎使用", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        bSizer3.Add(self.m_staticText5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, shop, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        bSizer3.Add(self.m_staticText6, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"查看在售菜品", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"上架菜品", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_button5, 0, wx.ALL, 5)

        self.m_button6 = wx.Button(self, wx.ID_ANY, u"查看新订单", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_button6, 0, wx.ALL, 5)

        self.m_button7 = wx.Button(self, wx.ID_ANY, u"查看评价", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_button7, 0, wx.ALL, 5)

        #self.m_button8 = wx.Button(self, wx.ID_ANY, u"修改密码", wx.DefaultPosition, wx.DefaultSize, 0)
        #bSizer3.Add(self.m_button8, 0, wx.ALL, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)
        self.m_button4.Bind(wx.EVT_BUTTON, MyDialogod(None).OnClick)
        self.m_button6.Bind(wx.EVT_BUTTON, MyDialogwo(None).OnClick)
        self.m_button5.Bind(wx.EVT_BUTTON, MyDialogad(None).OnClick)
        self.m_button7.Bind(wx.EVT_BUTTON, MyDialogwcs(None).OnClick)
        #self.m_button5.Bind(wx.EVT_BUTTON, MyDialogpu(None).OnClick)
    def OnCreate(self):
        dialogms = Mydialogms(None)
        print(shop)
        dialogms.ShowModal()
        #print('yes')
        #print(user)
        #print('yes')

class MyDialogwo(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"订单", pos=wx.DefaultPosition, size=wx.Size(500, 400),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        #wx.StaticText(self.panel, -1, "买家电话：", (20, 20))
        #self.t1 = wx.TextCtrl(self.panel, pos=(90, 20), size=(120, 25))
        # btn = wx.Button(parent=self.panel, label="查询", pos=(240, 20), size=(70, 25))
        # btn.Bind(wx.EVT_BUTTON, self.find)
        wx.StaticText(self.panel, -1, "订单编号", (20, 60))
        wx.StaticText(self.panel, -1, "订单金额", (120, 60))
        wx.StaticText(self.panel, -1, "下单用户", (220, 60))
        wx.StaticText(self.panel, -1, "接单骑手", (320, 60))

    def OnClick(self, e):
        dialogwo = MyDialogwo(None)
        btn = wx.Button(parent=dialogwo.panel, label="查看明细", pos=(240, 20), size=(70, 25))
        #btn.Bind(wx.EVT_BUTTON, dialogwo.)
        btn.Bind(wx.EVT_BUTTON, MyDialogwd(None).OnClick)
        #btn1 = wx.Button(parent=dialogsc.panel, label="全部结算", pos=(120, 20), size=(70, 25))
        #btn1.Bind(wx.EVT_BUTTON, dialogsc.OnOrder)
    #def find(self, event):
        conn = pymysql.connect("localhost", "root", "password", "baoleme", charset='utf8')
        cursor = conn.cursor()
        #data=(user,'0')
        #print('shu')
        #print(shop)
        #print(user)
        try:
            #sql = "select orders.orderid , dishid from order_detail join orders on order_detail.orderid=orders.orderid where shopid=%s "
            sql = "select orderid,cost,userid,raiderid from orders where shopid=%s and ok='0'"
            t=cursor.execute(sql,shop)
            rs = cursor.fetchall()
            print('rs')
            #print('tt')
            print(user)
            #print(rs)
            h = 80
            for row in rs:
                h = h + 20
                dish_id = str(row[0])
                dishname = str(row[1])
                shopname = str(row[2])
                price = str(row[3])
                m_radioBtn5 = wx.RadioButton(dialogwo.panel, wx.ID_ANY, dish_id, (20, h))
                wx.StaticText(dialogwo.panel, -1, dishname, (120, h))
                wx.StaticText(dialogwo.panel, -1, shopname, (220, h))
                wx.StaticText(dialogwo.panel, -1, price, (320, h))
            # self.panel.Refresh()
            dialogwo.Bind(wx.EVT_RADIOBUTTON, dialogwo.OnRadio)
            #print(data)
            conn.commit()
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
        dialogwo.Show()
    def OnRadio(self, e):
            r = e.GetEventObject()
            self.oid = r.GetLabel()
            global order
            order=self.oid
            #print('ra')

class MyDialogwd(wx.Dialog):
    def __init__(self, parent):
        ti=order+'号订单明细'
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=ti, pos=wx.DefaultPosition, size=wx.Size(500, 400),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        #wx.StaticText(self.panel, -1, "买家电话：", (20, 20))
        #self.t1 = wx.TextCtrl(self.panel, pos=(90, 20), size=(120, 25))
        # btn = wx.Button(parent=self.panel, label="查询", pos=(240, 20), size=(70, 25))
        # btn.Bind(wx.EVT_BUTTON, self.find)
        wx.StaticText(self.panel, -1, "菜品id", (20, 60))
        wx.StaticText(self.panel, -1, "菜品名", (120, 60))
        #wx.StaticText(self.panel, -1, "订单金额", (220, 60))
        #wx.StaticText(self.panel, -1, "订餐方式", (320, 60))

    def OnClick(self, e):
        dialogwd = MyDialogwd(None)
        #btn = wx.Button(parent=dialogwd.panel, label="查看明细", pos=(240, 20), size=(70, 25))
        #btn.Bind(wx.EVT_BUTTON, dialogwo.)
        #btn1 = wx.Button(parent=dialogsc.panel, label="全部结算", pos=(120, 20), size=(70, 25))
        #btn1.Bind(wx.EVT_BUTTON, dialogsc.OnOrder)
    #def find(self, event):
        conn = pymysql.connect("localhost", "root", "password", "baoleme", charset='utf8')
        cursor = conn.cursor()
        #data=(user,'0')
        #print('shu')
        #print(shop)
        #print(user)
        try:
            data=(shop,order)
            print('order')
            print(order)
            sql = "select dish.dishid,dishname from order_detail join dish on order_detail.dishid=dish.dishid where orderid=%s "
            #sql = "select * from orders where shopid=%s"
            t=cursor.execute(sql,order)
            rs = cursor.fetchall()
            print('rs')
            #print('tt')
            print(user)
            print(rs)
            h = 80
            for row in rs:
                h = h + 20
                dish_id = str(row[0])
                dishname = str(row[1])
                #shopname = str(row[2])
                #price = str(row[3])
                wx.StaticText(dialogwd.panel, -1, dish_id, (20, h))
                wx.StaticText(dialogwd.panel, -1, dishname, (120, h))
                #wx.StaticText(dialogwd.panel, -1, shopname, (220, h))
                #wx.StaticText(dialogsc.panel, -1, price, (320, h))
            # self.panel.Refresh()
            #dialogwo.Bind(wx.EVT_RADIOBUTTON, dialogwo.OnRadio)
            #print(data)
            conn.commit()
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
        dialogwd.Show()

class MyDialogad(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"上架菜品", pos=wx.DefaultPosition, size=wx.Size(400, 400),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "请输入菜名：", (20, 20))
        self.t1 = wx.TextCtrl(self.panel, pos=(150, 20), size=(120, 25))

        #wx.StaticText(self.panel, -1, "请输入姓名：", (20, 80))
        #self.t2 = wx.TextCtrl(self.panel, pos=(150, 80), size=(120, 25))

        #wx.StaticText(self.panel, -1, "请输入地址：", (20, 140))
        #self.t3 = wx.TextCtrl(self.panel, pos=(150, 140), size=(120, 25))

        #wx.StaticText(self.panel, -1, "请输入电话号码：", (20, 200))
        #self.t4 = wx.TextCtrl(self.panel, pos=(150, 200), size=(120, 25))

        wx.StaticText(self.panel, -1, "请输入价格：", (20, 260))
        self.t5 = wx.TextCtrl(self.panel, pos=(150, 260), size=(120, 25))

    def OnClick(self, e):
        dialogad = MyDialogad(None)
        btn = wx.Button(parent=dialogad.panel, label="上架", pos=(20, 310), size=(100, 45))
        btn.Bind(wx.EVT_BUTTON, dialogad.insert)
        dialogad.ShowModal()

    def insert(self, e):
        conn = pymysql.connect("localhost", "root", "password", "baoleme", charset='utf8')
        cursor = conn.cursor()

        student_phone = self.t1.GetValue()#.encode('utf8')
        #server_id = self.t2.GetValue()
        #order_id = self.t3.GetValue()
        #order_money = self.t4.GetValue()
        order_way = self.t5.GetValue()#.encode('utf8')

        data = (student_phone,shop,order_way)

        try:
            print(data)
            sql = "insert into dish (dishname,shopid,price) values(%s,%s,%s)"
            t = cursor.execute(sql, data)
            print(t)
            conn.commit()
            if t == 1:
                dial = wx.MessageDialog(None, '上架成功！', '结果', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
                dial.ShowModal()  # 显示对话框
                self.Close()
            #else:
                #dial = wx.MessageDialog(None, 'id重复!', '结果', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
                #dial.ShowModal()  # 显示对话框
        except:
            conn.rollback()
            #dial = wx.MessageDialog(None, 'id重复!', '结果', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
            #dial.ShowModal()  # 显示对话框
        finally:
            cursor.close()
            conn.close()

class MyDialogwcs(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"查看评价", pos=wx.DefaultPosition, size=wx.Size(500, 400),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        #wx.StaticText(self.panel, -1, "买家电话：", (20, 20))
        #self.t1 = wx.TextCtrl(self.panel, pos=(90, 20), size=(120, 25))
        # btn = wx.Button(parent=self.panel, label="查询", pos=(240, 20), size=(70, 25))
        # btn.Bind(wx.EVT_BUTTON, self.find)
        wx.StaticText(self.panel, -1, "订单编号", (20, 60))
        wx.StaticText(self.panel, -1, "评价详情", (120, 60))
        #wx.StaticText(self.panel, -1, "订单金额", (220, 60))
        #wx.StaticText(self.panel, -1, "订餐方式", (320, 60))

    def OnClick(self, e):
        dialogwcs = MyDialogwcs(None)
        #btn = wx.Button(parent=dialogwd.panel, label="查看明细", pos=(240, 20), size=(70, 25))
        #btn.Bind(wx.EVT_BUTTON, dialogwo.)
        #btn1 = wx.Button(parent=dialogsc.panel, label="全部结算", pos=(120, 20), size=(70, 25))
        #btn1.Bind(wx.EVT_BUTTON, dialogsc.OnOrder)
    #def find(self, event):
        conn = pymysql.connect("localhost", "root", "password", "baoleme", charset='utf8')
        cursor = conn.cursor()
        #data=(user,'0')
        #print('shu')
        #print(shop)
        #print(user)
        try:
            data=(shop,order)
            print('order')
            print(order)
            sql = "select orderid,content from shop_comment where shopid=%s "
            #sql = "select * from orders where shopid=%s"
            t=cursor.execute(sql,shop)
            rs = cursor.fetchall()
            print('rs')
            #print('tt')
            print(user)
            print(rs)
            h = 80
            for row in rs:
                h = h + 20
                dish_id = str(row[0])
                dishname = str(row[1])
                #shopname = str(row[2])
                #price = str(row[3])
                wx.StaticText(dialogwcs.panel, -1, dish_id, (20, h))
                wx.StaticText(dialogwcs.panel, -1, dishname, (120, h))
                #wx.StaticText(dialogwd.panel, -1, shopname, (220, h))
                #wx.StaticText(dialogsc.panel, -1, price, (320, h))
            # self.panel.Refresh()
            #dialogwo.Bind(wx.EVT_RADIOBUTTON, dialogwo.OnRadio)
            #print(data)
            conn.commit()
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
        dialogwcs.Show()

class MyDialogmr(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"骑手主页", pos=wx.DefaultPosition, size=wx.Size(180, 300),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"欢迎", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer1.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, raider, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        bSizer1.Add(self.m_staticText2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"接取订单", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button1, 0, wx.ALL, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"已接订单", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"查看评价", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button2, 0, wx.ALL, 5)

        #self.m_button3 = wx.Button(self, wx.ID_ANY, u"修改密码", wx.DefaultPosition, wx.DefaultSize, 0)
        #bSizer1.Add(self.m_button3, 0, wx.ALL, 5)

        self.m_button1.Bind(wx.EVT_BUTTON, MyDialogto(None).OnClick)
        self.m_button2.Bind(wx.EVT_BUTTON, MyDialogwcr(None).OnClick)
        self.m_button4.Bind(wx.EVT_BUTTON, MyDialogro(None).OnClick)
        self.SetSizer(bSizer1)
        self.Layout()
        self.Centre(wx.BOTH)
    def OnCreate(self):
        dialogmr = MyDialogmr(None)
        #print(shop)
        dialogmr.ShowModal()

class MyDialogwcr(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"查看评价", pos=wx.DefaultPosition, size=wx.Size(500, 400),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        #wx.StaticText(self.panel, -1, "买家电话：", (20, 20))
        #self.t1 = wx.TextCtrl(self.panel, pos=(90, 20), size=(120, 25))
        # btn = wx.Button(parent=self.panel, label="查询", pos=(240, 20), size=(70, 25))
        # btn.Bind(wx.EVT_BUTTON, self.find)
        wx.StaticText(self.panel, -1, "订单编号", (20, 60))
        wx.StaticText(self.panel, -1, "评价详情", (120, 60))
        #wx.StaticText(self.panel, -1, "订单金额", (220, 60))
        #wx.StaticText(self.panel, -1, "订餐方式", (320, 60))

    def OnClick(self, e):
        dialogwcr = MyDialogwcr(None)
        #btn = wx.Button(parent=dialogwd.panel, label="查看明细", pos=(240, 20), size=(70, 25))
        #btn.Bind(wx.EVT_BUTTON, dialogwo.)
        #btn1 = wx.Button(parent=dialogsc.panel, label="全部结算", pos=(120, 20), size=(70, 25))
        #btn1.Bind(wx.EVT_BUTTON, dialogsc.OnOrder)
    #def find(self, event):
        conn = pymysql.connect("localhost", "root", "password", "baoleme", charset='utf8')
        cursor = conn.cursor()
        #data=(user,'0')
        #print('shu')
        #print(shop)
        #print(user)
        try:
            data=(shop,order)
            print('order')
            print(order)
            sql = "select orderid,content from raider_comment where raiderid=%s "
            #sql = "select * from orders where shopid=%s"
            t=cursor.execute(sql,raider)
            rs = cursor.fetchall()
            print('rs')
            #print('tt')
            print(user)
            print(rs)
            h = 80
            for row in rs:
                h = h + 20
                dish_id = str(row[0])
                dishname = str(row[1])
                #shopname = str(row[2])
                #price = str(row[3])
                wx.StaticText(dialogwcr.panel, -1, dish_id, (20, h))
                wx.StaticText(dialogwcr.panel, -1, dishname, (120, h))
                #wx.StaticText(dialogwd.panel, -1, shopname, (220, h))
                #wx.StaticText(dialogsc.panel, -1, price, (320, h))
            # self.panel.Refresh()
            #dialogwo.Bind(wx.EVT_RADIOBUTTON, dialogwo.OnRadio)
            #print(data)
            conn.commit()
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
        dialogwcr.Show()

class MyDialogro(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"查看订单", pos=wx.DefaultPosition, size=wx.Size(700, 400),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        #wx.StaticText(self.panel, -1, "买家电话：", (20, 20))
        #self.t1 = wx.TextCtrl(self.panel, pos=(90, 20), size=(120, 25))
        # btn = wx.Button(parent=self.panel, label="查询", pos=(240, 20), size=(70, 25))
        # btn.Bind(wx.EVT_BUTTON, self.find)
        wx.StaticText(self.panel, -1, "订单编号", (20, 60))
        wx.StaticText(self.panel, -1, "下单用户", (120, 60))
        wx.StaticText(self.panel, -1, "用户电话", (220, 60))
        wx.StaticText(self.panel, -1, "用户地址", (320, 60))
        wx.StaticText(self.panel, -1, "接单商店", (420, 60))
        wx.StaticText(self.panel, -1, "商店地址", (520, 60))

    def OnClick(self, e):
        dialogro = MyDialogro(None)
        #btn = wx.Button(parent=dialogwd.panel, label="查看明细", pos=(240, 20), size=(70, 25))
        #btn.Bind(wx.EVT_BUTTON, dialogwo.)
        #btn1 = wx.Button(parent=dialogsc.panel, label="全部结算", pos=(120, 20), size=(70, 25))
        #btn1.Bind(wx.EVT_BUTTON, dialogsc.OnOrder)
    #def find(self, event):
        conn = pymysql.connect("localhost", "root", "password", "baoleme", charset='utf8')
        cursor = conn.cursor()
        #data=(user,'0')
        #print('shu')
        #print(shop)
        #print(user)
        try:
            data=(shop,order)
            print('order')
            print(order)
            sql = "select orderid,user.userid,user.phone,user.address,shop.shopid,shop.address from orders join user on orders.userid=user.userid join shop on orders.shopid=shop.shopid where raiderid=%s and ok='0'"
            #sql = "select * from orders where shopid=%s"
            t=cursor.execute(sql,raider)
            rs = cursor.fetchall()
            print('rs')
            #print('tt')
            print(user)
            print(rs)
            h = 80
            for row in rs:
                h = h + 20
                orderid = str(row[0])
                username = str(row[1])
                userpho = str(row[2])
                useradd = str(row[3])
                shopname = str(row[4])
                shopadd = str(row[5])
                wx.StaticText(dialogro.panel, -1, orderid, (20, h))
                wx.StaticText(dialogro.panel, -1, username, (120, h))
                wx.StaticText(dialogro.panel, -1, userpho, (220, h))
                wx.StaticText(dialogro.panel, -1, useradd, (320, h))
                wx.StaticText(dialogro.panel, -1, shopname, (420, h))
                wx.StaticText(dialogro.panel, -1, shopadd, (520, h))
            # self.panel.Refresh()
            #dialogwo.Bind(wx.EVT_RADIOBUTTON, dialogwo.OnRadio)
            #print(data)
            conn.commit()
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
        dialogro.Show()

class MyDialogod(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"在售菜品", pos=wx.DefaultPosition,
                           size=wx.Size(400, 400), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        fgSizer1 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText16 = wx.StaticText(self, wx.ID_ANY, u"菜品号", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)
        fgSizer1.Add(self.m_staticText16, 0, wx.ALL, 5)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"菜名", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)
        fgSizer1.Add(self.m_staticText17, 0, wx.ALL, 5)

        self.m_staticText18 = wx.StaticText(self, wx.ID_ANY, u"价格", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText18.Wrap(-1)
        fgSizer1.Add(self.m_staticText18, 0, wx.ALL, 5)

        conn = pymysql.connect("localhost", "root", "password", "baoleme", charset='utf8')
        cursor = conn.cursor()
        #name = self.t1.GetValue()
        #print(name)
        #name = '%' + name + '%'
        try:
            global shop
            sql = "SELECT dishid,dishname,price FROM dish WHERE shopid=%s "
            t = cursor.execute(sql, shop)
            #print(t)
            rs = cursor.fetchall()
            print(rs)
            #h = 80
            for row in rs:
                #h = h + 20
                id = str(row[0])
                name = str(row[1])
                price = str(row[2])
                self.m_radioBtn5 = wx.RadioButton(self, wx.ID_ANY, id, wx.DefaultPosition, wx.DefaultSize, 0)
                fgSizer1.Add(self.m_radioBtn5, 0, wx.ALL, 5)
                self.m_staticText18 = wx.StaticText(self, wx.ID_ANY, name, wx.DefaultPosition, wx.DefaultSize, 0)
                self.m_staticText18.Wrap(-1)
                fgSizer1.Add(self.m_staticText18, 0, wx.ALL, 5)
                self.m_staticText18 = wx.StaticText(self, wx.ID_ANY, price, wx.DefaultPosition, wx.DefaultSize, 0)
                self.m_staticText18.Wrap(-1)
                fgSizer1.Add(self.m_staticText18, 0, wx.ALL, 5)
            self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiogroup)
            #self.panel.Refresh()
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
        self.m_button11 = wx.Button(self, wx.ID_ANY, u"修改", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.m_button11, 0, wx.ALL, 5)
        self.m_button11.Bind(wx.EVT_BUTTON, MyDialogcd(None).OnClick)

        self.m_button12 = wx.Button(self, wx.ID_ANY, u"下架", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.m_button12, 0, wx.ALL, 5)
        self.m_button12.Bind(wx.EVT_BUTTON, self.out)

        self.SetSizer(fgSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def out(self,e):
        conn = pymysql.connect("localhost", "root", "password", "baoleme", charset='utf8')
        cursor = conn.cursor()
        # name = self.t1.GetValue()
        # print(name)
        # name = '%' + name + '%'
        try:
            global shop
            sql = "delete  FROM dish WHERE dishid=%s "
            t = cursor.execute(sql, self.idon)
            print(t)
            print(self.idon)

            conn.commit()
            dial = wx.MessageDialog(None, '成功下架!', '结果', wx.YES_NO)
            dial.ShowModal()  # 显示对话框
            self.Close()
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def OnRadiogroup(self, e):
        cb = e.GetEventObject()
        self.idon=cb.GetLabel()
        global id
        id = self.idon
        #print(self.cb1.GetValue())
        #print (cb.GetLabel(), ' is clicked', cb.GetValue())

    def OnClick(self, e):
        Dialogod = MyDialogod(None)
        Dialogod.ShowModal()

class MyDialogcd(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"菜品修改", pos=wx.DefaultPosition, size=wx.Size(302, 250),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "请输入新名称：", (20, 20))
        # 可编辑文本框的创建使用wx.TextCtrl，默认情况下，文本框只能编辑一行文字（无论文字多长均不换行）
        self.t1 = wx.TextCtrl(self.panel, pos=(130, 20), size=(120, 25))

        wx.StaticText(self.panel, -1, "请输入新价格：", (20, 80))
        self.t2 = wx.TextCtrl(self.panel, pos=(130, 80), size=(120, 25))



    def OnClick(self, e):
        Dialogpu = MyDialogcd(None)
        btn = wx.Button(parent=Dialogpu.panel, label="修改", pos=(20, 150), size=(100, 45), style=wx.BORDER_MASK)
        btn.Bind(wx.EVT_BUTTON, Dialogpu.insert)
        Dialogpu.ShowModal()

    def insert(self, event):
        conn = pymysql.connect("localhost", "root", "password", "baoleme",charset='utf8')
        cursor = conn.cursor()
        global id
        print(id)
        name = self.t1.GetValue().encode('utf8') #注意GetValue()获取的是unicode编码，
        price = self.t2.GetValue().encode('utf8') #你使用的#coding=utf8，那就对获取的数据.encode('utf8')重新编码
        data = (name, price,id)

        try:
            sql = "update dish set dishname=%s ,price=%s where dishid=%s"
            cursor.execute(sql, data)
            conn.commit() #提交给后台数据库
            dial = wx.MessageDialog(None, '成功修改!', '结果', wx.YES_NO)  # 创建一个带按钮的消息框, 语法是(self, 框中内容, 框标题, ID)
            dial.ShowModal()  # 显示对话框
            self.Close()
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

class Mydialogsd(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"订单信息", pos=wx.DefaultPosition, size=wx.Size(500, 400),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "查询菜名（查询所有则置空）：", (20, 20))
        self.t1 = wx.TextCtrl(self.panel, pos=(200, 20), size=(120, 25))
        # btn = wx.Button(parent=self.panel, label="查询", pos=(240, 20), size=(70, 25))
        # btn.Bind(wx.EVT_BUTTON, self.find)
        wx.StaticText(self.panel, -1, "菜品id", (20, 60))
        wx.StaticText(self.panel, -1, "菜名", (120, 60))
        wx.StaticText(self.panel, -1, "商家", (220, 60))
        wx.StaticText(self.panel, -1, "价格", (320, 60))
        self.m_button11 = wx.Button(self.panel, wx.ID_ANY, u"进入所在店铺", (20, 320))
        self.m_button11.Bind(wx.EVT_BUTTON, MyDialogus(None).OnClick)
        #self.m_button12 = wx.Button(self.panel, wx.ID_ANY, u"下架", (120, 160))
        # self.m_button12.Bind(wx.EVT_BUTTON, self.out)
    #def Onc(self,e):

    def OnClick(self, e):
        dialogsd = Mydialogsd(None)
        btn = wx.Button(parent=dialogsd.panel, label="查询", pos=(350, 20), size=(70, 25))
        btn.Bind(wx.EVT_BUTTON, dialogsd.find)
        dialogsd.ShowModal()

    def find(self, event):
        conn = pymysql.connect("localhost", "root", "password", "baoleme",charset='utf8')
        cursor = conn.cursor()
        name=self.t1.GetValue()
        print(name)
        name='%'+name+'%'
        try:
            sql = "SELECT * FROM dish WHERE dishname LIKE %s "
            t = cursor.execute(sql,name)
            #print(t)
            rs = cursor.fetchall()
            #print(rs)
            h = 80
            for row in rs:
                    h = h + 20
                    dish_id = str(row[0])
                    dishname = str(row[1])
                    shopname = str(row[2])
                    price = str(row[3])
                    self.m_radioBtn5 = wx.RadioButton(self.panel, wx.ID_ANY, dish_id, (20,h))
                    wx.StaticText(self.panel, -1, dishname, (120, h))
                    wx.StaticText(self.panel, -1, shopname, (220, h))
                    wx.StaticText(self.panel, -1, price, (320, h))
            #self.panel.Refresh()
            self.Bind(wx.EVT_RADIOBUTTON, self.OnRadio)
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def OnRadio(self,e):
        r=e.GetEventObject()
        global shop
        did=r.GetLabel()
        conn = pymysql.connect("localhost", "root", "password", "baoleme", charset='utf8')
        cursor = conn.cursor()
        print('did')
        print(did)
        try:
            sql = "SELECT shopid FROM dish WHERE dishid = %s "
            t = cursor.execute(sql, did)
            # print(t)
            rs = cursor.fetchone()
            shop=str(rs[0])
            print('shop')
            print(shop)
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

class Mydialogss(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"订单信息", pos=wx.DefaultPosition, size=wx.Size(500, 400),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "查询店名（查询所有则置空）：", (20, 20))
        self.t1 = wx.TextCtrl(self.panel, pos=(200, 20), size=(120, 25))
        # btn = wx.Button(parent=self.panel, label="查询", pos=(240, 20), size=(70, 25))
        # btn.Bind(wx.EVT_BUTTON, self.find)
        wx.StaticText(self.panel, -1, "商家名", (20, 60))
        wx.StaticText(self.panel, -1, "地址", (120, 60))
        #wx.StaticText(self.panel, -1, "商家", (220, 60))
        #wx.StaticText(self.panel, -1, "价格", (320, 60))
        self.m_button11 = wx.Button(self.panel, wx.ID_ANY, u"进店", (20, 320))
        self.m_button11.Bind(wx.EVT_BUTTON, MyDialogus(None).OnClick)
        #self.m_button12 = wx.Button(self.panel, wx.ID_ANY, u"下架", (120, 160))
        # self.m_button12.Bind(wx.EVT_BUTTON, self.out)
    def OnClick(self, e):
        dialogss = Mydialogss(None)
        btn = wx.Button(parent=dialogss.panel, label="查询", pos=(350, 20), size=(70, 25))
        btn.Bind(wx.EVT_BUTTON, dialogss.find)
        dialogss.ShowModal()

    def find(self, event):
        conn = pymysql.connect("localhost", "root", "password", "baoleme",charset='utf8')
        cursor = conn.cursor()
        name=self.t1.GetValue()
        print(name)
        name='%'+name+'%'
        try:
            sql = "SELECT * FROM shop WHERE shopid LIKE %s "
            t = cursor.execute(sql,name)
            #print(t)
            rs = cursor.fetchall()
            #print(rs)
            h = 80
            for row in rs:
                    h = h + 20
                    dish_id = str(row[0])
                    dishname = str(row[1])
                    shopname = str(row[2])
                    #price = str(row[3])
                    self.m_radioBtn5 = wx.RadioButton(self.panel, wx.ID_ANY, dish_id, (20,h))
                    wx.StaticText(self.panel, -1, dishname, (120, h))
                    #wx.StaticText(self.panel, -1, shopname, (220, h))
                    #wx.StaticText(self.panel, -1, price, (320, h))
            #self.panel.Refresh()
            self.Bind(wx.EVT_RADIOBUTTON, self.OnRadio)
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def OnRadio(self,e):
        r=e.GetEventObject()
        global shop
        did=r.GetLabel()
        conn = pymysql.connect("localhost", "root", "password", "baoleme", charset='utf8')
        cursor = conn.cursor()
        print('did')
        print(did)
        try:
            sql = "SELECT shopid FROM shop WHERE shopid = %s "
            t = cursor.execute(sql, did)
            # print(t)
            rs = cursor.fetchone()
            shop=str(rs[0])
            print('shop')
            print(shop)
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
class MyDialogso(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"订单", pos=wx.DefaultPosition, size=wx.Size(500, 400),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        #wx.StaticText(self.panel, -1, "买家电话：", (20, 20))
        #self.t1 = wx.TextCtrl(self.panel, pos=(90, 20), size=(120, 25))
        # btn = wx.Button(parent=self.panel, label="查询", pos=(240, 20), size=(70, 25))
        # btn.Bind(wx.EVT_BUTTON, self.find)
        wx.StaticText(self.panel, -1, "订单编号", (20, 60))
        wx.StaticText(self.panel, -1, "订单金额", (120, 60))
        wx.StaticText(self.panel, -1, "配送骑手", (220, 60))
        wx.StaticText(self.panel, -1, "接单商家", (320, 60))

    def OnClick(self, e):
        dialogso = MyDialogso(None)
        btn = wx.Button(parent=dialogso.panel, label="确认送达", pos=(240, 20), size=(70, 25))
        btn.Bind(wx.EVT_BUTTON, dialogso.OnOk)
        #btn1 = wx.Button(parent=dialogsc.panel, label="全部结算", pos=(120, 20), size=(70, 25))
        #btn1.Bind(wx.EVT_BUTTON, dialogsc.OnOrder)
    #def find(self, event):
        conn = pymysql.connect("localhost", "root", "password", "baoleme", charset='utf8')
        cursor = conn.cursor()
        #data=(user,'0')
        #print('shu')
        #print(shop)
        #print(user)
        try:
            sql = "select orderid,cost,raiderid,shopid from orders where userid=%s and ok ='0'"
            t=cursor.execute(sql,user)
            rs = cursor.fetchall()
            print('rs')
            #print('tt')
            print(user)
            print(rs)
            h = 80
            for row in rs:
                h = h + 20
                dish_id = str(row[0])
                dishname = str(row[1])
                shopname = str(row[2])
                price = str(row[3])
                m_radioBtn5 = wx.RadioButton(dialogso.panel, wx.ID_ANY, dish_id, (20, h))
                wx.StaticText(dialogso.panel, -1, dishname, (120, h))
                wx.StaticText(dialogso.panel, -1, shopname, (220, h))
                wx.StaticText(dialogso.panel, -1, price, (320, h))
            # self.panel.Refresh()
            dialogso.Bind(wx.EVT_RADIOBUTTON, dialogso.OnRadio)
            #print(data)
            conn.commit()
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
        dialogso.Show()
    def OnRadio(self, e):
            r = e.GetEventObject()
            self.oid = r.GetLabel()
            print('ra')
            print(self.oid)
    def OnOk(self,e):
            #print('delete')
            print(self.oid)
            conn = pymysql.connect("localhost", "root", "password", "baoleme", charset='utf8')
            cursor = conn.cursor()
            #print('did')
            #print(did)
            #data=(raider,self.oid)
            try:
                print(self.oid)
                sql = "update orders set ok='1' where orderid=%s"
                t = cursor.execute(sql, self.oid)
                print('st')
                print(t)
                #rs = cursor.fetchone()
                #shop = str(rs[0])
                #print('shop')
                #print(shop)
                conn.commit()
                dial = wx.MessageDialog(None, '订单已确认', '订单', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
                dial.ShowModal()  # 显示对话框
                self.Close()
            except:
                conn.rollback()
            finally:
                cursor.close()
                conn.close()

class MyDialogus(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"店铺", pos=wx.DefaultPosition, size=wx.Size(500, 400),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "查询菜名（查询所有则置空）：", (20, 20))
        self.t1 = wx.TextCtrl(self.panel, pos=(200, 20), size=(120, 25))
        # btn = wx.Button(parent=self.panel, label="查询", pos=(240, 20), size=(70, 25))
        # btn.Bind(wx.EVT_BUTTON, self.find)
        wx.StaticText(self.panel, -1, "菜品id", (20, 60))
        wx.StaticText(self.panel, -1, "菜名", (120, 60))
        #wx.StaticText(self.panel, -1, "商家", (220, 60))
        wx.StaticText(self.panel, -1, "价格", (320, 60))
        self.m_button11 = wx.Button(self.panel, wx.ID_ANY, u"加入购物车", (20, 320))
        self.m_button11.Bind(wx.EVT_BUTTON, self.OnCart)
        self.m_button12 = wx.Button(self.panel, wx.ID_ANY, u"查看购物车", (120, 320))
        self.m_button12.Bind(wx.EVT_BUTTON, MyDialogsc(None).OnClick)
    def OnClick(self, e):
        dialogus = MyDialogus(None)
        btn = wx.Button(parent=dialogus.panel, label="查询", pos=(350, 20), size=(70, 25))
        btn.Bind(wx.EVT_BUTTON, dialogus.find)
        dialogus.ShowModal()
        

    def find(self, event):
        conn = pymysql.connect("localhost", "root", "password", "baoleme",charset='utf8')
        cursor = conn.cursor()
        name=self.t1.GetValue()
        print(name)
        name='%'+name+'%'
        #global shop
        shopid=shop
        print('shopid')
        print(shopid)
        data=(name,shopid)
        try:
            sql = "SELECT * FROM dish join shop on dish.shopid=shop.shopid WHERE dishname LIKE %s and shop.shopid=%s "
            t = cursor.execute(sql,data)
            print("shop")
            print(shop)
            print("t")
            print(t)
            #print(t)
            rs = cursor.fetchall()
            #print(rs)
            h = 80
            for row in rs:
                    h = h + 20
                    dish_id = str(row[0])
                    dishname = str(row[1])
                    shopname = str(row[2])
                    price = str(row[3])
                    self.m_radioBtn5 = wx.RadioButton(self.panel, wx.ID_ANY, dish_id, (20,h))
                    wx.StaticText(self.panel, -1, dishname, (120, h))
                    #wx.StaticText(self.panel, -1, shopname, (220, h))
                    wx.StaticText(self.panel, -1, price, (320, h))
            #self.panel.Refresh()
            self.Bind(wx.EVT_RADIOBUTTON, self.OnRadio)
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
    #def OnCart(self,e):

    def OnRadio(self,e):
        r=e.GetEventObject()
        #global shop
        self.did=r.GetLabel()
        print(self.did)

    def OnCart(self, e):
        conn = pymysql.connect("localhost", "root", "password", "baoleme", charset='utf8')
        cursor = conn.cursor()
        #print('did')
        #print(did)
        data=(user,shop,self.did)
        try:
            sql = "insert into shopcart values(%s,%s,%s) "
            t = cursor.execute(sql,data)
            print('time')
            print(t)
            conn.commit()  # 提交给后台数据库
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

class MyDialogpu(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"修改密码", pos=wx.DefaultPosition, size=wx.Size(302, 250),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')
        '''
        wx.StaticText(self.panel, -1, "请输入原始密码：", (20, 20))
        # 可编辑文本框的创建使用wx.TextCtrl，默认情况下，文本框只能编辑一行文字（无论文字多长均不换行）
        self.t1 = wx.TextCtrl(self.panel, pos=(130, 20), size=(120, 25))
'''
        wx.StaticText(self.panel, -1, "请输入新密码：", (20, 80))
        self.t2 = wx.TextCtrl(self.panel, pos=(130, 80), size=(120, 25))


    def OnClick(self, e):
        Dialogpu = MyDialogpu(None)
        btn = wx.Button(parent=Dialogpu.panel, label="修改密码", pos=(20, 150), size=(100, 45), style=wx.BORDER_MASK)
        btn.Bind(wx.EVT_BUTTON, Dialogpu.insert)
        Dialogpu.ShowModal()

    def insert(self, event):
        conn = pymysql.connect("localhost", "root", "password", "baoleme",charset='utf8')
        cursor = conn.cursor()
        global user
        #oldkey = self.t1.GetValue().encode('utf8') #注意GetValue()获取的是unicode编码，
        newkey = self.t2.GetValue().encode('utf8') #你使用的#coding=utf8，那就对获取的数据.encode('utf8')重新编码
        data = (newkey, user)
        print(newkey)

        try:
            sql = "update user set keyword=%s where userid=%s"
            print(user)
            cursor.execute(sql, data)
            conn.commit() #提交给后台数据库
            print('shit')
            dial = wx.MessageDialog(None, '成功修改!', '结果', wx.YES_NO)  # 创建一个带按钮的消息框, 语法是(self, 框中内容, 框标题, ID)
            dial.ShowModal()  # 显示对话框
            self.Close()
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

class MyDialogsc(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"购物车", pos=wx.DefaultPosition, size=wx.Size(500, 400),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        #wx.StaticText(self.panel, -1, "买家电话：", (20, 20))
        #self.t1 = wx.TextCtrl(self.panel, pos=(90, 20), size=(120, 25))
        # btn = wx.Button(parent=self.panel, label="查询", pos=(240, 20), size=(70, 25))
        # btn.Bind(wx.EVT_BUTTON, self.find)
        wx.StaticText(self.panel, -1, "菜品id", (20, 60))
        wx.StaticText(self.panel, -1, "菜品名", (120, 60))
        wx.StaticText(self.panel, -1, "单价", (220, 60))
        wx.StaticText(self.panel, -1, "商店", (320, 60))

    def OnClick(self, e):
        dialogsc = MyDialogsc(None)
        btn = wx.Button(parent=dialogsc.panel, label="删除", pos=(240, 20), size=(70, 25))
        btn.Bind(wx.EVT_BUTTON, dialogsc.OnDel)
        btn1 = wx.Button(parent=dialogsc.panel, label="全部结算", pos=(120, 20), size=(70, 25))
        btn1.Bind(wx.EVT_BUTTON, dialogsc.OnOrder)


    #def find(self, event):
        conn = pymysql.connect("localhost", "root", "password", "baoleme", charset='utf8')
        cursor = conn.cursor()
        data=(shop,user)
        print('shu')
        print(shop)
        print(user)
        try:
            sql = "select dish.dishid,dishname,price,shopcart.shopid from shopcart join dish on dish.dishid=shopcart.dishid where shopcart.shopid=%s and userid=%s"
            t=cursor.execute(sql,data)
            rs = cursor.fetchall()
            #print('tt')
            #print(rs)
            h = 80
            for row in rs:
                h = h + 20
                dish_id = str(row[0])
                dishname = str(row[1])
                shopname = str(row[2])
                price = str(row[3])
                m_radioBtn5 = wx.RadioButton(dialogsc.panel, wx.ID_ANY, dish_id, (20, h))
                wx.StaticText(dialogsc.panel, -1, dishname, (120, h))
                wx.StaticText(dialogsc.panel, -1, shopname, (220, h))
                wx.StaticText(dialogsc.panel, -1, price, (320, h))
            # self.panel.Refresh()
            dialogsc.Bind(wx.EVT_RADIOBUTTON, dialogsc.OnRadio)
            print(data)
            sql = "SELECT sum(price) from shopcart join dish on dish.dishid=shopcart.dishid where shopcart.shopid=%s and userid=%s"
            cursor.execute(sql, data)
            rs = cursor.fetchone()
            dialogsc.cost = str(rs[0])
            ms='菜品总价为：'+dialogsc.cost+'元'
            wx.StaticText(dialogsc.panel, -1,ms, (360, 20))
            conn.commit()
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
        dialogsc.Show()
    def OnRadio(self, e):
            r = e.GetEventObject()
            self.did = r.GetLabel()
            print('ra')
            print(self.did)
    def OnDel(self,e):
            print('delete')
            print(self.did)
            conn = pymysql.connect("localhost", "root", "password", "baoleme", charset='utf8')
            cursor = conn.cursor()
            #print('did')
            #print(did)
            try:
                print(self.did)
                sql = "delete from shopcart where dishid=%s "
                t = cursor.execute(sql, self.did)
                print('st')
                print(t)
                #rs = cursor.fetchone()
                #shop = str(rs[0])
                #print('shop')
                #print(shop)
                conn.commit()
                dial = wx.MessageDialog(None, '删除成功', '购物车', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
                dial.ShowModal()  # 显示对话框
                self.Close()
            except:
                conn.rollback()
            finally:
                cursor.close()
                conn.close()

    def OnOrder(self, e):
        conn = pymysql.connect("localhost", "root", "password", "baoleme", charset='utf8')
        cursor = conn.cursor()
        # print('did')
        # print(did)
        data=(user,shop)
        try:
            #print(self.did)
            #sql = "SELECT sum(price) from shopcart join dish on dish.dishid=shopcart.dishid where userid=%s and shopcart.shopid=%s"
            #cursor.execute(sql, data)
            #rs = cursor.fetchone()
            #cost = str(rs[0])
            data0=(user,shop,self.cost)
            sql = "insert into orders (userid,shopid,cost,carriage)values(%s,%s,%s,5) "
            t = cursor.execute(sql,data0)
            #sql = "insert into order_detail (orderid,dishid)values(%s,%s) "
            #t = cursor.execute(sql, data0)
            print('t1')
            sql = "delete from shopcart where userid=%s and shopid=%s "
            t = cursor.execute(sql,data)
            print('t2')
            #print('st')
            print(t)
            # rs = cursor.fetchone()
            # shop = str(rs[0])
            # print('shop')
            # print(shop)
            conn.commit()
            ms='订单总价'+self.cost+'元'
            dial = wx.MessageDialog(None,ms, '订单已提交', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
            dial.ShowModal()  # 显示对话框
            self.Close()
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

class MyDialogto(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"订单", pos=wx.DefaultPosition, size=wx.Size(700, 400),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        #wx.StaticText(self.panel, -1, "买家电话：", (20, 20))
        #self.t1 = wx.TextCtrl(self.panel, pos=(90, 20), size=(120, 25))
        # btn = wx.Button(parent=self.panel, label="查询", pos=(240, 20), size=(70, 25))
        # btn.Bind(wx.EVT_BUTTON, self.find)
        wx.StaticText(self.panel, -1, "订单编号", (20, 60))
        wx.StaticText(self.panel, -1, "下单用户", (120, 60))
        wx.StaticText(self.panel, -1, "用户电话", (220, 60))
        wx.StaticText(self.panel, -1, "用户地址", (320, 60))
        wx.StaticText(self.panel, -1, "接单商店", (420, 60))
        wx.StaticText(self.panel, -1, "商店地址", (520, 60))

    def OnClick(self, e):
        dialogto = MyDialogto(None)
        btn = wx.Button(parent=dialogto.panel, label="接取", pos=(240, 20), size=(70, 25))
        btn.Bind(wx.EVT_BUTTON, dialogto.OnTake)
        #btn1 = wx.Button(parent=dialogsc.panel, label="全部结算", pos=(120, 20), size=(70, 25))
        #btn1.Bind(wx.EVT_BUTTON, dialogsc.OnOrder)


    #def find(self, event):
        conn = pymysql.connect("localhost", "root", "password", "baoleme", charset='utf8')
        cursor = conn.cursor()
        #data=(shop,user)
        #print('shu')
        #print(shop)
        #print(user)
        try:
            sql = "select orderid,user.userid,user.phone,user.address,shop.shopid,shop.address from orders join user on orders.userid=user.userid join shop on orders.shopid=shop.shopid where raiderid is null"
            t=cursor.execute(sql)
            rs = cursor.fetchall()
            print('rs')
            #print('tt')
            #print(rs)
            h = 80
            for row in rs:
                h = h + 20
                orderid = str(row[0])
                username = str(row[1])
                userpho = str(row[2])
                useradd = str(row[3])
                shopname = str(row[4])
                shopadd = str(row[5])
                m_radioBtn5 = wx.RadioButton(dialogto.panel, wx.ID_ANY, orderid, (20, h))
                wx.StaticText(dialogto.panel, -1, username, (120, h))
                wx.StaticText(dialogto.panel, -1, userpho, (220, h))
                wx.StaticText(dialogto.panel, -1, useradd, (320, h))
                wx.StaticText(dialogto.panel, -1, shopname, (420, h))
                wx.StaticText(dialogto.panel, -1, shopadd, (520, h))
            # self.panel.Refresh()
            dialogto.Bind(wx.EVT_RADIOBUTTON, dialogto.OnRadio)
            #print(data)
            '''
            sql = "SELECT sum(price) from shopcart join dish on dish.dishid=shopcart.dishid where shopcart.shopid=%s and userid=%s"
            cursor.execute(sql, data)
            rs = cursor.fetchone()
            dialogsc.cost = str(rs[0])
            ms='菜品总价为：'+dialogsc.cost+'元'
            wx.StaticText(dialogsc.panel, -1,ms, (360, 20))
            '''
            conn.commit()
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
        dialogto.Show()
    def OnRadio(self, e):
            r = e.GetEventObject()
            self.oid = r.GetLabel()
            print('ra')
            print(self.oid)
    def OnTake(self,e):
            print('delete')
            print(self.oid)
            conn = pymysql.connect("localhost", "root", "password", "baoleme", charset='utf8')
            cursor = conn.cursor()
            #print('did')
            #print(did)
            data=(raider,self.oid)
            try:
                print(self.oid)
                sql = "update orders set raiderid=%s where orderid=%s"
                t = cursor.execute(sql, data)
                print('st')
                print(t)
                #rs = cursor.fetchone()
                #shop = str(rs[0])
                #print('shop')
                #print(shop)
                conn.commit()
                dial = wx.MessageDialog(None, '订单已接取', '订单', wx.YES_NO)  # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
                dial.ShowModal()  # 显示对话框
                self.Close()
            except:
                conn.rollback()
            finally:
                cursor.close()
                conn.close()


if __name__ == "__main__":
    app = wx.App()
    Myframe(None).Show()
    app.MainLoop()
