import Listsupplement


def GetNumberAndPosition(ParentString: str, substring: str) -> list:
    """返回字串出现次数和第一次出现位置,如无返回空列表。

    Args:
        TargetStr (str): 父串
        substring (str): 字串

    Returns:
        list: [出现次数，第一次出现位置]
    """
    outList = list()
    if substring in ParentString:
        num = ParentString.count(substring)
        position = ParentString.find(substring)
        outList.append(num)
        outList.append(position)
        return outList
    else:
        return outList


def GetSubInParentPosition(ParentString: str, substring: str) -> list:
    """返回子串在父串中所有出现位置的索引

    Args:
        ParentString (str): 父串
        substring (str): 字串

    Returns:
        list: 索引列表
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

    Args:
        inStr ([type]):字符串
        item ([type]): 填充项
        length ([type]): 预期长度

    Returns:
        [type]: 经填充后的字符串
    """
    a = len(inStr)
    for i in range(length - a):
        inStr += item
    return inStr