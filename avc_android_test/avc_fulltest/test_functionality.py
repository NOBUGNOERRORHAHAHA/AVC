# -*- coding:utf-8 -*-
from airtest.core.api import *
import pytest
from common import case_tag
from common.maincase import Android_AVC

import pytesseract

from common.maincase2 import Android_AVC2

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.0/bin/tesseract'
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import connect_device

dev1 = connect_device('Android:///433edc01?cap_method=javacap&touch_method=adb')
dev2 = connect_device('Android:///57a1a1bd?cap_method=javacap&touch_method=adb')
poco_2 = AndroidUiautomationPoco(dev2, use_airtest_input=True, screenshot_each_action=False)
poco_1 = AndroidUiautomationPoco(dev1, use_airtest_input=True, screenshot_each_action=False)


class TestAndroid:

    def setup(self):
        self.avc = Android_AVC()
        self.avc_2 = Android_AVC2()
        self.channel_name = "AVCAUTO"
        self.password = "avctest"
        self.packageName = "io.agora.vcall"
        self.nickname = "jkjl"
        self.screeshot_path = "resource/images/"
        self.oppo_password = "bestvoip123"

    def tearDown(self):
        pass

    # TES-3739 获取版本号 (当前V4.0.0、RTC 2.9.1、RTM 1.0.1)
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_getversion(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        path1 = self.screeshot_path + "test_getversion.png"
        path2 = self.screeshot_path + "v4.0.0.png"
        snapshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 0, 41 / 50 * height, width, 8 / 9 * height)
        text = avc.getWordsInImage(path2)
        print(text)
        assert text == "V4.0.0"
        avc.checkversion()
        path1 = self.screeshot_path + "test_getversion1.png"
        path2 = self.screeshot_path + "RTC 2.9.1.png"
        snapshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 0, 41 / 50 * height, width, 8 / 9 * height)
        text = avc.getWordsInImage(path2)
        print(text)
        assert text == "RTC 2.9.1"
        avc.checkversion()
        path1 = self.screeshot_path + "test_getversion2.png"
        path2 = self.screeshot_path + "RTM 1.0.1.png"
        snapshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 0, 41 / 50 * height, width, 8 / 9 * height)
        text = avc.getWordsInImage(path2)
        print(text)
        assert text == "RTM 1.0.1"
        avc.key_back()

    # TES-3771 设置界面，昵称不超过18，中英文，特殊符号
    @pytest.mark.parametrize("nickname", ["1234567899876543210", "732djshgdshGHCTbddfbhddh", "37438", "😢昵称设置"])
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_editNick(self, nickname):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        sleep(1)
        avc.nick_comfirm(nickname)
        sleep(5)
        path1 = self.screeshot_path + "getNickname1.png"
        path2 = self.screeshot_path + "getNickname2.png"
        snapshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 0, 4 / 10 * height, width, 1 / 2 * height)
        text = avc.getWordsInImage(path2)
        print(text)
        assert len(text) <= 18

        # 返回AVC首页
        avc.key_back()

    # TES-3771 (1) 昵称更新查看会者列表与消息列表
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_update_nickname(self):
        self.channelname = "wdss"
        self.nickname = "SODK"
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.nick_comfirm(self.nickname)
        avc.settings_back()
        avc.inputChannelName(self.channelname)
        avc.joinChannel()
        avc.list_of_pepole()
        text = poco_1("io.agora.vcall:id/userName")
        b = text.get_text()
        a = b[0:4]
        print(a)
        assert a == "SODK"

    # TES-3760 频道名不能超过18
    @pytest.mark.parametrize("channelname", ["1234567899876543210", "eheygfFSFGCFTS378426", "387"])
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_Namelength(self, channelname):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(channelname)
        sleep(1)
        path1 = self.screeshot_path + "getNickname1.png"
        path2 = self.screeshot_path + "getNickname2.png"
        snapshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 0, 8 / 15 * height, width, 4 / 6 * height)
        text = avc.getWordsInImage(path2)
        print(text)
        assert len(text) <= 18

    # TES-3762 频道名自动大写
    @pytest.mark.parametrize("channelname", ["sdagh"])
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_Nameauto_capitalized(self, channelname):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(channelname)
        sleep(1)
        path1 = self.screeshot_path + "getNickname1.png"
        path2 = self.screeshot_path + "getNickname2.png"
        snapshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 0, 8 / 17 * height, width, 4 / 7 * height)
        text = avc.getWordsInImage(path2)
        a = text[-5:]
        print(a)
        assert a == "SDAGH"

    # TES-3763 房间密码格式
    @pytest.mark.parametrize("password", ["abc", "123", "Unicode 007FF", "abc900,."])
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_PWDlength(self, password):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.inputPassword(password)
        sleep(1)
        path1 = self.screeshot_path + "getNickname1.png"
        path2 = self.screeshot_path + "getNickname2.png"
        snapshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 0, 3 / 5 * height, width, 2 / 3 * height)
        text = avc.getWordsInImage(path2)
        print(text)
        assert len(text) <= 18

    # TES-3764 （1）有效房间名，无密码加入房间
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_name_valid(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.nick_comfirm(self.nickname)
        avc.settings_back()
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc.leaveChannel()

    # TES-3760（1）房间名小于3，无密码加入房间
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_namelength_less_3(self):
        self.channel_name = "12"
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.nick_comfirm(self.nickname)
        avc.settings_back()
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        path1 = self.screeshot_path + "getNickname1.png"
        path2 = self.screeshot_path + "getNickname2.png"
        snapshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 0, 27 / 50 * height, width, 29 / 50 * height)
        text = avc.getWordsInImage(path2)
        print(text)
        assert text == "不 能 少 于 3 位"
        # avc.leaveChannel()

    # TES-3760（2）房间名大于18，无密码加入房间
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_namelength_longer_18(self):
        self.channel_name = "123456789123456789000"
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        # avc.nick_comfirm(self.nickname)
        # avc.nick_back()
        avc.inputChannelName(self.channel_name)
        path1 = self.screeshot_path + "getNickname1.png"
        path2 = self.screeshot_path + "getNickname2.png"
        snapshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 0, 49 / 100 * height, width, 13 / 25 * height)
        text = avc.getWordsInImage(path2)
        print(text)
        assert text == "123456789123456789"
        avc.joinChannel()
        avc.leaveChannel()

    # TES-3764 （2）房间名有效，密码大于18加入房间
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_PWDlength_longer_18(self):
        self.password = "123456789123456789000"
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.nick_comfirm(self.nickname)
        avc.settings_back()
        avc.inputChannelName(self.channel_name)
        avc.inputPassword(self.password)
        path1 = self.screeshot_path + "getNickname1.png"
        path2 = self.screeshot_path + "getNickname2.png"
        snapshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 0, 29 / 50 * height, width, 31 / 50 * height)
        text = avc.getWordsInImage(path2)
        print(text)
        assert text == "123456789123456789"
        avc.joinChannel()
        avc.leaveChannel()

    # TES-3765 （1）房间名有效，密码有效，mute本地视频加入房间
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_mutelocalvideo_joinchanel(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.nick_comfirm(self.nickname)
        avc.mutelocalvideo_channelout()
        avc.settings_back()
        avc.inputChannelName(self.channel_name)
        avc.inputPassword(self.password)
        avc.joinChannel()
        path1 = self.screeshot_path + "getNickname1.png"
        path2 = self.screeshot_path + "getNickname2.png"
        snapshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 0, 29 / 50 * height, width, 31 / 50 * height)
        text = avc.getWordsInImage(path2)
        print(text)
        assert text == "123456789123456789"
        avc.leaveChannel()

    # TES - 3765 （2）房间名有效，无效密码，
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_Invalid_password_login(self):
        self.channel_name = "wede"
        self.password = "123"
        self.password_2 = "124"
        avc = self.avc
        avc2 = self.avc_2
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.inputPassword(self.password)
        avc.joinChannel()
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.inputPassword_2(self.password_2)
        avc2.joinChannel_2()
        assert_exists(Template(r"a/b/tpl1574305499112.png", record_pos=(-0.005, 0.643), resolution=(1080, 2160)),
                      "无效密码")

    # TES-3772 分辨率调试
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_1(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.bt_settings()
        avc.Resolution_480p()
        text = poco_1("io.agora.vcall:id/resolutionDetail")
        a = text.get_text()
        b = a[0:4]
        print(b)
        assert b == "480P"
        avc.Resolution_720p()
        text = poco_1("io.agora.vcall:id/resolutionDetail")
        c = text.get_text()
        d = c[0:4]
        print(d)
        assert d == "720P"
        avc.Resolution_360p()
        text = poco_1("io.agora.vcall:id/resolutionDetail")
        e = text.get_text()
        f = e[0:4]
        print(f)
        assert f == "360P"

    # TES-3773 （1）开启音视频进入房间
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_2(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.bt_settings()
        text = poco_1("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/itemCamera").offspring("io.agora.vcall:id/itemSecondaryText")
        a = text.get_text()
        b = a[0:4]
        assert b == "默认打开"
        text = poco_1("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/itemMicrophone").offspring("io.agora.vcall:id/itemSecondaryText")
        c = text.get_text()
        d = c[0:4]
        assert d == "默认打开"
        avc.settings_back()
        avc.joinChannel()
        assert_exists(Template(r"a/b/tpl1573294105065.png", record_pos=(-0.286, 0.79), resolution=(1080, 2160)),
                      "请填写测试点")
        avc.leaveChannel()

    # TES-3773 （2）关闭音视频进入房间
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_3(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.bt_settings()
        avc.Turn_off_the_camera()
        avc.Turn_off_the_maicrophone()
        avc.settings_back()
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        assert_exists(Template(r"a/b/tpl1573438981381.png", record_pos=(-0.294, 0.78), resolution=(1080, 2160)),
                      "请填写测试点")
        avc.leaveChannel()

    # TES-3773 （3）频道内更改音视频属性
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_4(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc.bt_settings()
        avc.Audio()
        avc.Video()
        avc.settings_back()
        avc.leaveChannel()
        avc.joinChannel()
        assert_exists(Template(r"a/b/tpl1573440042000.png", record_pos=(-0.276, 0.78), resolution=(1080, 2160)),
                      "请填写测试点")
        avc.leaveChannel()

    # TES-3770 头像上传
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_5(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.bt_settings()
        path1 = self.screeshot_path + "test_5.png"
        snapshot(path1)
        avc.Avatar_upload()
        path2 = self.screeshot_path + "test_5_2.png"
        snapshot(path2)
        avc.compare_images(path1, path2)
        avc.settings_back()

    # TES-3776 检查网络质量
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_conversation_quality(self):
        avc2 = self.avc_2
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        text = poco_2("io.agora.vcall:id/signalDes")
        a = text.get_text()
        print(a)
        assert a == "网络质量良好"
        avc2.home()
        avc2.settings_2()
        avc2.Network_settings_2()
        avc2.home()
        avc2.startAVC(self.packageName)
        text = poco_2("io.agora.vcall:id/signalDes")
        b = text.get_text()
        print(b)
        assert b == "网络质量差"

    # TES-3777 （1）说话者mute音频图标更改
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_6(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc.Turn_off_audio()
        assert_exists(Template(r"a/b/tpl1573453313058.png", record_pos=(0.437, -0.935), resolution=(1080, 2160)),
                      "请填写测试点")
        avc.Recovery_status_bar()
        avc.leaveChannel()

    # TES-3777 （2）说话者音频图标高亮
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_7(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        assert_exists(Template(r"a/b/tpl1573454482252.png", record_pos=(0.448, -0.906), resolution=(1080, 2160)),
                      "请填写测试点")
        avc.Recovery_status_bar()
        avc.leaveChannel()

    # TES-3778 （1）房间内收发信息
    @pytest.mark.parametrize("information", ["12345", "732djshg.//", "www.baidu.com", "😢昵称设置"])
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_8(self, information):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc.Message_list()
        path1 = self.screeshot_path + "test_8.png"
        snapshot(path1)
        avc.To_chat_with(information)
        avc.Send()
        path2 = self.screeshot_path + "test_8_2.png"
        snapshot(path2)
        avc.compare_images(path1, path2)
        avc.settings_back()
        avc.leaveChannel()

    # TES-3778 （2）房间内收发信息，链接正常跳转
    @pytest.mark.parametrize("information", ["www.baidu.com"])
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_9(self, information):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc.Message_list()
        avc.To_chat_with(information)
        avc.Send()
        avc.link()

    # TES-3779 本地音视频mute后，显示昵称
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_10(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        path1 = self.screeshot_path + "test_10.png"
        snapshot(path1)
        avc.Recovery_status_bar()
        avc.Turn_off_audio()
        avc.Close_vido()
        path2 = self.screeshot_path + "test_10_2.png"
        snapshot(path2)
        avc.compare_images(path1, path2)
        avc.leaveChannel()

    # TES-3781 （1）会议内设置界面操作（申请主持人，关闭音视频）
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_11(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        path1 = self.screeshot_path + "test_11.png"
        snapshot(path1)
        avc.Recovery_status_bar()
        avc.bt_settings()
        avc.Application_host()
        avc.Audio()
        avc.Video()
        avc.settings_back()
        avc.leaveChannel()
        avc.joinChannel()
        path2 = self.screeshot_path + "test_11_2.png"
        snapshot(path2)
        avc.compare_images(path1, path2)
        avc.leaveChannel()

    # TES- 3795 会议中横屏旋转（申请主持人之后，横屏后频道内图标显示正常）
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_12(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        path1 = self.screeshot_path + "test_12.png"
        snapshot(path1)
        avc.Recovery_status_bar()
        avc.bt_settings()
        avc.Application_host()
        avc.settings_back()
        path2 = self.screeshot_path + "test_12_2.png"
        snapshot(path2)
        avc.compare_images(path1, path2)
        avc.Recovery_status_bar()
        avc.leaveChannel()

    # TES-3796 上传日志
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_13(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc.bt_settings()
        path1 = self.screeshot_path + "test_13.png"
        snapshot(path1)
        avc.log_upload()
        sleep(2)
        path2 = self.screeshot_path + "test_13_2.png"
        snapshot(path2)
        avc.compare_images(path1, path2)
        avc.settings_back()
        avc.leaveChannel()

    # TES-3799 （1）主持人退出频道再次进入
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_14(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc.bt_settings()
        avc.Application_host()
        avc.settings_back()
        avc.leaveChannel()
        avc.joinChannel()
        avc.Recovery_status_bar()
        assert_exists(Template(r"a/b/tpl1573539825762.png", record_pos=(0.438, -0.933), resolution=(1080, 2160)),
                      "请填写测试点")
        avc.Recovery_status_bar()
        avc.leaveChannel()

    # TES-3799 （2）原主持人放弃主持人权限
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_15(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc.bt_settings()
        avc.Application_host()
        path1 = self.screeshot_path + "test_15.png"
        snapshot(path1)
        avc.settings_back()
        avc.leaveChannel()
        avc.joinChannel()
        avc.bt_settings()
        avc.Application_host()
        path2 = self.screeshot_path + "test_15_2.png"
        snapshot(path2)
        avc.compare_images(path1, path2)
        avc.settings_back()
        avc.leaveChannel()

    # TES-4345 （1）本地mute视频后显示昵称
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_16(self):
        self.nickname = "SDFGH"
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.nick_comfirm(self.nickname)
        avc.settings_back()
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc.Close_vido()
        text = poco_1("io.agora.vcall:id/userName")
        a = text.get_text()
        print(a)
        assert a == "SDFGH"

    # TES-4346 房间时常显示（本地退出当前房间时常累加，创建新房间是00：00）
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_17(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        text = poco_1("io.agora.vcall:id/duration")
        a = text.get_text()
        print(a)
        avc.leaveChannel()
        sleep(10)
        avc.joinChannel()
        text1 = poco_1("io.agora.vcall:id/duration")
        b = text1.get_text()
        print(b)
        assert a < b

    # TES-3774（1）一个主播和多个主播的显示
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_18(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        path1 = self.screeshot_path + "test_18.png"
        snapshot(path1)
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        path2 = self.screeshot_path + "test_18_2.png"
        snapshot(path2)
        avc.compare_images(path1, path2)

    # TES-3774（2）大小窗口切换
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_19(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()

        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        path1 = self.screeshot_path + "test_19.png"
        snapshot(path1)
        avc.Window_switching()
        path2 = self.screeshot_path + "test_19_2.png"
        snapshot(path2)
        avc.compare_images(path1, path2)

    # TES-3774（3）远端大屏位置主播退出会议，本地切换为大屏
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_20(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        path1 = self.screeshot_path + "test_20.png"
        snapshot(path1)
        avc2.setCurrentDevice(1)
        avc2.Recovery_status_bar_2()
        avc2.leaveChannel_2()
        avc.setCurrentDevice(0)
        path2 = self.screeshot_path + "test_20_2.png"
        snapshot(path2)
        avc.compare_images(path1, path2)

    # TES-3775 存在主持人切换窗口主持人UI图标的远端显示正常
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_21(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()

        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        path1 = self.screeshot_path + "test_21.png"
        snapshot(path1)

        avc2.setCurrentDevice(1)
        avc2.Recovery_status_bar_2()
        avc2.bt_settings_2()
        avc2.Application_host_2()
        avc.setCurrentDevice(0)
        path2 = self.screeshot_path + "test_21_2.png"
        snapshot(path2)

        avc.compare_images(path1, path2)

    # TES-3780 （1）存在主持人，非主持人查看会者列表无法操作
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_22(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        avc2.list_of_pepole_2()
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc2.setCurrentDevice(1)
        path1 = self.screeshot_path + "test_22.png"
        snapshot(path1)
        avc.setCurrentDevice(0)
        avc.bt_settings()
        avc.Application_host()
        avc2.setCurrentDevice(1)
        path2 = self.screeshot_path + "test_22_2.png"
        snapshot(path2)
        avc.compare_images(path1, path2)

    # TES-3780 （2）存在主持人，会话列表中操作音视频关闭和踢人
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_23(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        avc2.bt_settings_2()
        avc2.Application_host_2()
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc2.setCurrentDevice(1)
        avc2.settings_back_2()
        avc2.list_of_pepole_2()
        avc2.Select_attribute_1()
        avc2.Click_audio_2()
        avc2.Select_attribute_1()
        avc2.Click_Vido_2()
        avc.setCurrentDevice(0)
        avc.Recovery_status_bar()
        assert_exists(Template(r"a/b/tpl1574043428432.png", record_pos=(-0.278, 0.803), resolution=(1080, 1920)),
                      "请填写测试点")
        avc2.setCurrentDevice(1)
        path1 = self.screeshot_path + "test_23.png"
        snapshot(path1)
        avc2.Select_attribute_1()
        avc2.Kicking_people_2()
        path2 = self.screeshot_path + "test_23_2.png"
        snapshot(path2)
        avc.compare_images(path1, path2)

    # TES-3780 （3）动态显示房间人数(判断增加和减少房间人数的判断)
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_24(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        assert_exists(Template(r"a/b/tpl1574045198264.png", record_pos=(0.231, 0.785), resolution=(1080, 2160)),
                      "当前频道存在两人")
        avc2.setCurrentDevice(1)
        avc2.Recovery_status_bar_2()
        path1 = self.screeshot_path + "test_24.png"
        snapshot(path1)
        avc.setCurrentDevice(0)
        avc.Recovery_status_bar()
        avc.leaveChannel()
        avc2.setCurrentDevice(1)
        avc2.Recovery_status_bar_2()
        path2 = self.screeshot_path + "test_24_2.png"
        snapshot(path2)
        avc.compare_images(path1, path2)

    # TES-3787 （1）无房间主持人时，本地mute本地音频，远端发起邀请（本地拒绝）
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_25(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        avc2.Turn_off_audio_2()
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc.list_of_pepole()
        path1 = self.screeshot_path + "test_25.png"
        snapshot(path1)
        avc.Select_attribute_1()
        avc.Click_audio()
        avc.Choose_OK()
        avc2.setCurrentDevice(1)
        avc2.Choose_NO_2()
        avc.setCurrentDevice(0)
        path2 = self.screeshot_path + "test_25_2.png"
        snapshot(path2)
        avc.compare_images(path1, path2)

    # TES-3787 （2）无房间主持人时，本地mute本地音频，远端发起邀请（本地接受）
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_26(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        avc2.Turn_off_audio_2()
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc.list_of_pepole()
        path1 = self.screeshot_path + "test_26.png"
        snapshot(path1)
        avc.Select_attribute_1()
        avc.Click_audio()
        avc.Choose_OK()
        avc2.setCurrentDevice(1)
        avc2.Choose_OK_2()
        avc.setCurrentDevice(0)
        path2 = self.screeshot_path + "test_26_2.png"
        snapshot(path2)
        avc.compare_images(path1, path2)

    # TES-3787 （3）无房间主持人时，本地mute本地音频，远端发起邀请（本地不点击）
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_27(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        avc2.Turn_off_audio_2()
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc.list_of_pepole()
        avc.Select_attribute_1()
        avc.Click_audio()
        avc.Choose_OK()
        sleep(10)
        assert_exists(Template(r"a/b/tpl1574058657622.png", record_pos=(-0.018, 0.651), resolution=(1080, 2160)),
                      "请填写测试点")

    # TES-3788 （1）无房间主持人时，本地关闭视频，远端发起邀请 （本地拒绝邀请）
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_28(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        avc2.Close_vido_2()
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc.list_of_pepole()
        path1 = self.screeshot_path + "test_28.png"
        snapshot(path1)
        avc.Select_attribute_1()
        avc.Click_Vido()
        avc.Choose_OK()
        avc2.setCurrentDevice(1)
        avc2.Choose_NO_2()
        avc.setCurrentDevice(0)
        path2 = self.screeshot_path + "test_28_2.png"
        snapshot(path2)
        avc.compare_images(path1, path2)

    # TES-3788 （2） 无房间主持人时，本地关闭视频，远端发起邀请 （本地接受邀请）
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_29(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        avc2.Close_vido_2()
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc.list_of_pepole()
        path1 = self.screeshot_path + "test_29.png"
        snapshot(path1)
        avc.Select_attribute_1()
        avc.Click_Vido()
        avc.Choose_OK()
        avc2.setCurrentDevice(1)
        avc2.Choose_OK_2()
        avc.setCurrentDevice(0)
        sleep(2)
        path2 = self.screeshot_path + "test_29_2.png"
        snapshot(path2)
        avc.compare_images(path1, path2)

    # TES-3788 （3）无房间主持人时，本地关闭视频，远端发起邀请 （本地不点击）
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_30(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        avc2.Close_vido_2()
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc.list_of_pepole()
        avc.Select_attribute_1()
        avc.Click_Vido()
        avc.Choose_OK()
        sleep(10)
        assert_exists(Template(r"a/b/tpl1574060355183.png", record_pos=(-0.018, 0.651), resolution=(1080, 2160)),
                      "请填写测试点")

    # TES-3789 房间存在主持人时，本地mute音视频，主持人发起邀请，开启音视频
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_31(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        avc2.Close_vido_2()
        avc2.Turn_off_audio_2()
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc.bt_settings()
        avc.Application_host()
        avc.settings_back()
        avc.list_of_pepole()
        path1 = self.screeshot_path + "test_31.png"
        snapshot(path1)
        avc.Select_attribute_1()
        avc.Click_audio()
        avc.Choose_OK()
        avc2.setCurrentDevice(1)
        avc2.Choose_OK_2()
        avc.setCurrentDevice(0)
        avc.Select_attribute_1()
        avc.Click_Vido()
        avc.Choose_OK()
        avc2.setCurrentDevice(1)
        avc2.Choose_OK_2()
        avc.setCurrentDevice(0)
        path2 = self.screeshot_path + "test_31_2.png"
        snapshot(path2)
        avc.compare_images(path1, path2)

    # TES-3790（1）处于后台状态远端发起unmute音视频邀请 不点击
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_32(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        avc2.Turn_off_audio_2()
        avc2.home()
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc.list_of_pepole()
        avc.Select_attribute_1()
        avc.Click_audio()
        avc.Choose_OK()
        sleep(10)
        assert_exists(Template(r"a/b/tpl1574058657622.png", record_pos=(-0.018, 0.651), resolution=(1080, 2160)),
                      "请填写测试点")

    # TES-3790（2）处于后台状态远端发起unmute音视频邀请 接受
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_33(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        avc2.Turn_off_audio_2()
        avc2.Close_vido_2()
        avc2.home()
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc.list_of_pepole()
        path1 = self.screeshot_path + "test_33.png"
        snapshot(path1)
        avc.Select_attribute_1()
        avc.Click_audio()
        avc.Choose_OK()
        avc.Select_attribute_1()
        avc.Click_Vido()
        avc.Choose_OK()
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.Choose_OK_2()
        avc2.Choose_OK_2()
        avc.setCurrentDevice(0)
        path2 = self.screeshot_path + "test_33_2.png"
        snapshot(path2)
        avc.compare_images(path1, path2)

    # TES-3791 （1）断网过程中远端发起unmute音视频邀请（没有响应邀请）
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_34(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        avc2.Turn_off_audio_2()
        avc2.Close_vido_2()
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc2.setCurrentDevice(1)
        avc2.home()
        avc2.settings_2()
        avc2.Network_settings_2()
        avc.setCurrentDevice(0)
        avc.Recovery_status_bar()
        avc.list_of_pepole()
        path1 = self.screeshot_path + "test_34.png"
        snapshot(path1)
        avc.Select_attribute_1()
        avc.Click_audio()
        avc.Choose_OK()
        avc.Select_attribute_1()
        avc.Click_Vido()
        avc.Choose_OK()
        sleep(10)
        path2 = self.screeshot_path + "test_34_2.png"
        snapshot(path2)
        avc.compare_images(path1, path2)

    # TES-3791 （2）断网过程中远端发起unmute音视频邀请（重新连接网络）
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_35(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        avc2.Turn_off_audio_2()
        avc2.Close_vido_2()
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc.list_of_pepole()
        avc2.setCurrentDevice(1)
        avc2.home()
        avc2.settings_2()
        avc2.Network_settings_2()
        avc2.home()
        avc.setCurrentDevice(0)
        path1 = self.screeshot_path + "test_35.png"
        snapshot(path1)
        avc2.setCurrentDevice(1)
        avc2.settings_2()
        avc2.Network_settings_2()
        avc2.home()
        avc.setCurrentDevice(0)
        avc.Select_attribute_1()
        avc.Click_audio()
        avc.Choose_OK()
        avc.Select_attribute_1()
        avc.Click_Vido()
        avc.Choose_OK()
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.Choose_OK_2()
        avc2.Choose_OK_2()
        avc.setCurrentDevice(0)
        path2 = self.screeshot_path + "test_35_2.png"
        snapshot(path2)
        avc.compare_images(path1, path2)

    # TES-3793 音视频unmute邀请窗口分开显示
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_36(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        avc2.Turn_off_audio_2()
        avc2.Close_vido_2()
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc.list_of_pepole()
        avc.Select_attribute_1()
        avc.Click_audio()
        avc.Choose_OK()
        avc2.setCurrentDevice(1)
        assert_exists(Template(r"a/b/tpl1574135042899.png", record_pos=(0.002, 0.028), resolution=(1080, 1920)),
                      "邀请打开麦克风")
        avc2.Choose_OK_2()
        avc.setCurrentDevice(0)
        avc.Select_attribute_1()
        avc.Click_Vido()
        avc.Choose_OK()
        avc2.setCurrentDevice(1)
        assert_exists(Template(r"a/b/tpl1574135074701.png", record_pos=(0.0, 0.029), resolution=(1080, 1920)),
                      "邀请打开摄像头")
        avc2.Choose_OK_2()

    # 断网时修改房间音视频属性 （AB加入mute的房间，不互通）
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_37(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        avc2.bt_settings_2()
        avc2.Turn_off_the_camera_2()
        avc2.Turn_off_the_maicrophone_2()
        avc2.settings_back_2()
        avc2.leaveChannel_2()
        avc2.joinChannel_2()
        assert_exists(Template(r"a/b/tpl1574149708948.png", record_pos=(-0.121, 0.644), resolution=(1080, 1920)),
                      "房间默认关闭麦克风和摄像头")
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        assert_exists(Template(r"a/b/tpl1574149708948.png", record_pos=(-0.121, 0.644), resolution=(1080, 1920)),
                      "房间默认关闭麦克风和摄像头")

    # 断网过程中，被mute/unmute后重新联网 (mute)
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_38(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc.list_of_pepole()
        avc2.setCurrentDevice(1)
        avc2.home()
        avc2.settings_2()
        avc2.Network_settings_2()
        avc2.home()
        avc.setCurrentDevice(0)
        avc.Select_attribute_1()
        avc.Click_audio()
        avc.Select_attribute_1()
        avc.Click_Vido()
        avc2.setCurrentDevice(1)
        avc2.settings_2()
        avc2.Network_settings_2()
        avc2.home()
        avc2.startAVC(self.packageName)
        avc.setCurrentDevice(0)
        assert_exists(Template(r"a/b/tpl1574155811655.png", record_pos=(-0.156, -0.382), resolution=(1080, 2160)),
                      "音视频mute")

    # TES-3794 （1）会议参与者mute本地音频
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_39(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        avc2.Turn_off_audio_2()
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        assert_exists(Template(r"a/b/tpl1574215328320.png", record_pos=(0.304, -0.944), resolution=(1080, 2160)),
                      "mute音频")

    # TES-3794 （2） 会议参与者mute本地视频
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_40(self):
        self.channel_name = "wedfs"
        self.nickname = "dhdh"
        avc = self.avc
        avc2 = self.avc_2
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.nick_comfirm_2(self.nickname)
        avc2.settings_back_2()
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        avc2.Close_vido_2()
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        text = poco_1("io.agora.vcall:id/userName")
        a = text.get_text()
        print(a)
        assert a == "dhdh"
