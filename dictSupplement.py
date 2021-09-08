def GetMinValueDict(inD: dict) -> list:
    """返回最小值的键值对
    """
    return list(min(inD.items(), key=lambda x: x[1]))


def GetMaxValueDict(inD: dict) -> list:
    """返回最大值的键值对
    """
    return list(max(inD.items(), key=lambda x: x[1]))


def DistNullableValue(inDist: dict) -> dict:
    """字典去空值
    """
    for key in list(inDist.keys()):
        if not inDist.get(key):
            del inDist[key]
    return inDist