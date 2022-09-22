import pdb
import random
from hwprofile_cost import find_meterids_for_single_profile as cal_vmsize_cost

def calculate_vm_cost(metadata):
    # calculate only vm-profile cost..
    # Todo: storage and os cost

    meter = cal_vmsize_cost(hw_profile=metadata["metadata"]["hardwareProfile"], region=metadata["region"], os_type="windows")
    if meter:
        cost = meter[0][-2]
    else:
        cost = 0.66
    return cost*int(metadata["usagePeriod"].split('h')[0])


def process_cost(req):
    req = req[list(req.keys())[0]]
    for res in req:

        if "virtualMachines" in res["type"]:
            res.update({"cost": "${}".format(calculate_vm_cost(res))})
        else:
            res.update({"cost": "${}".format(round(random.uniform(10.0, 66.66), 2))})

    return req
