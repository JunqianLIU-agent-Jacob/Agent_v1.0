from openai import OpenAI
import requests

from db import get_db_conn, save_chat, get_history
from utils import mask_phone,extract_weather_city

# ai 部
def chat_robot():
    client = OpenAI(
        api_key="你的key",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )


    messages = [{'role': 'system', 'content': '1，说话简明，2，朋友人设'}]

    print('quit退出,history查询历史，what today查询天气')

    while True:
        user_text = input('你：')
        user_text = mask_phone(user_text)
        if user_text.lower() == 'quit':
            break
        elif user_text.lower() == 'history':
            get_history()
            continue
        elif user_text == 'what today':
            user_text1 = input('你想知道的地区天气：')

            kw = {'city': user_text1}

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
            response = requests.get('https://uapis.cn/api/v1/misc/weather', params=kw, headers=headers)
            user_text = response.text

        messages.append({'role': 'user', 'content': user_text})

        response = client.chat.completions.create(
            model="qwen-turbo",
            messages=messages
        )
        ai_text = response.choices[0].message.content

        print(f'Ai:{ai_text}')

        save_chat(user_text, ai_text)

if __name__ == '__main__':
    chat_robot()