import copy


def ListSplitting(inList: list, splitTerm: str) -> tuple:
    """将一个整列表根据分割项分割出多个小列表

    Args:
        inList (list): 列表
        Split (str): 分割项

    Returns:
        tuple: 包含多个小列表
    """
    out = list()
    temp = list()
    for sublist in inList:
        if sublist == splitTerm:
            out.append(copy.deepcopy(temp))
            temp.clear()
        else:
            temp.append(sublist)
    return tuple(out)


def listNullableValue(inlist: list) -> list:
    """列表去空值
    """
    # 列表推导式
    outList = [i for i in inlist if i != '']
    return outList


def ListFilling(line, item, length):
    """列表用指定字符填充到指定长度
    """
    a = len(line)
    for i in range(length - a):
        line.append(0)
    return line


def listEnd(end: list) -> object:
    """返回列表的最后一项，不是列表则返回空。
    """
    if type(end) == list:
        i = len(end)
        return end[i - 1]
    return None