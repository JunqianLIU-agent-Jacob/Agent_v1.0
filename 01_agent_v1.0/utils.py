import re

def mask_phone(text):
    text = re.sub(r'(1[3-9]\d)\d{4}(\d{4})', r'\1****\2', text)
    return text


def extract_weather_city(text):
    common_cities = ["北京", "上海", "广州", "深圳", "杭州", "南京", "成都", "重庆",
                     "武汉", "西安", "长沙", "沈阳", "青岛", "济南", "哈尔滨", "郑州"]
    for city in common_cities:
        if city in text:
            return city
    return None
