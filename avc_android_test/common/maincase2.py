# -*- coding:utf-8 -*-
from airtest.core.api import *
from airtest import aircv
from airtest.core.cv import Predictor
from PIL import Image, ImageChops
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.0/bin/tesseract'
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import connect_device

dev2 = connect_device('Android:///57a1a1bd?cap_method=javacap&touch_method=adb')

poco_2 = AndroidUiautomationPoco(dev2, use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)


# setCurrentDevice(1)代表360
class Android_AVC2():
    def __init__(self):
        self.interval = 2

    # 当前设备(0:oppo ,1:360)
    def setCurrentDevice(self, device):
        set_current(device)

    # 启动avc
    def startAVC(self, packageName):
        start_app(packageName)
        # wait(Template(r"resource/images/tpl1568208771836.png", record_pos=(-0.002, -0.009), resolution=(1080, 1920)))

    # 输入房间名称
    def inputChannelName_2(self, channelname):
        poco_2("io.agora.vcall:id/editRoomName").click()
        poco_2("io.agora.vcall:id/editRoomName").set_text("")
        text(channelname)
        sleep(self.interval)

    # 输入密码
    def inputPassword_2(self, password_2):
        poco_2("io.agora.vcall:id/editRoomPwd").click()
        poco_2("io.agora.vcall:id/editRoomPwd").set_text("")
        text(password_2)
        sleep(self.interval)

    # 加入频道
    def joinChannel_2(self):
        poco_2("io.agora.vcall:id/btJoin").click()

    # 点击查看版本号
    def checkversion_2(self):
        poco_2("io.agora.vcall:id/version").click()
        sleep(self.interval)

    # 点击设置输入昵称
    def nick_comfirm_2(self, nickname):
        poco_2("io.agora.vcall:id/btSettings").click()
        poco_2("io.agora.vcall:id/editNickName").click()
        poco_2("io.agora.vcall:id/editNickName").set_text("")
        text(nickname)
        sleep(self.interval)

    # 点击返回
    def settings_back_2(self):
        poco_2("io.agora.vcall:id/btBack").click()
        sleep(self.interval)

    # 点击设置打开摄像头
    def mutelocalvideo_channelout_2(self):
        poco_2("io.agora.vcall:id/btSettings").click()
        poco_2("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/itemCamera").offspring("io.agora.vcall:id/btSwitch").click()
        sleep(self.interval)

    # 返回键
    def key_back(self):
        keyevent("BACK")
        sleep(self.interval)

    # home键
    def home(self):
        keyevent("HOME")
        sleep(self.interval)

    # 清除房间名
    def clearRoomName_2(self):
        poco_2("io.agora.vcall:id/editRoomName").click()
        poco_2("io.agora.vcall:id/editRoomName").set_text("")
        sleep(self.interval)

    # 清除房间密码
    def clearRoomPwd_2(self):
        poco_2("io.agora.vcall:id/editRoomPwd").click()
        poco_2("io.agora.vcall:id/editRoomPwd").set_text("")
        sleep(self.interval)

    # 清除昵称
    def clearNickName_2(self):
        poco_2("io.agora.vcall:id/editNickName").click()
        poco_2("io.agora.vcall:id/editNickName").set_text("")
        sleep(self.interval)

    """
    关于设置中的所有功能选项
    """

    # 点击设置
    def bt_settings_2(self):
        poco_2("io.agora.vcall:id/btSettings").click()
        sleep(self.interval)

    # 关闭摄像头
    def Turn_off_the_camera_2(self):
        poco_2("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/itemCamera").child("android.view.ViewGroup").click()
        sleep(self.interval)

    # 关闭麦克风
    def Turn_off_the_maicrophone_2(self):
        poco_2("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/itemMicrophone").child("android.view.ViewGroup").click()

    # 夜间模式
    def Night_mode_2(self):
        poco_2("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/darkTheme").child("android.view.ViewGroup").click()
        sleep(self.interval)

    """
    屏幕分辨率设置
    """

    def Resolution_360p_2(self):
        poco_2("io.agora.vcall:id/resolutionIcon").click()
        sleep(self.interval)

    def Resolution_480p_2(self):
        poco_2("io.agora.vcall:id/resolutionIcon").click()
        sleep(self.interval)

    def Resolution_720p_2(self):
        poco_2("io.agora.vcall:id/resolutionIcon").click()
        sleep(self.interval)

    # 日志上传
    def log_upload_2(self):
        poco_2("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/uploadLog").child("android.view.ViewGroup").click()

    """
    头像上传
    """

    def Avatar_upload_2(self):
        poco_2("io.agora.vcall:id/changeAvatar").click()
        poco_2("io.agora.vcall:id/choose1").click()
        poco_2("com.oppo.camera:id/shutter_button").click()
        poco_2("com.oppo.camera:id/btn_done").click()
        sleep(self.interval)

    """
    房间内的状态栏设置
    """

    # 房间内点击恢复状态栏
    def Recovery_status_bar_2(self):
        poco_2("io.agora.vcall:id/mediaImage").click()

    # 窗口切换
    def Window_switching_2(self):
        poco_2("io.agora.vcall:id/small_bg").click()

    # 关闭音频
    def Turn_off_audio_2(self):
        poco_2("android.widget.LinearLayout").offspring("io.agora.vcall:id/localAudio").child(
            "io.agora.vcall:id/mediaImage").click()

    # 关闭视频
    def Close_vido_2(self):
        poco_2("android.widget.LinearLayout").offspring("io.agora.vcall:id/localVideo").child(
            "io.agora.vcall:id/mediaImage").click()

    """
    人员列表相关操作
    """

    def list_of_pepole_2(self):
        poco_2("io.agora.vcall:id/icon").click()
        sleep(self.interval)

    # 选择确定
    def Choose_OK_2(self):
        poco_2("android:id/button1").click()

    # 选择拒绝
    def Choose_NO_2(self):
        poco_2("android:id/button2").click()

    # 选择属性(更具人数元素去获取)
    def Select_attribute_0(self):
        poco_2("io.agora.vcall:id/more").click()
        sleep(self.interval)

    def Select_attribute_1(self):
        poco_2("android.widget.LinearLayout").offspring("io.agora.vcall:id/part_recy").child(
            "android.view.ViewGroup")[
            1].child("io.agora.vcall:id/more").click()

    # 关闭音频
    def Click_audio_2(self):
        poco_2("io.agora.vcall:id/audioActionText").click()
        sleep(self.interval)

    # 关闭视频
    def Click_Vido_2(self):
        poco_2("io.agora.vcall:id/videoActionText").click()
        sleep(self.interval)

    # 踢人
    def Kicking_people_2(self):
        poco_2("io.agora.vcall:id/hangUpText").click()
        poco_2("android:id/button1").click()

    """
    聊天
    """

    # 点击消息列表
    def Message_list_2(self):
        poco_2("io.agora.vcall:id/chatImage").click()

    # 点击链接
    def link_2(self):
        poco_2("io.agora.vcall:id/chatContent").click()
        sleep(self.interval)

    # 聊天输入信息
    def To_chat_with_2(self, information):
        poco_2("io.agora.vcall:id/input").click()
        poco_2("io.agora.vcall:id/input").set_text("")
        text(information)
        sleep(self.interval)

    # 聊天-发送
    def Send_2(self):
        poco_2("io.agora.vcall:id/sendInclude").click()
        sleep(self.interval)

    """
    挂断电话，退出频道
    """

    # 离开频道
    def leaveChannel_2(self):
        poco_2("io.agora.vcall:id/hangUp").click()
        sleep(self.interval)

    """
    房间设置
    """

    # 申请/放弃主持人
    def Application_host_2(self):
        poco_2("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/scrollView").offspring("io.agora.vcall:id/roomHost").child(
            "android.view.ViewGroup").click()
        sleep(self.interval)

    # 日志上传
    def Log_upload_2(self):
        poco_2("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/scrollView").offspring("io.agora.vcall:id/uploadLog").child(
            "android.view.ViewGroup").click()
        sleep(self.interval)

    # 关闭/打开音频
    def Audio_2(self):
        poco_2("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/scrollView").offspring("io.agora.vcall:id/itemMicrophone").child(
            "android.view.ViewGroup").click()
        sleep(self.interval)

    # 关闭/打开视频
    def Video_2(self):
        poco_2("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/scrollView").offspring("io.agora.vcall:id/itemCamera").child(
            "android.view.ViewGroup").click()
        sleep(self.interval)

    # 本机点击设置
    def settings_2(self):
        poco_2("设置").click()

    # 关网
    def Network_settings_2(self):
        poco_2("android.widget.FrameLayout").offspring("com.android.settings:id/dashboard_container").child(
            "com.android.settings:id/category")[0].child("com.android.settings:id/category_content").child(
            "android.widget.FrameLayout")[1].offspring("com.android.settings:id/icon").click()
        poco_2("com.android.settings.wifi:id/switchButton").click()

    # 开网
    def Open_Network_2(self):
        poco_2("com.android.settings.wifi:id/switchButton").click()

    # 点击房间设置打开开发者模式
    def Open_developer_mode(self):
        touch(Template(r"a/b/tpl1574309054241.png", record_pos=(0.011, -0.852), resolution=(1080, 2160)), times=6)

        poco_2("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/scrollView").offspring("io.agora.vcall:id/developerMenu").child(
            "android.view.ViewGroup").click()

    # RTM断开/连接
    def RTM_disconnect(self):
        poco_2("android.widget.LinearLayout").offspring("io.agora.vcall:id/developer_container").offspring(
            "io.agora.vcall:id/connRtm").offspring("io.agora.vcall:id/btSwitch").click()

    # 打开开发者
    def developer_mode(self):
        poco_2("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/scrollView").offspring("io.agora.vcall:id/developerMenu").child(
            "android.view.ViewGroup").click()
