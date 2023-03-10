color_css_dict = {
    "red": {"background": "linear-gradient(to right, #f85032, #e73827)"},
    "orange": {"background-image": "linear-gradient(-60deg, #ff5858 0%, #f09819 100%)"},
    "blue": {"background-image": "linear-gradient(to right, #243949 0%, #517fa4 100%)"},
    "green": {"background": "linear-gradient(to right, #11998e, #38ef7d)"},
    "pink": {"background-image": "linear-gradient(to top, #fad0c4 0%, #ffd1ff 100%)"},
    "grey": {"background-image": "linear-gradient(60deg, #29323c 0%, #485563 100%)"}
    # 还有一个白色
}


word_dict = {
    "red": ["愤怒", "生气", "太差了", "糟糕", "烂透了", "遭透了"],
    "orange": ["开心", "激动", "兴奋", "不错", "很好"],
    "blue": ["悲伤", "难过", "抑郁"],
    "green": ["和平", "希望", "成长", "健康", "健身", "生命力", "peace and love", "提升", "改善"],
    "pink": ["浪漫", "甜蜜", "幸福", "恋爱", "热恋"],
    "grey": ["失望", "无意义", "人间不值得"],
}



def get_color(text):
    """
    输入文字返回七种颜色，
    如果返回None，就是没有情绪的白色
    """
    for c, w in word_dict.items():
        for item in w:
            if item in text:
                return color_css_dict[c]
    return


