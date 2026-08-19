def get_constellation(month, day):
    """
    根据月份、日期判断星座
    :param month: int 月份 1‑12
    :param day: int 日期
    :return: str 星座名称
    """
    dates = ((1, 20, "水瓶座"),
             (2, 19, "双鱼座"),
             (3, 21, "白羊座"),
             (4, 20, "金牛座"),
             (5, 21, "双子座"),
             (6, 22, "巨蟹座"),
             (7, 23, "狮子座"),
             (8, 23, "处女座"),
             (9, 23, "天秤座"),
             (10, 24, "天蝎座"),
             (11, 23, "射手座"),
             (12, 22, "摩羯座"))

    if day < dates[month-1][1]:
        return dates[month-2][2]
    else:
        return dates[month-1][2]


# 模块自测，直接运行本文件可以测试
if __name__ == "__main__":
    print(get_constellation(8, 17))   # 处女座
    print(get_constellation(2, 20))   # 双鱼座