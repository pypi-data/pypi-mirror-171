# -*- coding: utf-8 -*-
"""
Created on 2022/9/7 4:11 PM
---------
@summary:
---------
@author: Boris
@email: boris_liu@foxmail.com
"""

import json
import os
import re
from typing import Union, List, Literal

from playwright.sync_api import Page, BrowserContext, ViewportSize, ProxySettings
from playwright.sync_api import Playwright, Browser
from playwright.sync_api import Response
from playwright.sync_api import sync_playwright

from feapder.utils import tools
from feapder.utils.log import log
from feapder.utils.webdriver.webdirver import *


class PlaywrightDriver(WebDriver):
    def __init__(
        self,
        page_on_event_callback: dict = None,
        storage_state_path=None,
        url_regexes: list = None,
        driver_type: Literal["chromium", "firefox", "webkit"] = "chromium",
        **kwargs
    ):
        """

        Args:
            page_on_event_callback: page.on() 事件的回调 如 page_on_event_callback={"dialog": lambda dialog: dialog.accept()}
            storage_state_path: 保存浏览器状态的路径
            url_regexes: 拦截接口，支持正则，数组类型
            **kwargs:
        """
        super(PlaywrightDriver, self).__init__(**kwargs)
        self.driver: Playwright = None
        self.browser: Browser = None
        self.context: BrowserContext = None
        self.page: Page = None
        self.url = None
        self.storage_state_path = storage_state_path

        self._driver_type = driver_type
        self._page_on_event_callback = page_on_event_callback
        self._cache_data = {}
        self._url_regexes = url_regexes

        self._setup()

    def _setup(self):
        # 处理参数
        if self._proxy:
            proxy = self._proxy() if callable(self._proxy) else self._proxy
            proxy = self.format_context_proxy(proxy)
        else:
            proxy = None

        user_agent = (
            self._user_agent() if callable(self._user_agent) else self._user_agent
        )

        view_size = ViewportSize(
            width=self._window_size[0], height=self._window_size[1]
        )

        # 初始化浏览器对象
        self.driver = sync_playwright().start()
        self.browser = getattr(self.driver, self._driver_type).launch(
            headless=self._headless,
            args=["--no-sandbox"],
            proxy=proxy,
            executable_path=self._executable_path,
            downloads_path=self._download_path,
        )

        if self.storage_state_path and os.path.exists(self.storage_state_path):
            self.context = self.browser.new_context(
                user_agent=user_agent,
                screen=view_size,
                viewport=view_size,
                proxy=proxy,
                storage_state=self.storage_state_path,
            )
        else:
            self.context = self.browser.new_context(
                user_agent=user_agent,
                screen=view_size,
                viewport=view_size,
                proxy=proxy,
            )

        if self._use_stealth_js:
            path = os.path.join(os.path.dirname(__file__), "../js/stealth.min.js")
            self.context.add_init_script(path=path)

        self.page = self.context.new_page()
        self.page.set_default_timeout(self._timeout * 1000)

        if self._page_on_event_callback:
            for event, callback in self._page_on_event_callback.items():
                self.page.on(event, callback)
        elif self._url_regexes:
            self.page.on("response", self.on_response)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            log.error(exc_val)

        self.quit()
        return True

    def format_context_proxy(self, proxy) -> ProxySettings:
        """
        Args:
            proxy: username:password@ip:port / ip:port
        Returns:
            {
                "server": "ip:port"
                "username": username,
                "password": password,
            }
            server: http://ip:port or socks5://ip:port. Short form ip:port is considered an HTTP proxy.
        """

        if "@" in proxy:
            certification, _proxy = proxy.split("@")
            username, password = certification.split(":")

            context_proxy = ProxySettings(
                server=_proxy,
                username=username,
                password=password,
            )
        else:
            context_proxy = ProxySettings(server=proxy)

        return context_proxy

    def save_storage_stage(self):
        if self.storage_state_path:
            os.makedirs(os.path.dirname(self.storage_state_path), exist_ok=True)
            self.context.storage_state(path=self.storage_state_path)

    def quit(self):
        self.page.close()
        self.context.close()
        self.browser.close()
        self.driver.stop()

    @property
    def domain(self):
        return tools.get_domain(self.url or self.page.url)

    @property
    def cookies(self):
        cookies_json = {}
        for cookie in self.page.context.cookies():
            cookies_json[cookie["name"]] = cookie["value"]

        return cookies_json

    @cookies.setter
    def cookies(self, val: Union[dict, List[dict]]):
        """
        设置cookie
        Args:
            val: List[{name: str, value: str, url: Union[str, NoneType], domain: Union[str, NoneType], path: Union[str, NoneType], expires: Union[float, NoneType], httpOnly: Union[bool, NoneType], secure: Union[bool, NoneType], sameSite: Union["Lax", "None", "Strict", NoneType]}]

        Returns:

        """
        if isinstance(val, list):
            self.page.context.add_cookies(val)
        else:
            cookies = []
            for key, value in val.items():
                cookies.append(
                    {"name": key, "value": value, "url": self.url or self.page.url}
                )
            self.page.context.add_cookies(cookies)

    @property
    def user_agent(self):
        return self.page.evaluate("() => navigator.userAgent")

    def on_response(self, response: Response):
        for regex in self._url_regexes:
            if re.search(regex, response.request.url):
                intercept_request = InterceptRequest(
                    url=response.request.url,
                    headers=response.request.headers,
                    data=response.request.post_data,
                )

                intercept_response = InterceptResponse(
                    request=intercept_request,
                    url=response.url,
                    headers=response.headers,
                    content=response.body(),
                    status_code=response.status,
                )
                self._cache_data[regex] = intercept_response

    def get_response(self, url_regex) -> InterceptResponse:
        return self._cache_data.get(url_regex)

    def get_text(self, url_regex):
        return (
            self.get_response(url_regex).content.decode()
            if self.get_response(url_regex)
            else None
        )

    def get_json(self, url_regex):
        return (
            json.loads(self.get_text(url_regex))
            if self.get_response(url_regex)
            else None
        )
