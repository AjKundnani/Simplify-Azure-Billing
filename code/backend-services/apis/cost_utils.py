import random


def process_cost(req):
    req = req[list(req.keys())[0]]
    for res in req:
        res[list(res.keys())[0]].update({"cost": "${}".format(round(random.uniform(10.0, 66.66), 2))})
    return req
