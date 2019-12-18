# -*- coding:utf-8 -*-
from airtest.core.api import  *
from airtest.core.ios.ios import IOS
import pytest
from common import case_tag,verify_utils
from common.avc_ios import IOS_AVC
from common.avc_android import Android_AVC
from common import avc_constance as ac
# connect_device("ios:///http://127.0.0.1:8100")
# from poco.drivers.ios import iosPoco
# poco = iosPoco()
class TestIOS:

    def setup(self):
        self.avcIOS = IOS_AVC()
        self.avcAndroid = Android_AVC()
        self.channel_name = "AVC"
        self.password = "avctest"
        self.packageName = ac.Package_Name.ios_packageName
        self.packageName_android = ac.Package_Name.android_packageName
        self.screeshot_path = "avc_ios_test/resource/screenshot/"

    def teardown(self):
        # self.avc.stopAVC(self.packageName)
        pass


    '''3760（2，3，4） 房间名长度3-18有效，不能超过18'''
    @pytest.mark.parametrize("roomName",
                             ["aaa","ABCDEFGHIJKLMNOPQRS", "abcdefghijklmnopqrs",
                              "zxcvbnmm", "ZXCVBNM<>?!@#$%^&*(", "1234567890123456789"])
    @pytest.mark.tags(case_tag.iOS, case_tag.HIGH, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_roomName_02(self, roomName):
        avc = self.avcIOS
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.setRoomName(roomName)
        touch([100, 100])
        path = self.screeshot_path + "test_roomName_02_a.jpg"
        path1 = self.screeshot_path + "test_roomName_02_b.jpg"
        avc.getScreenshot(path)
        width, height = avc.getImageSize(path)
        avc.getCustomizeImage(path, path1, 1 / 6 * width, 7 / 20 * height, width, 2 / 5 * height)
        room_name = avc.getWordsInImage(path1)
        print("<<<<", room_name)
        assert len(room_name) <= 18

    ''' 3760（1）房间名小于3不能进入,出现提示房间名不小于三位'''
    @pytest.mark.parametrize("roomName",
                             ["as", "e", ""])
    @pytest.mark.tags(case_tag.iOS, case_tag.HIGH, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_roomName_03(self, roomName):
        avc = self.avcIOS
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        touch([100, 100])
        avc.setRoomName(roomName)
        assert avc.lessThree

    '''3761房间名输入无效'''
    @pytest.mark.parametrize("roomName",
                             ["测试测试", "，。/.';&*¥%"])
    @pytest.mark.tags(case_tag.iOS, case_tag.HIGH, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_roomName_04(self, roomName):
        avc = self.avcIOS
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        touch([100, 100])
        avc.setRoomName(roomName)
        touch([100, 100])
        path = self.screeshot_path + "test_roomName_03_a.jpg"
        path1 = self.screeshot_path + "test_roomName_03_b.jpg"
        avc.getScreenshot(path)
        width, height = avc.getImageSize(path)
        avc.getCustomizeImage(path, path1, 1 / 6 * width, 7 / 20 * height, width, 2 / 5 * height)
        room_name = avc.getWordsInImage(path1)
        print("<<<<", room_name)
        assert room_name != roomName


    '''3761房间名输入有效'''
    @pytest.mark.parametrize("roomName",
                             ["TEST", "12345", "1ABC", "NONE", "NULL", "NIL"])
    @pytest.mark.tags(case_tag.iOS, case_tag.HIGH, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_roomName_05(self, roomName):
        avc = self.avcIOS
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        touch([100, 100])
        avc.setRoomName(roomName)
        touch([100, 100])
        path = self.screeshot_path + "test_roomName_04_a.jpg"
        path1 = self.screeshot_path + "test_roomName_04_b.jpg"
        avc.getScreenshot(path)
        width, height = avc.getImageSize(path)
        avc.getCustomizeImage(path, path1, 1 / 6 * width, 7 / 20 * height, width, 2 / 5 * height)
        room_name = avc.getWordsInImage(path1)
        print("<<<<", room_name)
        assert room_name == roomName

    '''3762 英文房间名自动大写'''
    @pytest.mark.parametrize("roomName",["abcd"])
    @pytest.mark.tags(case_tag.iOS, case_tag.HIGH, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_roomName_01(self, roomName):
        avc = self.avcIOS
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.setRoomName(roomName)
        touch([100, 100])
        path = self.screeshot_path + "test_roomName_01_a.jpg"
        path1 = self.screeshot_path + "test_roomName_01_b.jpg"
        avc.getScreenshot(path)
        width, height = avc.getImageSize(path)
        avc.getCustomizeImage(path, path1, 1 / 6 * width, 7 / 20 * height, width, 2 / 5 * height)
        room_name = avc.getWordsInImage(path1)
        assert room_name == "ABCD"

    '''3763密码有效格式'''
    @pytest.mark.parametrize("password",
                             ["abc", "123", "abc900", ",.?[];"])
    @pytest.mark.tags(case_tag.iOS, case_tag.HIGH, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_password_01(self, password):
        avc = self.avcIOS
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.setPassword(password)
        path = self.screeshot_path + "test_password_01a.jpg"
        path1 = self.screeshot_path + "test_password_01b.jpg"
        avc.getScreenshot(path)
        width, height = avc.getImageSize(path)
        avc.getCustomizeImage(path, path1, 1 / 7 * width, 4 / 9 * height, width, 5 / 9 * height)
        pwd = avc.getWordsInImage(path1)
        print(">>>>>", pwd)
        assert pwd == password

    '''3763 密码置空不填 有效 '''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_password_blank(self):
        avc = self.avcIOS
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.joinChannel(roomName = self.channel_name, password = "")
        avc.leaveChannel()

    '''3763密码无效格式'''
    @pytest.mark.parametrize("password",
                             ["测试"])
    @pytest.mark.tags(case_tag.iOS, case_tag.HIGH, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_password_02(self, password):
        avc = self.avcIOS
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.setPassword(password)
        path = self.screeshot_path + "test_password_02a.jpg"
        path1 = self.screeshot_path + "test_password_02b.jpg"
        avc.getScreenshot(path)
        width, height = avc.getImageSize(path)
        avc.getCustomizeImage(path, path1, 1 / 7 * width, 4 / 9 * height, width, 5 / 9 * height)
        pwd = avc.getWordsInImage(path1)
        print(">>>>>", pwd)
        assert pwd != password

    '''3764密码长度不能超过18，小于等于18有效'''
    @pytest.mark.parametrize("password",
                             ["1ACV21-_", "Tasd_VBG00", "qwertyuiopasdfghk", "zxcvbm", "QWERTYUIOPASDFGHJKL", "ZXCVBNM",
                              "1234567890123456789", ",./!@#$%^&*()-+"])
    @pytest.mark.tags(case_tag.iOS, case_tag.HIGH, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_password(self, password):
        avc = self.avcIOS
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.setPassword(password)
        path = self.screeshot_path + "test_password_a.jpg"
        path1 = self.screeshot_path + "test_password_b.jpg"
        avc.getScreenshot(path)
        width, height = avc.getImageSize(path)
        avc.getCustomizeImage(path, path1, 1 / 7 * width, 4 / 9 * height, width, 5 / 9 * height)
        pwd = avc.getWordsInImage(path1)
        print(">>>>>",pwd)
        assert len(pwd) <= 18

    '''3765输入的房间密码正确可以正常进入会议'''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_joinchannelWithCorrectPassword(self):
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        avc_ios.leaveChannel()

    ''' 3765输入不存在的房间，成功创建房间并加入频道 '''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_joinNoExistchannel(self):
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(roomName="NotExistRoom", password = self.password)
        avc_ios.leaveChannel()

    '''3765输入的房间密码不正确无法进入会议'''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_joinchannelWithIncorrectPassword(self):
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(roomName=self.channel_name, password="error")
        assert avc_ios.errorPasswordInfo

    ''' 3770 更换头像，查看与会者列表中头像是否变化'''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_updateAvatarLocal(self):
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name,self.password)
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_android.downIcon()
        avc_android.downIcon()
        avc_android.goToParticipantList()
        # 更换头像之前，远端在与会者列表中看到的头像
        pathRemoteBefore = self.screeshot_path + "test_updateAvatar_c.jpg"
        avc_android.getScreenshot(filename=pathRemoteBefore)
        avc_android.back()
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.goToParticipantList()
        # 更换头像之前，本地在与会者列表中看到的头像
        pathLocalBefore = self.screeshot_path + "test_updateAvatar_e.jpg"
        avc_ios.getScreenshot(filename=pathLocalBefore)
        avc_ios.back()
        avc_ios.leaveChannel()
        # 本地进入个人设置界面去更换头像
        avc_ios.goMine()
        path1 = self.screeshot_path + "test_updateAvatar_a.jpg"
        path2 = self.screeshot_path + "test_updateAvatar_b.jpg"
        avc_ios.getScreenshot(filename=path1)
        # 更换头像
        avc_ios.updateAvatar()
        avc_ios.getScreenshot(filename=path2)
        # 判断本地是否更换头像成功
        assert verify_utils.compare_images(path1, path2) == "Success"
        avc_ios.back()
        # 更换头像后加入频道
        avc_ios.joinChannelSecond()
        avc_ios.goToParticipantList()
        # 更换头像之后，本地在与会者列表中看到的头像
        pathLocalAfter = self.screeshot_path + "test_updateAvatar_f.jpg"
        avc_ios.getScreenshot(filename=pathLocalAfter)
        # 判断本地与会者列表中头像是否更换
        assert verify_utils.compare_images(pathLocalBefore, pathLocalAfter) == "Success"
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.downIcon()
        avc_android.goToParticipantList()
        # 更换头像之后，远端在与会者列表中看到的头像
        pathReomoteAfter = self.screeshot_path + "test_updateAvatar_d.jpg"
        avc_android.getScreenshot(filename=pathReomoteAfter)
        avc_android.back()
        avc_android.downIcon()
        avc_android.leaveChannel()
        #远端与会者列表中查看头像是否更换
        assert verify_utils.compare_images(pathRemoteBefore, pathReomoteAfter) == "Success"

    '''3770更换头像，查看消息列表中头像是否改变'''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_updateAvatarToSeeInMessage(self):
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        # 本地更改头像前发送消息
        avc_ios.sendMessage("aaaa")
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.downIcon()
        avc_android.downIcon()
        avc_android.readMessage()
        path1 = self.screeshot_path + "test_updateAvatar_g.jpg"
        # path2保存远端在本地更改头像前看到的头像
        path2 = self.screeshot_path + "test_updateAvatar_h.jpg"
        avc_android.getScreenshot(path1)
        width, height = avc_android.getImageSize(path1)
        avc_android.getCustomizeImage(path1, path2, 1 / 20 * width, 2 / 20 * height, width, 4 / 20 * height)
        avc_android.back()
        avc_android.downIcon()
        avc_android.leaveChannel()
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.back()
        avc_ios.leaveChannel()
        avc_ios.goMine()
        # 本地去更改头像
        avc_ios.updateAvatar()
        avc_ios.back()
        avc_ios.joinChannelSecond()
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        # 本地更改头像后发送消息
        avc_ios.sendMessage("aaaa")
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.readMessage()
        path3 = self.screeshot_path + "test_updateAvatar_i.jpg"
        # path4保存远端在本地更改头像前看到的头像
        path4 = self.screeshot_path + "test_updateAvatar_j.jpg"
        avc_android.getScreenshot(path3)
        width, height = avc_android.getImageSize(path3)
        avc_android.getCustomizeImage(path3, path4,  1 / 20 * width, 2 / 20 * height, width, 4 / 20 * height)
        # 断言远端在消息列表中看到本地的头像前后是否改变
        assert verify_utils.compare_images(path2, path4) == "Success"
        

    ''' 3771 nickname有效'''
    @pytest.mark.parametrize("nickname",
                            [ "测试中文","1234567890", "qwertyuiopasdfghjk", "QWERTYUIOPASDFGHJ", "KLZXCVVBNM", "l;'zxv c ",
                             "~!@#$%^&()_+","ull",""] )
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_updateNickname_01(self, nickname):
        avc = self.avcIOS
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.goMine()
        avc.updateNickname(nickname)
        path1 = self.screeshot_path + "test_updateNickname_01a.jpg"
        path2 = self.screeshot_path + "test_updateNickname_01b.jpg"
        avc.getScreenshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 1 / 4 * width, 41 / 100 * height,  width, 10 / 20 * height)
        words = avc.getWordsInImage(path2)
        assert words == nickname
        avc.back()

    ''' 3771nickname长度 > 18 无效 '''
    @pytest.mark.parametrize("nickname",["12345678901234567890"])
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_updateNickname_02(self, nickname):
        avc = self.avcIOS
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.goMine()
        avc.updateNickname(nickname)
        path1 = self.screeshot_path + "test_updateNickname_02a.jpg"
        path2 = self.screeshot_path + "test_updateNickname_02b.jpg"
        avc.getScreenshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 1 / 4 * width, 41 / 100 * height, width, 1/ 2 * height)
        words = avc.getWordsInImage(path2)
        assert words == "123456789012345678"

    '''3771，4345（1）更新昵称，与会者列表昵称显示情况'''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_setNickNameParticipantList(self):
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_android.downIcon()
        avc_android.downIcon()
        avc_android.goToParticipantList()
        # 更新昵称前，远端在与会者列表中看到的昵称
        pathRemoteBefore = self.screeshot_path + "test_updateNickName_c.jpg"
        avc_android.getScreenshot(filename=pathRemoteBefore)
        avc_android.back()
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.goToParticipantList()
        # 更新昵称前，本地在与会者列表中看到的昵称
        pathLocalBefore = self.screeshot_path + "test_updateNickName_e.jpg"
        avc_ios.getScreenshot(filename=pathLocalBefore)
        avc_ios.back()
        avc_ios.leaveChannel()
        avc_ios.goMine()
        path1 = self.screeshot_path + "test_updateNickName_a.jpg"
        path2 = self.screeshot_path + "test_updateNickName_b.jpg"
        avc_ios.getScreenshot(filename=path1)
        avc_ios.updateNickname("nickName1")
        avc_ios.getScreenshot(filename=path2)
        # 判断本地是否更换昵称成功
        assert verify_utils.compare_images(path1, path2) == "Success"
        avc_ios.back()
        avc_ios.joinChannelSecond()
        avc_ios.goToParticipantList()
        # 更新昵称后，本地在与会者列表中看到的昵称
        pathLocalAfter = self.screeshot_path + "test_updateNickName_f.jpg"
        avc_ios.getScreenshot(filename=pathLocalAfter)
        # 判断本地与会者列表中昵称是否更新
        assert verify_utils.compare_images(pathLocalBefore, pathLocalAfter) == "Success"
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.downIcon()
        avc_android.goToParticipantList()
        # 更新昵称后，远端在与会者列表中看到的昵称
        pathRemoteAfter = self.screeshot_path + "test_updateNickName_d.jpg"
        avc_android.getScreenshot(filename=pathRemoteAfter)
        avc_android.back()
        avc_android.leaveChannel()
        # 判断远端与会者列表中昵称是否更新
        assert verify_utils.compare_images(pathRemoteBefore, pathRemoteAfter) == "Success"

    '''
        3771， 4345（1）更换昵称，查看消息列表中昵称是否改变
    '''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_updateNickNameToSeeInMessage(self):
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        # 本地在更换昵称前发送消息
        avc_ios.sendMessage("aaaa")
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.downIcon()
        avc_android.downIcon()
        avc_android.readMessage()
        path1 = self.screeshot_path + "test_updateNickName_g.jpg"
        # path2保存远端在本地更改昵称前看到的昵称
        path2 = self.screeshot_path + "test_updateNickName_h.jpg"
        avc_android.getScreenshot(path1)
        width, height = avc_android.getImageSize(path1)
        avc_android.getCustomizeImage(path1, path2, 1 / 20 * width, 2 / 20 * height, width, 4 / 20 * height)
        avc_android.back()
        avc_android.leaveChannel()
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.back()
        avc_ios.leaveChannel()
        avc_ios.goMine()
        # 本地更改昵称
        avc_ios.updateNickname("nickName2")
        avc_ios.back()
        avc_ios.joinChannelSecond()
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        # 本地在更换昵称后发送消息
        avc_ios.sendMessage("aaaa")
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.readMessage()
        path3 = self.screeshot_path + "test_updateNickName_i.jpg"
        # path4保存远端在本地更改昵称后看到的昵称
        path4 = self.screeshot_path + "test_updateNickName_j.jpg"
        avc_android.getScreenshot(path3)
        width, height = avc_android.getImageSize(path3)
        avc_android.getCustomizeImage(path3, path4, 1 / 20 * width, 2 / 20 * height, width, 4 / 20 * height)
        # 断言远端在消息列表中看到本地的昵称前后是否改变
        assert verify_utils.compare_images(path2, path4) == "Success"

    '''
        3773 
        进入频道前设置音视频unmute，
        进入频道后音视频仍是unmute，
        道内更改音视频属性对个人设置界面没有影响
    '''
    @pytest.mark.tags(case_tag.iOS, case_tag.HIGH, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_UnmuteVideoAndAudioBeforeJoinchannel(self):
        avc = self.avcIOS
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.goMine()
        avc.preUnmuteVideo()
        avc.preUnmuteAudio()
        avc.back()
        avc.joinChannel(self.channel_name, self.password)
        assert avc.videoUnmuteExistsInChannel
        assert avc.audioUnmuteExistsInChannel
        avc.muteVideoInchannel()
        avc.muteAudioInchannel()
        avc.leaveChannel()
        avc.goMine()
        assert avc.preVideoUnMuteExists
        assert avc.preAudioUnMuteExists

    '''
        3773
        进入频道前设置本地的视频mute,音频为unmute
        进入频道后本地的视频是mute状态，音频是unmute状态
        频道内更改音视频属性对个人设置界面没有影响
    '''
    @pytest.mark.tags(case_tag.iOS, case_tag.HIGH, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_muteVideoBeforeJoinchannel(self):
        avc = self.avcIOS
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.goMine()
        avc.preUnmuteAudio()
        avc.preMuteVideo()
        avc.back()
        avc.joinChannel(self.channel_name, self.password)
        assert avc.videoMuteExistsInChannel
        assert avc.audioUnmuteExistsInChannel
        avc.muteAudioInchannel()
        avc.unmuteVideoInchannel()
        avc.leaveChannel()
        avc.goMine()
        assert avc.preAudioUnMuteExists
        assert avc.preVideoMuteExists

    '''
        3773
        进入频道前设置本地的音频mute，视频为unmute,
        进入频道后本地的音频是mute状态，视频unmute状态
        频道内更改音视频属性对个人设置界面没有影响
    '''
    @pytest.mark.tags(case_tag.iOS, case_tag.HIGH, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_muteAudioBeforeJoinchannel(self):
        avc = self.avcIOS
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.goMine()
        avc.preUnmuteVideo()
        avc.preMuteAudio()
        avc.back()
        avc.joinChannel(self.channel_name, self.password)
        assert avc.audioMuteExistsInChannel
        assert avc.videoUnmuteExistsInChannel
        avc.unmuteAudioInchannel()
        avc.muteVideoInchannel()
        avc.leaveChannel()
        avc.goMine()
        assert avc.preAudioMuteExists
        assert avc.preVideoUnMuteExists

    '''
        3774
        只有一个主播主播大屏显示
        大小窗口可切换主播上大屏显示
        大屏主播退出频道后，随机一人上大屏显示
        大屏主播mute音视频之后，随机一人上大屏显示    
    '''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_smallAndBigwindowChange(self):
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        pathSingleEnter = self.screeshot_path + "test_smallAndBigwindowchange_a.jpg"
        pathdoubleEnter = self.screeshot_path + "test_smallAndBigwindowchange_b.jpg"
        # pathLeaveBefore = self.screeshot_path + "test_smallAndBigwindowchange_c.jpg"
        pathLeaveAfter = self.screeshot_path + "test_smallAndBigwindowchange_d.jpg"
        pathMuteBefore = self.screeshot_path + "test_smallAndBigwindowchange_e.jpg"
        pathMuteAfter = self.screeshot_path + "test_smallAndBigwindowchange_f.jpg"
        # 只有一个主播，主播大屏显示
        avc_ios.getScreenshot(filename=pathSingleEnter)
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.getScreenshot(filename=pathdoubleEnter)
        assert verify_utils.compare_images(pathSingleEnter, pathdoubleEnter) == "Success"
        # 将某个主播设置为大屏
        # avc_ios.smallAndBigwindowChange()
        # avc_ios.getScreenshot(filename=pathLeaveBefore)
        # assert verify_utils.compare_images(pathdoubleEnter, pathLeaveBefore) == "Success"
        # 大屏主播退出会议，随机一人上大屏显示
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.downIcon()
        avc_android.leaveChannel()
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.getScreenshot(filename=pathLeaveAfter)
        assert verify_utils.compare_images(pathdoubleEnter, pathLeaveAfter) == "Success"
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.joinChannel(self.channel_name,self.password)
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        # 将某个主播设置为大屏
        # avc_ios.smallAndBigwindowChange()
        # pathMuteBefore 保存大屏主播mute音视频之前本地看到的大屏幕
        avc_ios.getScreenshot(filename=pathMuteBefore)
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.downIcon()
        avc_android.downIcon()
        # 大屏主播mute音视频变成观众，随机一人上大屏显示
        avc_android.muteAudioInchannel()
        avc_android.muteVideoInchannel()
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        # pathMuteAfter 保存大屏主播mute音视频之后本地看到的大屏幕
        avc_ios.getScreenshot(filename=pathMuteAfter)
        assert verify_utils.compare_images(pathMuteBefore, pathMuteAfter) == "Success"

    '''3775本地前后摄像头切换'''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_frontAndRearCameras(self):
        avc = self.avcIOS
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.joinChannel(self.channel_name, self.password)
        path1 = self.screeshot_path + "test_frontAndRearCameras_a.jpg"
        path2 = self.screeshot_path + "test_frontAndRearCameras_b.jpg"
        avc.getScreenshot(filename=path1)
        avc.frontAndRearCameras()
        avc.getScreenshot(filename=path2)
        assert verify_utils.compare_images(path1, path2) == "Success"

    '''3776网络质量显示'''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_NetWorkInfo(self):
        avc = self.avcIOS
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        assert avc.goodNetWorkExistsOUT
        avc.joinChannel(self.channel_name, self.password)
        assert avc.goodNetWorkExistsInchannel
        avc.home()
        avc.closeNeWork()
        avc.startAVC(self.packageName)
        assert avc.badNetWorkExistsOUT
        avc.joinChannel(self.channel_name, self.password)
        assert avc.badNetWorkExistsInchannel


    '''3777会议参与者在频道内说话音频图标显示'''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_audioExist(self):
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        assert avc_ios.audioExistInChannel

    '''3777mute音频的人说话，另一方看到mute的人视频窗口显示麦克风关闭状态'''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_disAudioExist(self):
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_android.muteAudioInchannel()
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        assert avc_ios.disAudioExistInChannel

    '''
        3778
        会议中可以发送接受消息
        读完消息数字消失
        链接可正常跳转
        可复制聊天页面的消息并发送
    '''
    @pytest.mark.tags(case_tag.iOS, case_tag.HIGH, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_sendMsg(self):
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        msg1 = ["qwreqwirghiuqwhfiahfiwefhwef","1231243124134",",/.[]]["
                ,"👌","测试成功","www.baidu.com"]
        msg2 = "hello"
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.sendMessage(msg1)
        avc_ios.back()
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.downIcon()
        avc_android.sendMessage(msg2)
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.readMessage()
        # 复制消息
        avc_ios.copyHistroyMessageAndSend()
        avc_ios.back()
        # 读完消息之后，消息图标上的数字应该消失
        assert avc_ios.numberMissAfterReadExits
        avc_ios.sendMessage("www.baidu.com")
        # 链接跳转
        avc_ios.clickLink()


    '''
        3779, 3794c 
        在频道内mute音频,
        远端看到本地的音频状态为mute
    '''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_muteAudioInchannel(self):
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        avc_ios.muteAudioInchannel()
        avc_ios.unmuteAudioInchannel()
        assert avc_ios.audioMuteExistsInChannel
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        assert avc_android.muteAudioIconExist

    '''
        3779 3794b
        在频道内mute视频,远端看不到本地
    '''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_muteVideoInchannel(self):
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        avc_ios.muteVideoInchannel()
        avc_ios.unmuteAudioInchannel()
        assert avc_ios.videoMuteExistsInChannel
        # 本地切换为观众
        assert avc_ios.nameExists
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        # 远端切换为观众
        assert avc_android.nameExists

    '''
        3779 3794a
        在频道内同时mute音视频，切为观众
    '''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_muteVideoAndAudioInchannel(self):
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        avc_ios.muteVideoInchannel()
        avc_ios.muteAudioInchannel()
        # 本地切换为观众
        assert avc_ios.nameExists

    '''
        3780 ,3789
        存在主持人，非主持人查看与会者，主持人后显示host图标，
        显示所有人的音频状态，但无法操作该状态
    '''
    def test_disHostUnMuteOthers(self):
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_android.muteAudioInchannel()
        avc_android.muteVideoInchannel()
        avc_android.goSettingInChannel()
        avc_android.applyToHost()
        avc_android.back()
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        avc_ios.goToParticipantList()
        # 非主持人看到主持人后面显示主持人图标
        assert avc_ios.OthersHostIconExist
        # unmute音频
        avc_ios.unMutuOthersAudio()
        assert avc_ios.othersAudioMuteExists
        avc_ios.cancel()
        # unmute视频
        avc_ios.unMutuOthersVideo()
        assert avc_ios.othersVideoMuteExists
        avc_ios.cancel()
        # 踢人
        avc_ios.getOthersOut()
        assert avc_ios.cannotKickOther
        avc_ios.cancel()

    ''' 
        3780 
        存在主持人，主持人查看与会者，
        显示所有人的音频状态，可以对音视频状态，踢人进行操作
    '''
    def test_hostUnMuteOthers(self):
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_android.muteAudioInchannel()
        avc_android.muteVideoInchannel()
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        avc_ios.goSettingInChannel()
        avc_ios.applyToHost()
        avc_ios.back()
        avc_ios.goToParticipantList()
        # unmute音频
        avc_ios.unMutuOthersAudio()
        assert avc_ios.inviteExists
        avc_ios.sureClickUnmute()
        # unmute视频
        avc_ios.unMutuOthersVideo()
        assert avc_ios.inviteExists
        avc_ios.sureClickUnmute()
        # 踢人
        avc_ios.getOthersOut()
        assert avc_ios.inviteExists
        avc_ios.sureClickUnmute()

    '''3780动态显示与会者列表人数'''
    def test_dynamicDisplayParticipants(self):
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        avc_ios.goToParticipantList()
        path1 = self.screeshot_path + "test_checkParticipants_a.jpg"
        path2 = self.screeshot_path + "test_checkParticipants_b.jpg"
        avc_ios.getScreenshot(filename=path1)
        width, height = avc_ios.getImageSize(path1)
        avc_ios.getCustomizeImage(path1, path2, 1 / 3 * width, 1 / 20 * height, 2 / 3 * width, 1 / 8 * height)
        avc_ios.getNumberOfParticipants(path2)
        assert avc_ios.getNumberOfParticipants(path2) == 1
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        # 远端加入频道
        avc_android.joinChannel(self.channel_name, self.password)
        # 本地查看房间人数有没有动态更新为2
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        path3 = self.screeshot_path + "test_checkParticipants_c.jpg"
        path4 = self.screeshot_path + "test_checkParticipants_d.jpg"
        avc_ios.getScreenshot(filename=path3)
        width, height = avc_ios.getImageSize(path3)
        avc_ios.getCustomizeImage(path3, path4, 1 / 3 * width, 1 / 20 * height, 2 / 3 * width, 1 / 8 * height)
        avc_ios.getNumberOfParticipants(path4)
        assert avc_ios.getNumberOfParticipants(path4) == 2
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.downIcon()
        # 远端退出频道
        avc_android.leaveChannel()
        # 本地查看房间人数有没有动态更新为1
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        path5 = self.screeshot_path + "test_checkParticipants_c.jpg"
        path6 = self.screeshot_path + "test_checkParticipants_d.jpg"
        avc_ios.getScreenshot(filename=path5)
        width, height = avc_ios.getImageSize(path5)
        avc_ios.getCustomizeImage(path5, path6, 1 / 3 * width, 1 / 20 * height, 2 / 3 * width, 1 / 8 * height)
        avc_ios.getNumberOfParticipants(path6)
        assert avc_ios.getNumberOfParticipants(path6) == 1

    '''
        3781
        点击主持人的info按钮，会有文字说明
        存在主持人，无法更改房间内属性
        不存在主持人，可以申请成为主持人
        更改房间属性后，本地加入房间后与设置的房间音视频属性一致
    '''
    def test_channelSettings(self):
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_android.goSettingInChannel()
        avc_android.applyToHost()
        avc_android.back()
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        avc_ios.goSettingInChannel()
        # 点击主持人说明
        avc_ios.hostInfoClick()
        assert avc_ios.hostIconExists
        # 点击房间属性，非主持人无法点击
        avc_ios.roomSettingClick()
        # 存在主持人，无法更改房间内属性
        assert avc_ios.roomSettingExists
        avc_ios.back()
        avc_ios.leaveChannel()
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.downIcon()
        avc_android.goSettingInChannel()
        avc_android.muteChannelVideo()
        avc_android.muteChannelAudio()
        # 远端放弃主持人权限
        avc_android.disApplyToHost()
        avc_android.back()
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.joinChannelSecond()
        # 本地加入房间后的属性与房间属性一致
        assert avc_ios.audioMuteExistsInChannel
        assert avc_ios.videoMuteExistsInChannel
        avc_ios.goSettingInChannel()
        # 不存在主持人，可以申请成为主持人
        avc_ios.applyToHost()
        avc_ios.back()
        assert avc_ios.hostIconExists

    '''
        3782断网后修改房间音视频属性    
    '''
    def test_offNetWorkChangeRoomSetting(self):
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        avc_ios.goSettingInChannel()
        # 设置房间的音视频属性为mute
        avc_ios.muteChannelVideo()
        avc_ios.muteChannelAudio()
        avc_ios.back()
        # avc_ios.startAVC(self.packageName)
        # avc_ios.joinChannel(self.channel_name, self.password)
        # 远端加入音视频mute属性的房间
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_ios.setCurrentDevice(0)
        # 本地断网，远端修改房间音视频属性
        avc_ios.closeNetWork()
        avc_android.setCurrentDevice(1)
        path1 = self.screeshot_path + "test_offNetWork1.jpg"
        avc_android.getScreenshot(filename=path1)
        avc_android.goSettingInChannel()
        avc_android.UnmuteChannelAudio()
        avc_android.UnmuteChannelVideo()
        avc_android.back()
        # 本地联网
        avc_ios.setCurrentDevice(0)
        avc_ios.openNetWork()
        sleep(5)
        avc_android.setCurrentDevice(1)
        path2 = self.screeshot_path + "test_offNetWork2.jpg"
        avc_android.getScreenshot(filename=path2)
        # 断网后重连网络，音视频仍不会互通
        assert verify_utils.compare_images(path1, path2) == "Success"
        # 进入音视频属性为unmute的房间
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        avc_ios.closeNetWork()
        avc_android.setCurrentDevice(0)
        path3 = self.screeshot_path + "test_offNetWork3.jpg"
        avc_android.getScreenshot(filename=path3)
        avc_android.downIcon()
        avc_android.goSettingInChannel()
        avc_android.muteChannelAudio()
        avc_android.muteChannelVideo()
        avc_ios.setCurrentDevice(0)
        avc_ios.openNetWork()
        sleep(5)
        avc_android.setCurrentDevice(1)
        path4 = self.screeshot_path + "test_offNetWork4.jpg"
        avc_android.getScreenshot(filename=path4)
        # 断网后重连网络，音视频仍会互通
        assert verify_utils.compare_images(path3, path4) == "Success"

    '''
        3784断网过程中，被mute/unmute后重新联网    
    '''
    def test_offNetWorkBeMuteThanOpenNet(self):
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_ios.setCurrentDevice(0)
        avc_ios.closeNetWork()
        avc_android.setCurrentDevice(1)
        avc_android.goToParticipantList()
        avc_android.muteOthersAudio()
        avc_android.muteOthersVideo()
        # 本地联网
        avc_ios.setCurrentDevice(0)
        avc_ios.openNetWork()
        sleep(5)
        avc_ios.home()
        avc_ios.openAVC()
        assert avc_ios.audioUnmuteExistsInChannel
        assert avc_ios.videoUnmuteExistsInChannel


    '''3787 3788无主持人时，与会者邀请远端unmute音视频，以及踢人'''
    def test_NoHostUnMuteOthers(self):
        # 启动android
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_android.muteAudioInchannel()
        avc_android.muteVideoInchannel()
        # 启动ios
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        avc_ios.goToParticipantList()
        # unmute音频
        avc_ios.unMutuOthersAudio()
        assert avc_ios.inviteExists
        avc_ios.sureClickUnmute()
        # unmute视频
        avc_ios.unMutuOthersVideo()
        assert avc_ios.inviteExists
        avc_ios.sureClickUnmute()
        # 踢人
        avc_ios.getOthersOut()
        assert avc_ios.inviteExists
        avc_ios.sureClickUnmute()

    # '''3789存在主持人，非主持人邀请远端unmute音视频，以及踢人，不会出现弹窗'''
    # def test_disHostUnMuteOthers(self):
    #     # 启动android
    #     avc_android = self.avcAndroid
    #     avc_android.setCurrentDevice(1)
    #     avc_android.startAVC(self.packageName_android)
    #     avc_android.joinChannel(self.channel_name, self.password)
    #     avc_android.muteAudioInchannel()
    #     avc_android.muteVideoInchannel()
    #     avc_android.goSettingInChannel()
    #     avc_android.applyToHost()
    #     avc_android.back()
    #     # 启动ios
    #     avc_ios = self.avcIOS
    #     avc_ios.setCurrentDevice(0)
    #     avc_ios.startAVC(self.packageName)
    #     avc_ios.joinChannel(self.channel_name, self.password)
    #     avc_ios.goToParticipantList()
    #
    #     # unmute音频
    #     avc_ios.unMutuOthersAudio()
    #     # bug
    #     assert_not_exists(avc_ios.inviteExists)
    #     # unmute视频
    #     avc_ios.unMutuOthersVideo()
    #     # bug
    #     assert_not_exists(avc_ios.inviteExists)
    #     # 踢人
    #     avc_ios.getOthersOut()
    #     # bug
    #     assert_not_exists(avc_ios.inviteExists)

    ''' 3789存在主持人，主持人可以邀请远端unmute音视频，以及踢人'''
    def test_HostUnMuteOthers(self):
        # 启动android
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_android.muteAudioInchannel()
        avc_android.muteVideoInchannel()
        # 启动ios
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        avc_ios.goSettingInChannel()
        avc_ios.applyToHost()
        avc_ios.back()
        avc_ios.goToParticipantList()
        # unmute音频
        avc_ios.unMutuOthersAudio()
        assert avc_ios.inviteExists
        # unmute视频
        avc_ios.unMutuOthersVideo()
        assert avc_ios.inviteExists
        # 踢人
        avc_ios.getOthersOut()
        assert avc_ios.inviteExists

    ''' 3790后台状态，远端发起unmute音视频邀请'''
    def test_homeStatusRemoteUnmute(self):
        # 启动ios
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        avc_ios.muteAudioInchannel()
        avc_ios.muteVideoInchannel()
        avc_ios.home()
        # 启动android
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_android.goToParticipantList()
        # unmute音频
        avc_android.unMutuOthersAudio()
        # unmute视频
        avc_android.unMutuOthersVideo()
        sleep(3)
        path1 = self.screeshot_path + "test_homeStatusRemoteUnmute_01.jpg"
        path2 = self.screeshot_path + "test_homeStatusRemoteUnmute_02.jpg"
        avc_android.getScreenshot(path1)
        width, height = avc_ios.getImageSize(path1)
        avc_android.getCustomizeImage(path1, path2, 1 / 20 * width, 74 / 80 * height, 11 / 12 * width, 79 / 80 * height)
        info = avc_android.getWordsInImage(path2)
        print(info)

    ''' 3793音视频unmute窗口分开显示'''
    def test_audioAndVideoDiffUmnuteWindows(self):
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        avc_ios.muteAudioInchannel()
        avc_ios.muteVideoInchannel()
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_android.goToParticipantList()
        # unmute音频
        avc_android.unMutuOthersAudio()
        assert avc_ios.inviteExists
        # unmute视频
        avc_android.unMutuOthersVideo()
        assert avc_ios.inviteExists

    ''' 3797获取版本号 '''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_getAppVersion(self):
        avc = self.avcIOS
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        assert avc.versionExist
        avc.versionClick()
        assert avc.RTCExist
        avc.RTCClick()
        assert avc.RTMExist
        avc.RTMClick()
        assert avc.buildExist

    '''
        3791断网过程中，远端发起unmute音视频邀请  
    '''
    def test_offNetWorkRemoteUnmute(self):
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_ios.setCurrentDevice(0)
        avc_ios.muteVideoInchannel()
        avc_ios.muteAudioInchannel()
        avc_ios.closeNetWork()
        avc_android.setCurrentDevice(1)
        avc_android.goToParticipantList()
        avc_android.unMutuOthersAudio()
        avc_android.unMutuOthersVideo()
        # 本地联网
        avc_ios.setCurrentDevice(0)
        avc_ios.openNetWork()
        sleep(5)
        avc_ios.home()
        avc_ios.openAVC()
        assert avc_ios.audioUnmuteExistsInChannel
        assert avc_ios.videoUnmuteExistsInChannel

    '''3799主持人icon显示'''
    def test_hostIcon(self):
        # 启动android
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_android.goSettingInChannel()
        avc_android.applyToHost()
        # avc_android.back()
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        # 频道内存在主持人，通话界面显示主持人图标
        sleep(5)
        path1 = self.screeshot_path + "test_hostIcon1.jpg"
        avc_ios.getScreenshot(path1)
        assert avc_ios.hostIconExists
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.back()
        avc_android.downIcon()
        # 主持人退出频道再重新进入
        avc_android.leaveChannel()
        avc_android.joinChannel(self.channel_name, self.password)
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        sleep(5)
        assert avc_ios.hostIconExists
        # 原主持人放弃主持人权限
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.downIcon()
        avc_android.goSettingInChannel()
        avc_android.disApplyToHost()
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        sleep(10)
        path2 = self.screeshot_path + "test_hostIcon2.jpg"
        avc_ios.getScreenshot(path2)
        assert verify_utils.compare_images(path1, path2) == "Success"

    '''4343房间密码说明'''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_passwordInfo(self):
        avc = self.avcIOS
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.passwordInfoClick()
        avc.passwordInfoExists

    '''4345设置昵称，mute音视频昵称显示情况'''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_setNickNameMute(self):
        avc = self.avcIOS
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.goMine()
        avc.updateNickname("ios")
        avc.back()
        avc.joinChannel(self.channel_name, self.password)
        avc.muteAudioInchannel()
        avc.muteVideoInchannel()
        assert avc.nameExists

    '''4346房间时长显示'''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_channeltime_info(self):
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        sleep(1)
        path = self.screeshot_path + "test_channeltime_01.jpg"
        path1 = self.screeshot_path + "test_channeltime_02.jpg"
        avc_ios.getScreenshot(path)
        width, height = avc_ios.getImageSize(path)
        avc_ios.getCustomizeImage(path, path1, 1 / 20 * width, 5 / 80 * height, 2/ 6 * width, 7 / 80 * height)
        channeltime_first = avc_ios.getWordsInImage(path1)
        print("<<<<", channeltime_first)
        # assert channeltime_first >= "00:00:00" and channeltime_first <= "00:00:05"
        # 远端加入房间
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        channeltime_remote1 = avc_android.remoteTime
        print("<<<<", channeltime_remote1)
        # assert channeltime_remote1 >= "00:00:05" and channeltime_remote1 <= "00:01:05"
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        # 本地退出房间，远端时长继续累加
        avc_ios.leaveChannel()
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.downIcon()
        avc_android.downIcon()
        channeltime_remote2 = avc_android.remoteTime
        print("<<<<", channeltime_remote2)
        # assert channeltime_remote2 >= "00:00:05" and channeltime_remote2 <= "00:01:05"
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        # 本地继续加入房间，现场当前进行中的时长
        avc_ios.joinChannelSecond()
        sleep(1)
        path2 = self.screeshot_path + "test_channeltime_03.jpg"
        path3 = self.screeshot_path + "test_channeltime_04.jpg"
        avc_ios.getScreenshot(path2)
        width, height = avc_ios.getImageSize(path2)
        avc_ios.getCustomizeImage(path2, path3, 1 / 20 * width, 5 / 80 * height, 2 / 6 * width, 7 / 80 * height)
        channeltime_second = avc_ios.getWordsInImage(path3)
        print("<<<<", channeltime_second)
        # assert channeltime_second >= "00:00:00" and channeltime_second <= "00:00:05"


    '''4689进入会议室后不可修改密码'''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_changePassWordInChannel(self):
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        avc_ios.leaveChannel()
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(roomName=self.channel_name, password="changePassword")
        assert avc_ios.errorPasswordInfo

    '''4347closeAndOpen  rtm '''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_rtmCloseAndOpen(self):
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name,self.password)
        avc_ios.goMine()
        avc_ios.openDeveloperInChannel()
        avc_ios.closeRTM()
        # rtm断线的业务图标存在
        assert avc_ios.rtmDisConnectIconExists
        avc_ios.openDeveloperInChannel()
        avc_ios.openRTM()
        avc_ios.back()
        # 重连rtm，业务图标消失，可发送消息
        avc_ios.sendMessage("aaaa")

    '''4362, 4551 断开rtm，媒体功能自测'''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_rtmCloseMediaTest(self):
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.goMine()
        avc_ios.openDeveloperOUT()
        avc_ios.closeRTM()
        avc_ios.back()
        # 输入正确的密码，音视频会被纠正过来
        avc_ios.joinChannel(self.channel_name, self.password)
        assert avc_ios.audioExistInChannel
        assert avc_ios.videoExistInChannel
        avc_ios.muteAudioInchannel()
        avc_ios.goSettingInChannel()
        # 点击房间设置，业务功能无法使用
        avc_ios.roomSettingClick()
        assert avc_ios.roomSettingExists
        avc_ios.back()
        avc_ios.goToParticipantList()
        avc_ios.mutuOthersAudio()
        avc_ios.back()
        avc_ios.back()
        # mute视频，媒体功能无法使用
        avc_ios.muteVideoInchannel()
        avc_ios.goToParticipantList()
        # 不能mute，提示服务器未连接
        avc_ios.mutuOthersVideo()
        assert avc_ios.disConnetExists
        avc_ios.back()
        avc_ios.back()
        avc_ios.leaveChannel()
        # 输入错误的密码，不提示有无密码，以及密码是否正确
        avc_ios.reSetPassword("fsasfas")
        assert avc_ios.audioMuteExistsInChannel
        assert avc_ios.videoMuteExistsInChannel
        avc_ios.leaveChannel()

    '''4531频道外断开rtm，本地默认关闭音视频'''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_rtmCloseMute(self):
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.goMine()
        avc_ios.openDeveloperOUT()
        avc_ios.closeRTM()
        avc_ios.back()
        avc_ios.joinChannel(self.channel_name, self.password)
        assert avc_ios.audioMuteExistsInChannel
        assert avc_ios.videoMuteExistsInChannel
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        # 远端不断开rtm加入频道，音视频会被纠正过来
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        assert avc_ios.audioExistInChannel
        assert avc_ios.videoExistInChannel
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.downIcon()
        avc_android.downIcon()
        avc_android.goSettingInChannel()
        avc_android.muteChannelAudio()
        avc_android.muteChannelVideo()
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.goSettingInChannel()
        # 远端更改房间音视频mute，本地房间音视频为mute
        assert avc_ios.muteChannelAudioExists
        assert avc_ios.muteChannelVideoExists
        avc_ios.slide()
        # 频道内重连rtm，本地音视频不会被mute
        avc_ios.openDeveloperInChannel()
        avc_ios.openRTM()
        avc_ios.back()
        assert avc_ios.audioUnmuteExistsInChannel
        assert avc_ios.videoUnmuteExistsInChannel
        # 退出频道重新进入频道，本地音视频被mute
        avc_ios.leaveChannel()
        avc_ios.joinChannelSecond()
        assert avc_ios.audioMuteExistsInChannel
        assert avc_ios.videoMuteExistsInChannel

    '''4548 （1-5） 本地rtm断开，开config，加入存在的房间，房间密码显示'''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_rtmClosejoinOthers(self):
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.goMine()
        avc_ios.openDeveloperOUT()
        avc_ios.closeRTM()
        avc_ios.back()
        # 断开rtm，输入正确的密码，房间设置界面显示房间名和房间密码
        avc_ios.joinChannel(self.channel_name,self.password)
        avc_ios.goSettingInChannel()
        assert avc_ios.channelInfoExists
        avc_ios.back()
        avc_ios.leaveChannel()
        # 断开rtm，输入错误的房间密码，本地与远端不互通
        avc_ios.reSetPassword("adfasfas")
        avc_ios.goToParticipantList()
        path3 = self.screeshot_path + "test_checkParticipants_c.jpg"
        path4 = self.screeshot_path + "test_checkParticipants_d.jpg"
        avc_ios.getScreenshot(filename=path3)
        width, height = avc_ios.getImageSize(path3)
        avc_ios.getCustomizeImage(path3, path4, 1 / 3 * width, 1 / 20 * height, 2 / 3 * width, 1 / 8 * height)
        avc_ios.getNumberOfParticipants(path4)
        assert avc_ios.getNumberOfParticipants(path4) == 1
        avc_ios.back()
        avc_ios.leaveChannel()
        avc_ios.reSetPassword("")
        # 断开rtm，不输入密码，本地与远端不互通
        avc_ios.goToParticipantList()
        path1 = self.screeshot_path + "test_checkParticipants_a.jpg"
        path2 = self.screeshot_path + "test_checkParticipants_b.jpg"
        avc_ios.getScreenshot(filename=path1)
        width, height = avc_ios.getImageSize(path1)
        avc_ios.getCustomizeImage(path1, path2, 1 / 3 * width, 1 / 20 * height, 2 / 3 * width, 1 / 8 * height)
        avc_ios.getNumberOfParticipants(path2)
        assert avc_ios.getNumberOfParticipants(path2) == 1
        avc_ios.back()
        avc_ios.leaveChannel()

    '''4548 （6- 9） 本地rtm断开创建房间，远端加入房间，房间密码显示'''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_rtmCloseCreateRoom(self):
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.goMine()
        avc_ios.openDeveloperOUT()
        avc_ios.closeRTM()
        avc_ios.back()
        avc_ios.joinChannel(self.channel_name,self.password)
        # 远端不输入房间密码,不互通，只显示本地（远端创建了房间，本地断开rtm创建的房间不会被业务服务器获取到）
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(roomName=self.channel_name, password="")
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.goToParticipantList()
        path1 = self.screeshot_path + "test_checkParticipants_a.jpg"
        path2 = self.screeshot_path + "test_checkParticipants_b.jpg"
        avc_ios.getScreenshot(filename=path1)
        width, height = avc_ios.getImageSize(path1)
        avc_ios.getCustomizeImage(path1, path2, 1 / 3 * width, 1 / 20 * height, 2 / 3 * width, 1 / 8 * height)
        avc_ios.getNumberOfParticipants(path2)
        assert avc_ios.getNumberOfParticipants(path2) == 1
        # 远端输入错误的房间密码，无法加入房间，提示密码错误(在远端创建的房间销毁之前)
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.leaveChannel()
        avc_android.joinChannel(roomName=self.channel_name,password="errorpassword")
        assert avc_android.errorPasswordInfo
        #  远端输入正确的房间密码，正常加入频道（在远端创建的房间被业务服务器销毁之后）
        sleep(100)
        avc_android.joinChannel(self.channel_name,self.password)
        avc_android.goSettingInChannel()
        path = self.screeshot_path + "test_channelInfoToSee.jpg"
        avc_android.getScreenshot(filename=path)

    '''4548 （10-12）本地断开rtm，输入随机密码加入存在的房间，频道内重连rtm，提示密码错误被退出房间'''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_rtmClosejoinThanOpenRTM(self):
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.goMine()
        avc_ios.openDeveloperOUT()
        avc_ios.closeRTM()
        avc_ios.back()
        avc_ios.joinChannel(roomName=self.channel_name,password="dfadsfads")
        avc_ios.goSettingInChannel()
        avc_ios.openDeveloperInChannel()
        avc_ios.openRTM()
        # 提示密码错误，并且被退出房间
        # assert
        avc_ios.joinChannelSecond()






    # '''查看与会者列表人数'''
    # @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    # def test_checkParticipants(self):
    #     avc = self.avcIOS
    #     avc.setCurrentDevice(0)
    #     avc.startAVC(self.packageName)
    #     avc.joinChannel(self.channel_name,self.password)
    #     avc.goToParticipantList()
    #     path = self.screeshot_path+"test_checkParticipants_a.jpg"
    #     path1 = self.screeshot_path+"test_checkParticipants_b.jpg"
    #     avc.getScreenshot(filename=path)
    #     width,height = avc.getImageSize(path)
    #     avc.getCustomizeImage(path,path1,1/3*width,1/20*height,2/3*width,1/8*height)
    #     avc.getNumberOfParticipants(path1)
    #     assert avc.getNumberOfParticipants(path1) == 1




    # '''点击主持人的info按钮会有提示消息'''
    # def test_hostIconClick(self):
    #     avc = self.avcIOS
    #     avc.setCurrentDevice(0)
    #     avc.startAVC(self.packageName)
    #     avc.joinChannel(self.channel_name, self.password)
    #     avc.goSettingInChannel()
    #     avc.hostInfoClick()
    #     assert avc.hostIconExists

    # '''3781无主持人，申请主持人，显示主持人图标'''
    #
    # def test_hostIcon(self):
    #     avc = self.avcIOS
    #     avc.setCurrentDevice(0)
    #     avc.startAVC(self.packageName)
    #     avc.joinChannel(self.channel_name, self.password)
    #     avc.goSettingInChannel()
    #     avc.applyToHost()
    #     avc.back()
    #     assert avc.hostIconExists





    # #进入会议前只mute音频，远端可以看到视频听不到声音
    # def test_preMuteAudioThanInChannel(self):
    #     # 启动ios
    #     avc_ios = self.avcIOS
    #     avc_ios.setCurrentDevice(0)
    #     avc_ios.startAVC(self.packageName)
    #     avc_ios.joinChannel(self.channel_name, self.password)
    #     # 启动android
    #     avc_android = self.avcAndroid
    #     avc_android.setCurrentDevice(1)
    #     avc_android.startAVC(self.packageName_android)
    #     avc_android.goMine()
    #     #打开视频，关闭麦克风
    #     avc_android.preUnmuteVideo()
    #     avc_android.preMuteAudio()
    #     #返回，加入频道
    #     avc_android.back()
    #     avc_android.joinChannel(self.channel_name, self.password)
    #     # 启动ios
    #     avc_ios = self.avcIOS
    #     avc_ios.setCurrentDevice(0)
    #     assert avc_ios.disAudioExistInChannel
    #
    # #进入会议前只mute视频，远端可以看到视频听不到声音
    # def test_preMuteVideoThanInChannel(self):
    #     # 启动ios
    #     avc_ios = self.avcIOS
    #     avc_ios.setCurrentDevice(0)
    #     avc_ios.startAVC(self.packageName)
    #     avc_ios.joinChannel(self.channel_name, self.password)
    #     # 启动android
    #     avc_android = self.avcAndroid
    #     avc_android.setCurrentDevice(1)
    #     avc_android.startAVC(self.packageName_android)
    #     avc_android.goMine()
    #     #打开麦克风，关闭视频
    #     avc_android.preUnmuteAudio()
    #     avc_android.preMuteVideo()
    #     #返回，加入频道
    #     avc_android.back()
    #     avc_android.joinChannel(self.channel_name, self.password)
    #     # 启动ios
    #     avc_ios = self.avcIOS
    #     avc_ios.setCurrentDevice(0)
    #     assert avc_ios.videoExistInChannel
    #
    # #进入会议前mute音视频，远端看到对方的视频框消失
    # def test_preMuteVideoAndAudioThanInChannel(self):
    #     # 启动ios
    #     avc_ios = self.avcIOS
    #     avc_ios.setCurrentDevice(0)
    #     avc_ios.startAVC(self.packageName)
    #     avc_ios.joinChannel(self.channel_name, self.password)
    #     # 启动android
    #     avc_android = self.avcAndroid
    #     avc_android.setCurrentDevice(1)
    #     avc_android.startAVC(self.packageName_android)
    #     avc_android.goMine()
    #     #关闭麦克风，关闭视频
    #     avc_android.preMuteAudio()
    #     avc_android.preMuteVideo()
    #     #返回，加入频道
    #     avc_android.back()
    #     avc_android.joinChannel(self.channel_name, self.password)
    #     # 启动ios
    #     avc_ios = self.avcIOS
    #     avc_ios.setCurrentDevice(0)
    #     assert_not_exists(avc_ios.videoExistInChannel)
    #     assert_not_exists(avc_ios.disAudioExistInChannel)































