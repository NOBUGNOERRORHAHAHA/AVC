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

dev1 = connect_device('Android:///433edc01?cap_method=javacap&touch_method=adb')

poco_1 = AndroidUiautomationPoco(dev1, use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)


# setCurrentDevice(0)代表oppo
class Android_AVC():
    def __init__(self):
        self.interval = 2

    # 当前设备(0:oppo ,1:360)
    def setCurrentDevice(self, device):
        set_current(device)

    # 安装app
    def install_software(self):
        install("apk/avc-standalone-4.0.0.1795.apk")

    # 输入安装密码
    def Installation_password(self):
        poco_1("com.coloros.safecenter:id/et_login_passwd_edit").click()
        text("bestvoip123")
        poco_1("android:id/button1").click()

    # 启动avc
    def startAVC(self, packageName):
        start_app(packageName)
        # wait(Template(r"resource/images/tpl1568208771836.png", record_pos=(-0.002, -0.009), resolution=(1080, 1920)))
        sleep(self.interval)

    # 输入房间名称
    def inputChannelName(self, channelname):
        poco_1("io.agora.vcall:id/editRoomName").click()
        poco_1("io.agora.vcall:id/editRoomName").set_text("")
        text(channelname)
        sleep(self.interval)

    # 输入密码
    def inputPassword(self, password):
        poco_1("io.agora.vcall:id/editRoomPwd").click()
        poco_1("io.agora.vcall:id/editRoomPwd").set_text("")
        text(password)
        sleep(self.interval)

    # 加入频道
    def joinChannel(self):
        poco_1("io.agora.vcall:id/btJoin").click()

    # 点击查看版本号
    def checkversion(self):
        poco_1("io.agora.vcall:id/version").click()
        sleep(self.interval)

    # 点击设置输入昵称
    def nick_comfirm(self, nickname):
        poco_1("io.agora.vcall:id/btSettings").click()
        poco_1("io.agora.vcall:id/editNickName").click()
        poco_1("io.agora.vcall:id/editNickName").set_text("")
        text(nickname)
        sleep(self.interval)

    # 点击返回
    def settings_back(self):
        poco_1("io.agora.vcall:id/btBack").click()
        sleep(self.interval)

    # 点击设置打开摄像头
    def mutelocalvideo_channelout(self):
        poco_1("io.agora.vcall:id/btSettings").click()
        poco_1("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/itemCamera").offspring("io.agora.vcall:id/btSwitch").click()
        sleep(self.interval)

    # 得到文字图片
    def getWordsInImage(self, image_path):
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang='chi_sim')
        return text

    # 得到图片大小
    def getImageSize(self, img_path):
        img = Image.open(img_path)
        width = img.size[0]
        height = img.size[1]
        print("width:%s,height:%s" % (width, height))
        return width, height

    # 获取截图的大小
    def getCustomizeImage(self, origin_image_path, new_image_path, left, upper, right, lower):
        """
        :param origin_image_path: 原始图片的路径
        :param new_image_path: 图片裁剪后的路径
        :param left: 左 坐标
        :param upper: 上 坐标
        :param right: 右 坐标
        :param lower: 下 坐标
        :return:
        """
        img = Image.open(origin_image_path)
        cropped = img.crop((left, upper, right, lower))
        cropped.save(new_image_path)

    def key_back(self):
        keyevent("BACK")
        sleep(self.interval)

    def home(self):
        keyevent("HOME")
        sleep(self.interval)

    # 清除房间名
    def clearRoomName(self):
        poco_1("io.agora.vcall:id/editRoomName").click()
        poco_1("io.agora.vcall:id/editRoomName").set_text("")
        sleep(self.interval)

    # 清除房间密码
    def clearRoomPwd(self):
        poco_1("io.agora.vcall:id/editRoomPwd").click()
        poco_1("io.agora.vcall:id/editRoomPwd").set_text("")
        sleep(self.interval)

    # 清除昵称
    def clearNickName(self):
        poco_1("io.agora.vcall:id/editNickName").click()
        poco_1("io.agora.vcall:id/editNickName").set_text("")
        sleep(self.interval)

    """
    关于设置中的所有功能选项
    """

    # 点击设置
    def bt_settings(self):
        poco_1("io.agora.vcall:id/btSettings").click()
        sleep(self.interval)

    # 关闭摄像头
    def Turn_off_the_camera(self):
        poco_1("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/itemCamera").child("android.view.ViewGroup").click()
        sleep(self.interval)

    # 关闭麦克风
    def Turn_off_the_maicrophone(self):
        poco_1("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/itemMicrophone").child("android.view.ViewGroup").click()

    # 夜间模式
    def Night_mode(self):
        poco_1("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/darkTheme").child("android.view.ViewGroup").click()
        sleep(self.interval)

    """
    屏幕分辨率设置
    """

    def Resolution_360p(self):
        poco_1("io.agora.vcall:id/resolutionIcon").click()
        sleep(self.interval)

    def Resolution_480p(self):
        poco_1("io.agora.vcall:id/resolutionIcon").click()
        sleep(self.interval)

    def Resolution_720p(self):
        poco_1("io.agora.vcall:id/resolutionIcon").click()
        sleep(self.interval)

    # 日志上传
    def log_upload(self):
        poco_1("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/uploadLog").child("android.view.ViewGroup").click()

    """
    头像上传
    """

    def Avatar_upload(self):
        poco_1("io.agora.vcall:id/changeAvatar").click()
        poco_1("io.agora.vcall:id/choose1").click()
        poco_1("com.oppo.camera:id/shutter_button").click()
        poco_1("com.oppo.camera:id/btn_done").click()
        sleep(self.interval)

    def compare_images(self, path_one, path_two):  # 文件1的路径，文件2的路径，生成比较后不同的图片文件路径
        image_one = Image.open(path_one)
        image_two = Image.open(path_two)

        try:
            diff = ImageChops.difference(image_one, image_two)
            if diff.getbbox() is None:
                # 图片间没有任何不同则直接退出
                print("We are the same!")
            else:
                print("图片不同")

        except ValueError as e:
            text = ("表示图片大小和box对应的宽度不一致，参考API说明：Pastes another image into this image."
                    "The box argument is either a 2-tuple giving the upper left corner, a 4-tuple defining the left, upper, "
                    "right, and lower pixel coordinate, or None (same as (0, 0)). If a 4-tuple is given, the size of the pasted "
                    "image must match the size of the region.使用2纬的box避免上述问题")
            print("【{0}】{1}".format(e, text))

    """
    房间内的状态栏设置
    """

    # 房间内点击恢复状态栏
    def Recovery_status_bar(self):
        poco_1("io.agora.vcall:id/mediaImage").click()

    # 关闭音频
    def Turn_off_audio(self):
        poco_1("android.widget.LinearLayout").offspring("io.agora.vcall:id/localAudio").child(
            "io.agora.vcall:id/mediaImage").click()

    # 关闭视频
    def Close_vido(self):
        poco_1("android.widget.LinearLayout").offspring("io.agora.vcall:id/localVideo").child(
            "io.agora.vcall:id/mediaImage").click()

    # 窗口切换
    def Window_switching(self):
        poco_1("io.agora.vcall:id/small_bg").click()

    """
    人员列表相关操作
    """

    def list_of_pepole(self):
        poco_1("io.agora.vcall:id/icon").click()
        sleep(self.interval)

    # 选择确定
    def Choose_OK(self):
        poco_1("android:id/button1").click()

    # 选择拒绝
    def Choose_NO(self):
        poco_1("android:id/button2").click()

    # 选择属性(更具人数元素去获取)
    def Select_attribute_0(self):
        poco_1("io.agora.vcall:id/more").click()
        sleep(self.interval)

    def Select_attribute_1(self):
        poco_1("android.widget.LinearLayout").offspring("io.agora.vcall:id/part_recy").child("android.view.ViewGroup")[
            1].child("io.agora.vcall:id/more").click()

    # 关闭音频
    def Click_audio(self):
        poco_1("io.agora.vcall:id/audioActionText").click()

    # 关闭视频
    def Click_Vido(self):
        poco_1("io.agora.vcall:id/videoActionText").click()

    # 踢人
    def Kicking_people(self):
        poco_1("io.agora.vcall:id/hangUpText").click()
        poco_1("android:id/button1").click()

    """
    聊天
    """

    # 点击消息列表
    def Message_list(self):
        poco_1("io.agora.vcall:id/chatImage").click()

    # 点击链接
    def link(self):
        poco_1("io.agora.vcall:id/chatContent").click()
        sleep(self.interval)

    # 聊天输入信息
    def To_chat_with(self, information):
        poco_1("io.agora.vcall:id/input").click()
        poco_1("io.agora.vcall:id/input").set_text("")
        text(information)
        sleep(self.interval)

    # 聊天-发送
    def Send(self):
        poco_1("io.agora.vcall:id/sendInclude").click()
        sleep(self.interval)

    """
    挂断电话，退出频道
    """

    # 离开频道
    def leaveChannel(self):
        poco_1("io.agora.vcall:id/hangUp").click()
        sleep(self.interval)

    """
    房间设置
    """

    # 申请/放弃主持人
    def Application_host(self):
        poco_1("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/scrollView").offspring("io.agora.vcall:id/roomHost").child(
            "android.view.ViewGroup").click()
        sleep(self.interval)

    # 日志上传
    def Log_upload(self):
        poco_1("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/scrollView").offspring("io.agora.vcall:id/uploadLog").child(
            "android.view.ViewGroup").click()
        sleep(self.interval)

    # 关闭/打开音频
    def Audio(self):
        poco_1("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/scrollView").offspring("io.agora.vcall:id/itemMicrophone").child(
            "android.view.ViewGroup").click()
        sleep(self.interval)

    # 关闭/打开视频
    def Video(self):
        poco_1("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/scrollView").offspring("io.agora.vcall:id/itemCamera").child(
            "android.view.ViewGroup").click()
        sleep(self.interval)

    # 本机点击设置
    def settings(self):
        poco_1("设置").click()

    # 关网/开网
    def Network_settings(self):
        poco_1("android.widget.FrameLayout").offspring("com.android.settings:id/dashboard_container").child(
            "com.android.settings:id/category")[0].child("com.android.settings:id/category_content").child(
            "android.widget.FrameLayout")[1].offspring("com.android.settings:id/icon").click()
        poco_1("com.android.settings.wifi:id/switchButton").click()

    # 打开开发者模式
    def Open_developer_mode(self):
        touch(Template(r"a/b/tpl1574309054241.png", record_pos=(0.011, -0.852), resolution=(1080, 2160)), times=6)

        poco_1("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/scrollView").offspring("io.agora.vcall:id/developerMenu").child(
            "android.view.ViewGroup").click()

    #RTM断开/连接
    def RTM_disconnect(self):
        poco_1("android.widget.LinearLayout").offspring("io.agora.vcall:id/developer_container").offspring(
            "io.agora.vcall:id/connRtm").offspring("io.agora.vcall:id/btSwitch").click()