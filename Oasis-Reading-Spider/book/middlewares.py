# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import base64

proxyUser = "970242471433228288"
proxyPass = "7biQlUXy"
proxyHost = "http-short.xiaoxiangdaili.com"
proxyPort = "10010"

proxyServer = "http://%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort
}

proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta["proxy"] = proxyServer
        request.headers["Proxy-Authorization"] = proxyAuth
