# 文件必须以test_开头或者_test结尾，文件名和方法名
# 类外叫函数 类内叫方法
def test_add():
    assert 1 + 1 == 2


class TestDemo:
    def test_add1(self):
        assert 1 + 1 == 2

    def test_add2(self):
        assert 1 + 1 == 23
