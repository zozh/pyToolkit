import Listsupplement


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
        out = Listsupplement.listNullableValue(out)
    return out


def StrFilling(inStr, item, length):
    """字符串用指定字符填充到指定长度
    """
    a = len(inStr)
    for i in range(length - a):
        inStr += item
    return inStr