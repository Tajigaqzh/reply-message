# python自动回复消息
初始化项目啊，需要完善

## automation.py命令
example:
        python automation.py -t
args:
-t      delay time, default 3 seconds, begin to enumerate after Value seconds, this must be an integer
        you can delay a few seconds and make a window active so automation can enumerate the 
active window
延迟秒数
-d      enumerate tree depth, this must be an integer, if it is null, enumerate the whole tree
枚举目录树的深度
-r      enumerate from root:Desktop window, if it is null, enumerate from foreground window 
从桌面开始枚举
-f      enumerate from focused control, if it is null, enumerate from foreground window      
从控制窗口开始枚举，如果为空从桌面枚举
-c      enumerate the control under cursor, if depth is < 0, enumerate from its ancestor up to depth
鼠标控制的位置枚举
-a      show ancestors of the control under cursor
展示坐标
-n      show control full name, if it is null, show first 30 characters of control's name in 
console,
        always show full name in log file @AutomationLog.txt

-p      show process id of controls


用法详情[点击链接](https://github.com/yinkaisheng/Python-UIAutomation-for-Windows/blob/master/readme_cn.md)
