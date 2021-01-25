# -*- coding: utf-8 -*-
"""
@Auth ： xingqiufen
"""
import pytest

def test001():
    print("-------开始---------")
    assert  1+2==3
    print("-------结束---------")
    # result=1+2
    # if result==3:
    #     print("通过")
    # else:
    #     print("失败")

@pytest.mark.parametrize('inData,a',[(1,3)])
def test002(inData,a):
    print('*'*10+'开始'+'*'*10)
    assert inData+a==4
    print('*' * 10 + '结束' + '*' * 10)


class Test_001:
    def test_class001(self):
        assert 1+1==2


if __name__ == '__main__':
    pytest.main(['test_Fun.py','-s','--html=../testReport/result.html'])


