import requests


class R:
    """
    requests二次封装
    """

    @staticmethod
    def try_do(json_ret):
        try:
            ret = json_ret.json()
        except:
            ret = json_ret.text
        return ret

    def req_get(self, url, datas, header):
        if url and datas:
            ret = requests.get(url=url, params=datas, headers=header)
            json_ret = self.try_do(ret)
            return json_ret
        else:
            return False

    def req_post(self, url, datas, header):
        if url and datas:
            ret = requests.post(url=url, json=datas, headers=header)
            json_ret = self.try_do(ret)
            return json_ret
        else:
            return False

    def req_put(self, url, datas, header):
        if url and datas:
            ret = requests.put(url=url, json=datas, headers=header)
            json_ret = self.try_do(ret)
            return json_ret
        else:
            return False