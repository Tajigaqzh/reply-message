import uiautomation

window2 = uiautomation.WindowControl(searchDepth=1, Name='window2')#search 2 times
sub = window2.Control(searchDepth=1, Name='2-4')# search 4 times
edit = sub.EditControl(searchDepth=1, Name='myedit2')# search 2 times
edit.SendKeys('hi')