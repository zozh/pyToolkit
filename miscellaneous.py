import math
import sys


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
        #抛出错误
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


def GetNumberAndPosition(TargetStr: str, substring: str) -> list:
    """返回字串出现次数和第一次出现位置,如无返回空列表。
    """
    outList = list()
    if substring in TargetStr:
        num = TargetStr.count(substring)
        position = TargetStr.find(substring)
        outList.append(num)
        outList.append(position)
        return outList
    else:
        return outList


def GetMinValueDict(inD: dict) -> list:
    """返回最小值的键值对
    """
    return list(min(inD.items(), key=lambda x: x[1]))


def GetMaxValueDict(inD: dict) -> list:
    """返回最大值的键值对
    """
    return list(max(inD.items(), key=lambda x: x[1]))


def GetMinValueList(inL: list) -> object:
    pass


def GetMaxValueList(inL: list) -> object:
    pass


def DistNullableValue(inDist: dict) -> dict:
    """字典去空值
    """
    for key in list(inDist.keys()):
        if not inDist.get(key):
            del inDist[key]
    return inDist


def GetSubInParentPosition(ParentString: str, substring: str) -> list:
    """返回子串在父串中出现的所有位置头部索引
    """
    # 利用切片，划分出与子串长度相同的逐个比较。两位置之间不可小于字符串长度。
    a = len(ParentString)
    b = len(substring)
    out = list()
    for n in range(0, a - b + 1):
        if ParentString[n:n + b] == substring:
            out.append(n)
    i = int()
    out = list(map(int, out))
    while i < len(out):
        j = int(1)
        while i + j < len(out):
            if out[i + j] - out[i] < b:
                out[i + j] = ''
                j += 1
            else:
                break
        i += 1
        out = listNullableValue(out)
    return out


def StrFilling(inStr, item, length):
    """字符串用指定字符填充到指定长度
    """
    a = len(inStr)
    for i in range(length - a):
        inStr += item
    return inStr
