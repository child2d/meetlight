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
    "red": ["愤怒", "生气", "太差了", "糟糕", "烂透了", "遭透了","烦人","你真狗","滚","咋不去死","受够了"],
    "orange": ["开心", "激动", "兴奋", "不错", "很好","中奖","演唱会","生日","毕业","怀孕","升职","发工资","红包","奖金","蛋糕","礼物", "哈哈", "嘿嘿", "笑死"],
    "blue": ["悲伤", "难过", "抑郁","钱丢了","吃药","医院","下雨","分手","失业","车祸","去世","生病","孤独","孤儿","emo","失恋","住院"],
    "green": ["和平", "希望", "成长", "健康", "健身", "生命力", "peace and love", "提升", "改善","发芽"],
    "pink": ["浪漫", "甜蜜", "幸福", "恋爱", "热恋","婚礼","玫瑰","戒指","求婚","我爱你", "我们在一起了"],
    "grey": ["失望", "无意义", "人间不值得","灾难","全没了","活着还有什么意义","瘫痪","绝症","世界末日","完了"],
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


if __name__ == '__main__':
    print(get_color("哈哈哈"))