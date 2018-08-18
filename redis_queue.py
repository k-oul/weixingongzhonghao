from redis import StrictRedis
from pickle import loads, dumps
from request import WeixinRequest
REDIS_HOST = 'localhost'
REDIS_USER = 'root'
REDIS_PASSWORD  = ''
REDIS_PORT = 6379
REDIS_KEY = 'weixin'

class RedisQueue():
    def __init__(self):
        # 初始化数据库
        self.db = StrictRedis(host=REDIS_HOST, password=REDIS_PASSWORD, port=REDIS_PORT)

    def add(self, request):
        if isinstance(request, WeixinRequest):
            return self.db.rpush(REDIS_KEY, dumps(request))
        return False

    def pop(self):
        if self.db.llen(REDIS_KEY):
            return loads(self.db.lpop(REDIS_KEY))
        return False

    def empty(self):
        return self.db.llen(REDIS_KEY) == 0