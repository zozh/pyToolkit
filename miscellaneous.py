import math


def NumberInto(divisorp: float, dividend: float) -> int:
    """去除小数加1
    """
    t = int(divisorp / dividend)
    if divisorp % dividend != 0:
        t = t + 1
    return t


def HexadecimalConversion(num: float, outScale: int,
                          inScale: int = (10)) -> int:
    """任意进制之间转换，默认十进制转其他
    """
    i = list()
    if inScale == 10:
        while num != 0:
            i.append(num % outScale)
            num //= outScale
        i = list(map(str, i))
        s1 = "".join(i[::-1])
    return int(s1)


def numLen(num: str) -> int:
    """返回数字长度
    """
    return len(num)


def DigitalReversal(num: float) -> float:
    """大于一的数字反转输出
    提取个位n/10^0%10，十位n/10^1%10……
    //求取两数相除的商
    """
    Len = numLen(num)
    i = int()
    out = int()
    while i < Len:
        temp = num // math.pow(10, i) % 10
        out += temp * math.pow(10, Len - 1 - i)
        i += 1
    return out


def getGreatestCommonDivisor(a: int, b: int) -> int:
    """辗转相除法
    """
    if b > a:
        a, b = b, a
    if a == b:
        gcd = int(a)
    if b < 0:
        # 抛出错误
        pass
    while a % b != 0:
        gcd = a % b
        a = b
        b = gcd
    if 'gcd' in locals().keys():
        pass
    else:
        gcd = b
    return gcd


class listRewrite(list):
    """重写list类，加入自定义方法和属性
    """
    pass


def GetMinValueList(inL: list) -> object:
    pass


def GetMaxValueList(inL: list) -> object:
    pass
