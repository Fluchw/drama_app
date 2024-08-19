# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/4/8 20:58
# @Author  : jerry.zzw 
# @Email   : jerry.zzw@antgroup.com
# @FileName: server_application.py

from agentuniverse.agent_serve.web.web_booster import start_web_server
from agentuniverse.base.agentuniverse import AgentUniverse


class ServerApplication:
    """
    Server application.
    """

    @classmethod
    def start(cls):
        # AgentUniverse().start()
        AgentUniverse().start(config_path='../../config/config.toml')
        start_web_server(bind="0.0.0.0:8001")


if __name__ == "__main__":
    ServerApplication.start()
