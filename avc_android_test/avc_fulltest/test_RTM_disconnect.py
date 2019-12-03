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

    # TES-4347 RTM断线重连提示
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_41(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc.bt_settings()
        avc.Open_developer_mode()
        avc.RTM_disconnect()
        avc.settings_back()
        path1 = self.screeshot_path + "test_41.png"
        snapshot(path1)
        avc.Open_developer_mode()
        avc.RTM_disconnect()
        avc.settings_back()
        path2 = self.screeshot_path + "test_41_2.png"
        snapshot(path2)
        avc.compare_images(path1, path2)

    # TES-4531 (1)频道外断开RTM，本地默认关闭音视频
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_42(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.bt_settings()
        avc.Open_developer_mode()
        avc.RTM_disconnect()
        avc.settings_back()
        avc.settings_back()
        avc.joinChannel()
        assert_exists(Template(r"a/b/tpl1573438981381.png", record_pos=(-0.294, 0.78), resolution=(1080, 2160)),
                      "音视频关闭")
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        avc.setCurrentDevice(0)
        avc.Recovery_status_bar()
        assert_exists(Template(r"a/b/tpl1573294105065.png", record_pos=(-0.286, 0.79), resolution=(1080, 2160)),
                      "音视频打开")

    # TES-4531 (2)频道外断开RTM，本地默认关闭音视频 (远端更改房间属性为mute)
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_43(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.bt_settings()
        avc.Open_developer_mode()
        avc.RTM_disconnect()
        avc.settings_back()
        avc.settings_back()
        avc.joinChannel()
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
        avc.setCurrentDevice(0)
        avc.Recovery_status_bar()
        avc.bt_settings()
        text = poco_1(text="参会者进入房间时自动关闭摄像头")
        a = text.get_text()
        print(a)
        assert a == "参会者进入房间时自动关闭摄像头"
        text_1 = poco_1(text="参会者进入房间时自动关闭麦克风")
        b = text_1.get_text()
        print(b)
        assert b == "参会者进入房间时自动关闭麦克风"

    # TES-4531 (2)频道外断开RTM，本地默认关闭音视频 (本地重连RTM)
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_44(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.bt_settings()
        avc.Open_developer_mode()
        avc.RTM_disconnect()
        avc.settings_back()
        avc.settings_back()
        avc.joinChannel()
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
        avc.setCurrentDevice(0)
        avc.Recovery_status_bar()
        avc.bt_settings()
        avc.Open_developer_mode()
        avc.RTM_disconnect()
        avc.settings_back()
        avc.settings_back()
        assert_exists(Template(r"a/b/tpl1573294105065.png", record_pos=(-0.286, 0.79), resolution=(1080, 2160)),
                      "音视频打开")
        avc.leaveChannel()
        avc.joinChannel()
        assert_exists(Template(r"a/b/tpl1574149708948.png", record_pos=(-0.121, 0.644), resolution=(1080, 1920)),
                      "房间默认关闭麦克风和摄像头")

    # TES-4551 (1) 断开RTM，频道内操控远端音视频(mute没有断开RTM的一端/unmute)
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_45(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.bt_settings()
        avc.Open_developer_mode()
        avc.RTM_disconnect()
        avc.settings_back()
        avc.settings_back()
        avc.joinChannel()
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        avc.setCurrentDevice(0)
        avc.Recovery_status_bar()
        avc.list_of_pepole()
        avc.Select_attribute_1()
        avc.Click_audio()
        avc.Select_attribute_1()
        avc.Click_Vido()
        avc2.setCurrentDevice(1)
        avc2.Recovery_status_bar_2()
        assert_exists(Template(r"a/b/tpl1574043428432.png", record_pos=(-0.278, 0.803), resolution=(1080, 1920)),
                      "请填写测试点")
        avc.setCurrentDevice(0)
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
        avc2.Recovery_status_bar_2()
        assert_exists(Template(r"a/b/tpl1573294105065.png", record_pos=(-0.286, 0.79), resolution=(1080, 2160)),
                      "请填写测试点")

    # TES-4551 (2) 断开RTM，频道内操控远端音视频(mute本地RTM断开的)
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_46(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.bt_settings()
        avc.Open_developer_mode()
        avc.RTM_disconnect()
        avc.settings_back()
        avc.settings_back()
        avc.joinChannel()
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        avc.setCurrentDevice(0)
        avc.Recovery_status_bar()
        avc.Turn_off_audio()
        avc.Close_vido()
        avc2.setCurrentDevice(1)
        avc2.Recovery_status_bar_2()
        avc2.list_of_pepole_2()
        assert_exists(Template(r"a/b/tpl1574155811655.png", record_pos=(-0.156, -0.382), resolution=(1080, 2160)),
                      "音视频mute")
        avc2.Select_attribute_1()
        avc2.Click_audio_2()
        avc2.Choose_OK_2()
        avc.setCurrentDevice(0)
        avc.Choose_OK()
        avc2.setCurrentDevice(1)
        avc2.Select_attribute_1()
        avc2.Click_Vido_2()
        avc2.Choose_OK_2()
        avc.setCurrentDevice(0)
        avc.Choose_OK()
        avc2.setCurrentDevice(1)
        assert_exists(Template(r"a/b/tpl1574388802546.png", record_pos=(-0.123, -0.253), resolution=(1080, 1920)),
                      "请填写测试点")

    # TES-4551 (3) 断开RTM，频道内操控远端音视频(断开RTM那端mute视频后，控制远端unmute/mute)
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_47(self):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.bt_settings()
        avc.Open_developer_mode()
        avc.RTM_disconnect()
        avc.settings_back()
        avc.settings_back()
        avc.joinChannel()
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        avc2.Turn_off_audio_2()
        avc.setCurrentDevice(0)
        avc.Recovery_status_bar()
        avc.Close_vido()
        avc.list_of_pepole()
        avc.Select_attribute_1()
        avc.Click_audio()
        avc.Choose_OK()
        assert_exists(Template(r"a/b/tpl1574390635065.png", record_pos=(0.021, 0.63), resolution=(1080, 2160)),
                      "请填写测试点")
        avc.Select_attribute_1()
        avc.Click_Vido()
        assert_exists(Template(r"a/b/tpl1574390635065.png", record_pos=(0.021, 0.63), resolution=(1080, 2160)),
                      "请填写测试点")

    # TES-4362 （1）断开RTM，媒体功能测试（频道外设置断开RTM）
    @pytest.mark.parametrize("information", ["ajsnjdbvjhsd"])
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_48(self, information):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.bt_settings()
        avc.Open_developer_mode()
        avc.RTM_disconnect()
        avc.settings_back()
        avc.settings_back()
        avc.joinChannel()
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        avc.setCurrentDevice(0)
        avc.Recovery_status_bar()
        avc.Turn_off_audio()
        avc.Message_list()
        avc.To_chat_with(information)
        avc.Send()
        text = poco_1("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/chatRecyclerView").child("android.view.ViewGroup")[0].child(
            "io.agora.vcall:id/chatIndicator")
        a = text.get_text()
        print(a)
        assert a == "发送失败，点击重试"

    # TES-4362（2）断开RTM，媒体功能测试（房间内设置断开RTM）
    @pytest.mark.parametrize("information", ["ajsnjdbvjhsd"])
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_49(self, information):
        self.channel_name = "wedfs"
        avc = self.avc
        avc2 = self.avc_2
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc.bt_settings()
        avc.Open_developer_mode()
        avc.RTM_disconnect()
        avc.settings_back()
        avc.settings_back()
        avc.Turn_off_audio()
        avc.Close_vido()
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        assert_exists(Template(r"a/b/tpl1574405924286.png", record_pos=(0.005, -0.819), resolution=(1080, 1920)),
                      "请填写测试点")
        avc.setCurrentDevice(0)
        avc.Recovery_status_bar()
        avc.Message_list()
        avc.To_chat_with(information)
        avc.Send()
        text = poco_1("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/chatRecyclerView").child("android.view.ViewGroup")[0].child(
            "io.agora.vcall:id/chatIndicator")
        a = text.get_text()
        print(a)
        assert a == "发送失败，点击重试"

    # TES-4548 (1)RTM断开，开config，房间密码显示
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_50(self):
        self.channel_name = "wedfs"
        self.password = "123"
        self.password_2 = "124"
        avc = self.avc
        avc2 = self.avc_2
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.inputPassword_2(self.password_2)
        avc2.joinChannel_2()
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.bt_settings()
        avc.Open_developer_mode()
        avc.RTM_disconnect()
        avc.settings_back()
        avc.settings_back()
        avc.joinChannel()
        assert_exists(Template(r"a/b/tpl1574408884628.png", record_pos=(0.003, -0.926), resolution=(1080, 2160)),
                      "请填写测试点")
        avc.leaveChannel()
        avc.inputPassword(self.password)
        avc.joinChannel()
        assert_exists(Template(r"a/b/tpl1574408884628.png", record_pos=(0.003, -0.926), resolution=(1080, 2160)),
                      "请填写测试点")

    # TES-4548 (2)RTM断开，开config，房间密码显示
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_51(self):
        self.channel_name = "wedfs"
        self.password = "123"
        self.password_2 = "124"
        avc = self.avc
        avc2 = self.avc_2
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.inputPassword(self.password)
        avc.bt_settings()
        avc.Open_developer_mode()
        avc.RTM_disconnect()
        avc.settings_back()
        avc.settings_back()
        avc.joinChannel()
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.joinChannel_2()
        assert_exists(Template(r"a/b/tpl1574405924286.png", record_pos=(0.005, -0.819), resolution=(1080, 1920)),
                      "请填写测试点")
        avc2.leaveChannel_2()
        avc2.inputPassword_2(self.password_2)
        avc2.joinChannel_2()
        assert_exists(Template(r"a/b/tpl1574305499112.png", record_pos=(-0.005, 0.643), resolution=(1080, 2160)),
                      "无效密码")

    # TES-4548 (3)RTM断开，开config，房间密码显示
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_52(self):
        self.channel_name = "wedfs"
        self.password = "124"
        self.password_2 = "123"
        avc = self.avc
        avc2 = self.avc_2
        avc2.setCurrentDevice(1)
        avc2.startAVC(self.packageName)
        avc2.inputChannelName_2(self.channel_name)
        avc2.inputPassword_2(self.password_2)
        avc2.joinChannel_2()
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.inputPassword(self.password)
        avc.bt_settings()
        avc.Open_developer_mode()
        avc.RTM_disconnect()
        avc.settings_back()
        avc.settings_back()
        avc.joinChannel()
        avc.bt_settings()
        text=poco_1("io.agora.vcall:id/roomPwd")
        a = text.get_text()
        print(a)
        assert a == "124"
        avc.Open_developer_mode()
        avc.RTM_disconnect()
        assert_exists(Template(r"a/b/tpl1574305499112.png", record_pos=(-0.005, 0.643), resolution=(1080, 2160)),
                      "无效密码")

