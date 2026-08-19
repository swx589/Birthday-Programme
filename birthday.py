import datetime
import random


def get_constellation(month: int, day: int) -> str:
    """
    根据月份、日期判断星座
    :param month: int 月份 1‑12
    :param day: int 日期
    :return: str 星座名称
    """
    dates = (
        (1, 20, "水瓶座"),
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
        (12, 22, "摩羯座")
    )
    if day < dates[month - 1][1]:
        return dates[(month - 2 + 12) % 12][2]
    else:
        return dates[month - 1][2]


def get_random_fortune() -> str:
    """随机获取模拟运势文本"""
    fortune_list = [
        "今日整体运势良好，做事效率高，适合推进计划。爱情运平平，多和身边人沟通。财运平稳，不宜冲动消费。健康注意睡眠。",
        "今日运势中等，会遇到小阻碍，保持耐心。人际方面注意说话分寸。财运小收获。适当运动放松。",
        "今日大吉！机遇较多，适合大胆行动。贵人运佳，容易得到帮助。财运有惊喜，心情舒畅。",
        "今日需要谨慎行事，不要做重大决定。情绪容易起伏，多给自己独处时间，饮食清淡。"
    ]
    return random.choice(fortune_list)


def calc_birthday_info(input_str: str):
    """
    解析生日，计算全部信息
    :param input_str: 用户输入字符串，支持 "2000‑05‑20" 或者 "05‑20"
    :return: 结果文本字符串
    """
    parts = input_str.strip().split("-")
    year = None
    month = None
    day = None

    if len(parts) == 3:
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
    elif len(parts) == 2:
        month = int(parts[0])
        day = int(parts[1])
    else:
        raise ValueError("格式错误！请使用格式如：2000‑05‑20 或 05‑20")

    if not (1 <= month <= 12 and 1 <= day <= 31):
        raise ValueError("月份或日期不合法！")

    today = datetime.date.today()

    # 计算下一个生日
    try:
        next_birthday = datetime.date(today.year, month, day)
    except ValueError:
        raise ValueError("该日期不存在！")

    if next_birthday < today:
        next_birthday = datetime.date(today.year + 1, month, day)

    days_to_next_birth = (next_birthday - today).days
    star = get_constellation(month, day)

    output_lines = []
    output_lines.append("====生日星座运势查询结果====")
    output_lines.append(f"输入生日：{input_str}")
    output_lines.append(f"你的星座：{star}")
    output_lines.append(f"距离下一个生日还有：{days_to_next_birth} 天")

    # 如果有出生年份，计算已经活了多少天
    if year is not None:
        birth_day = datetime.date(year, month, day)
        lived_days = (today - birth_day).days
        output_lines.append(f"从出生到现在，你已经度过：{lived_days} 天")

    fortune_text = get_random_fortune()
    output_lines.append(f"\n【{star}今日运势】")
    output_lines.append(fortune_text)
    output_lines.append(f"查询时间：{datetime.datetime.now().strftime('%Y‑%m‑%d %H:%M:%S')}")

    return "\n".join(output_lines)


def export_to_file(content: str, filename: str = "生日运势结果.txt"):
    """将结果导出到本地文本文件"""
    with open(filename, mode="w", encoding="utf‑8") as f:
        f.write(content)
    print(f">>>结果已经保存到文件：{filename}")


def main():
    print("====生日查询小程序====")
    print("输入格式示例：2000‑08‑15（带年份） 或者 08‑15（仅月日）")
    user_input = input("请输入你的出生日期：")
    try:
        result = calc_birthday_info(user_input)
        print("\n" + result)
        export_to_file(result)
    except Exception as e:
        print(f"\n错误：{e}")


if __name__ == "__main__":
    main()