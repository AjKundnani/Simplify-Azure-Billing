
import csv
import os
import pandas as pd
import constant
import pdb

# filters to be applied on cost sheet to reduce data-set
meter_region = None #"US East" # "US East" #"IN West"  # "IN South" #"IN West Jio" #"IN Central"
service_family = "Compute"
cost_sheet = "None"


def read_cost_sheet(force_read_xls=False):
    pick_file = './df.pick'
    if os.path.exists(pick_file) and not force_read_xls:
        print("reading from pick file.")
        df = pd.read_pickle(pick_file)
    else:
        print("reading from xls file.")
        df = pd.read_excel(cost_sheet)
        df.to_pickle(pick_file)
    if service_family:
        df = df[df["serviceFamily"] == service_family]
    if meter_region:
        df = df[df["meterRegion"] == meter_region]
    return filter_hw_profile(df)


def filter_hw_profile(df):
    product_list = []
    for row in df.iterrows():
        # some plans are same like: D16a v4/D16as v4, but meter name dont have info
        # so we are taking help of product name to find linux/windows meter
        product = row[1]["product"].lower()
        row[1]["meterName"] = row[1]["meterName"].replace("- Expired", "")
        meters = row[1]["meterName"].split("/")
        # ignore low priority profiles
        if 'low priority' in product:
            continue

        # do not consider cloud services sub-category
        if 'Cloud Services' in row[1]['meterSubCategory']:
            continue

        # take help of product name to detect if it is promo/windows/basic
        for i in range(len(meters)):
            if 'promo' in product:
                meters[i] = meters[i] + " " + "Promo"
            if 'windows' in product:
                meters[i] = meters[i] + " " + "windows"

            if 'basic' in product:
                meters[i] = meters[i] + " " + "Basic"
            else:
                meters[i] = meters[i] + " " + "Standard"

            meters[i] = meters[i].replace("_", " ")

        for meter in meters:
            product_list.append([meter, row[1]["meterId"], row[1]["marketPrice"], row[1]["meterRegion"]])
        # print(values)
    return product_list


def find_meter_info_for_profile(cost_data, hw_profile, os_type, region):
    matching_words = hw_profile.split("_")
    meters = []
    if os_type == "windows":
        matching_words.append("windows")

    for row in cost_data:
        # # debugging purpose..
        # if 'Virtual Machines Dv2 Series Windows - D12 v2 - IN Central' in row[2] and '' in hw_profile[1]["name"]:
        #     pdb.set_trace()
        if set(matching_words) == set(row[0].split()) and region == row[-1]:
            meters.append(row)

    return meters


cost_data = read_cost_sheet()


def find_meterids_for_single_profile(hw_profile = "Standard_D1_v2", region="US East", os_type="windows"):
    original_hw_profile = hw_profile

    win_meters = find_meter_info_for_profile(cost_data, hw_profile, os_type, region)
    # if some results not found, then retry using different names..
    if not win_meters and hw_profile in constant.exceptional_profiles:
        new_hw_profile = 'Standard_' + constant.exceptional_profiles[hw_profile]
        win_meters = find_meter_info_for_profile(cost_data, new_hw_profile, os_type, region)

    if len(win_meters)!=1:
        print(original_hw_profile, ">>>>> No unique meter detected..", win_meters)
        # write a row to the csv file
    print("meter for windows:")
    print(original_hw_profile, ": ",win_meters)
    return win_meters



# find_meterids_for_single_profile()