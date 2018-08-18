from requests import Request


TIMEOUT = 10

class WeixinRequest(Request):
    def __init__(self, url, callback, method='GET', header=None, need_proxy=False, fail_time=0,
                 timeout=TIMEOUT):
        Request.__init__(self, method, url, header)
        self.callback = callback
        self.need_proxy = need_proxy
        self.fail_time = fail_time
        self.timeout = timeout


