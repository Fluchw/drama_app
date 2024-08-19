#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2024/8/11 14:58
# @Author : fluchw
# @Email  : zerozed00@qq.com
# @File   ：test_stream.py
import requests


def t_service_run_stream(data,url):

    headers = {
        "Accept": "text/event-stream",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
    }

    response = requests.post(url, headers=headers, json=data, stream=True)

    # 处理 SSE 流
    for line in response.iter_lines():
        if line:
            event_data = line.decode('utf-8')
            print(event_data)
            if event_data.startswith("data:"):
                # 去除 "data:" 前缀
                event_data = event_data[len("data:"):]
                print(event_data)


if __name__ == "__main__":
    data = {
        "service_id": "law_drama_service",
        "params": {
            "user_role": "原告方",
            "user_id": "1984",
            "input": "快还钱",
            "cur_node": "a0",
            "background": "李明诉王芳欠款纠纷案。2019年3月，李明借给王芳10万元人民币，约定一年后归还。双方没有签订书面借款合同，但有微信聊天记录为证。到2020年3月归还期限到期后，王芳以各种理由推脱，至今未归还借款。李明多次催促未果，遂向法院提起诉讼，要求王芳归还借款10万元并支付相应的利息。",
            "session_id": "112"
        }
    }
    # data = {
    #     "service_id": "law_service",
    #     "params": {
    #         "input": "张三打人一巴掌,然后赔钱五毛违法吗",
    #     }
    # }

    # url = "http://localhost:8002/service_run_stream"
    url = "http://localhost:8002/service_run"
    # url = "http://localhost:8888/service_run_stream"
    # url = "http://localhost:8888/service_run"
    t_service_run_stream(data,url)
