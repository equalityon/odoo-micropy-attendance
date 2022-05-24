def json_rpc(url, method, params):
    import json
    import random
    import urequests as rq
    data = {"jsonrpc": "2.0","method": method,"params": params,"id": random.randint(0, 1000000000),}
    return rq.post(url=url, data=json.dumps(data), headers={"Content-Type":"application/json",}).json()['result']
def call(url, service, method, *args):
    return json_rpc(url, "call", {"service": service, "method": method, "args": args})
