#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/5/15 上午 02:33
import pytest
import requests
from common.handle_config import conf
from common.handle_log import log


@pytest.fixture(scope='class')
def login_setup():
    url = conf.get("login", "url")
    params = {"UsernameOrEmailAddress": conf.get("login", "username"),
              "Password": conf.get("login", "password"),
              "RememberMe": "false",
              "TenancyName": "Default"}
    headers = {"cookie": "ASP.NET_SessionId=p1yeborxr4wql2yu0fyiaybe",
               "content-type": "application/json;charset=UTF-8"}
    # requests.adapters.DEFAULT_RETRIES = 5
    session = requests.session()
    # session.keep_alive = False
    response = session.post(url=url, json=params, headers=headers)
    log.error(response.text)
    yield session
    session.close()


# if __name__ == '__main__':
#     login()
