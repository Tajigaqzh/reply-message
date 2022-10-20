import pandas as pd# 导入pandas数据分析库
import numpy as np# 导入科学计算基础包
from uiautomation import WindowControl, MenuControl# 导入自动化控制相关模块
import pyperclip


wx = WindowControl(Name="微信", searchDepth=1)  # 绑定名为微信的主窗口控件
wx.SwitchToThisWindow()  # 切换窗口
hw = wx.ListControl(Name="会话")# 寻找会话控件绑定
df = pd.read_excel("./关键词匹配文件.xlsx")# 通过pandas读取Excel文件
while True:# 循环等待消息
    we = hw.TextControl(searchDepth=4)# 查找未读消息
    if we.Name:# 加入存在未读消息
        we.Click(simulateMove=False)# 点击未读消息
        last_msg = wx.ListControl(Name='消息').GetChildren()[-1].Name# 读取最后一条消息
        msg = df.apply(lambda x: x['回复内容'] if x["关键词"] in last_msg else None,axis=1)# 判断是否存在关键词
        msg.dropna(axis=0, how='any', inplace=True)# 数据清洗，移除空白数据
        ar = np.array(msg).tolist()# 数组转字符串
        if ar:# 判断是否有关键词内容，如果有，则执行以下代码
            pyperclip.copy(ar[0])
            wx.SendKeys("{Ctrl}v", waitTime=0)
            wx.SendKeys("{Enter}", waitTime=0)# 回车发送消息
            wx.TextControl(SubName=ar[0][:5]).RightClick()# 通过消息匹配检索会话栏中的联系人并右击
        else:# 如果没有关键词内容，则执行以下代码
            wx.TextControl(SubName=last_msg[:5]).RightClick()
        ment = MenuControl(ClassName="CMenuWnd")# 匹配右击控件
        ment.TextControl(Name="不显示聊天").Click()# 点击右击控件中的不显示聊天


