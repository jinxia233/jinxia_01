import allure
class Test11:
    def test_a(self):
        print('aaa')
        assert 0

    @allure.step("测试登录的步骤")
    def test_b(self):
        print("bbb1")
        allure.attach("描述1","请输入用户名")
        print("bbb2")
        allure.attach("描述2","请输入密码")
        assert 1

