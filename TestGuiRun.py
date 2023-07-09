import wx
import time
from VideoDiff import *
class MyFrame(wx.Frame):
	def __init__(self, parent, id):
		wx.Frame.__init__(self, parent, id, 'VideoDiff', size=(400, 300))
		# 创建面板
		panel = wx.Panel(self)
		# 创建确定和取消按钮，并绑定事件
		self.bt_confirm = wx.Button(panel, label='确定', pos=(105, 130))
		self.bt_cancel = wx.Button(panel, label='取消', pos=(195, 130))
		self.bt_confirm.Bind(wx.EVT_BUTTON, self.OnclickSubmit)
		self.bt_cancel.Bind(wx.EVT_BUTTON, self.OnclickCancel)
		# 创建输入框
		self.title = wx.StaticText(panel, label="请输入两个视频路径", pos=(140, 20))
		self.labelVideoPathA = wx.StaticText(panel, label="视频A路径：", pos=(50, 50))
		self.labelVideoPathB = wx.StaticText(panel, label="视频B路径：", pos=(50, 90))
		self.textVideoPathA = wx.TextCtrl(panel, pos=(120, 50), size=(235, 25), style=wx.TE_LEFT)
		self.textVideoPathB = wx.TextCtrl(panel, pos=(120, 90), size=(235, 25), style=wx.TE_LEFT)

	def OnclickSubmit(self, event):
		message = ""
		username = self.textVideoPathA.GetValue()
		password = self.textVideoPathB.GetValue()

		diff = VideoDiff(username,password,12)
		result = diff.videoDiff()

		if len(result) == 0:
			message = "运行失败,请检查路径重试"
		else:
			for key, value in result.items():
				if value <= 0.96:
					message ="视频不相同，请检查第"+str(key)+"秒视频"
					break
				else:
					message ="视频相同"

		time.sleep(2)
		wx.MessageBox(message)  # 弹出提示框

	def OnclickCancel(self, event):
		self.textVideoPathA.SetValue("")  # 清空输入框
		self.textVideoPathB.SetValue("")


if __name__ == "__main__":
	app = wx.App()
	frame = MyFrame(parent=None, id=-1)
	frame.Show()
	app.MainLoop()
