# following mapping has been added based on https://docs.microsoft.com/en-us/azure/virtual-machines/constrained-vcpu
constrained_hw_profile = {'Standard_M8-2ms': 'M8ms', 'Standard_M8-4ms': 'M8ms', 'Standard_M16-4ms': 'M16ms',
              'Standard_M16-8ms': 'M16ms', 'Standard_M32-8ms': 'M32ms', 'Standard_M32-16ms': 'M32ms',
              'Standard_M64-32ms': 'M64ms', 'Standard_M64-16ms': 'M64ms', 'Standard_M128-64ms': 'M128ms',
              'Standard_M128-32ms': 'M128ms', 'Standard_E4-2s_v3': 'E4s_v3', 'Standard_E8-4s_v3': 'E8s_v3',
              'Standard_E8-2s_v3': 'E8s_v3', 'Standard_E16-8s_v3': 'E16s_v3', 'Standard_E16-4s_v3': 'E16s_v3',
              'Standard_E32-16s_v3': 'E32s_v3', 'Standard_E32-8s_v3': 'E32s_v3', 'Standard_E64-32s_v3': 'E64s_v3',
              'Standard_E64-16s_v3': 'E64s_v3', 'Standard_E4-2s_v4': 'E4s_v4', 'Standard_E8-4s_v4': 'E8s_v4',
              'Standard_E8-2s_v4': 'E8s_v4', 'Standard_E16-8s_v4': 'E16s_v4', 'Standard_E16-4s_v4': 'E16s_v4',
              'Standard_E32-16s_v4': 'E32s_v4', 'Standard_E32-8s_v4': 'E32s_v4', 'Standard_E64-32s_v4': 'E64s_v4',
              'Standard_E64-16s_v4': 'E64s_v4', 'Standard_E4-2ds_v4': 'E4ds_v4', 'Standard_E8-4ds_v4': 'E8ds_v4',
              'Standard_E8-2ds_v4': 'E8ds_v4', 'Standard_E16-8ds_v4': 'E16ds_v4', 'Standard_E16-4ds_v4': 'E16ds_v4',
              'Standard_E32-16ds_v4': 'E32ds_v4', 'Standard_E32-8ds_v4': 'E32ds_v4', 'Standard_E64-32ds_v4': 'E64ds_v4',
              'Standard_E64-16ds_v4': 'E64ds_v4', 'Standard_E4-2s_v5': 'E4s_v5', 'Standard_E8-4s_v5': 'E8s_v5',
              'Standard_E8-2s_v5': 'E8s_v5', 'Standard_E16-8s_v5': 'E16s_v5', 'Standard_E16-4s_v5': 'E16s_v5',
              'Standard_E32-16s_v5': 'E32s_v5', 'Standard_E32-8s_v5': 'E32s_v5', 'Standard_E64-32s_v5': 'E64s_v5',
              'Standard_E64-16s_v5': 'E64s_v5', 'Standard_E96-48s_v5': 'E96s_v5', 'Standard_E96-24s_v5': 'E96s_v5',
              'Standard_E4-2ds_v5': 'E4ds_v5', 'Standard_E8-4ds_v5': 'E8ds_v5', 'Standard_E8-2ds_v5': 'E8ds_v5',
              'Standard_E16-8ds_v5': 'E16ds_v5', 'Standard_E16-4ds_v5': 'E16ds_v5', 'Standard_E32-16ds_v5': 'E32ds_v5',
              'Standard_E32-8ds_v5': 'E32ds_v5', 'Standard_E64-32ds_v5': 'E64ds_v5', 'Standard_E64-16ds_v5': 'E64ds_v5',
              'Standard_E96-48ds_v5': 'E96ds_v5', 'Standard_E96-24ds_v5': 'E96ds_v5', 'Standard_E4-2as_v4': 'E4as_v4',
              'Standard_E8-4as_v4': 'E8as_v4', 'Standard_E8-2as_v4': 'E8as_v4', 'Standard_E16-8as_v4': 'E16as_v4',
              'Standard_E16-4as_v4': 'E16as_v4', 'Standard_E32-16as_v4': 'E32as_v4', 'Standard_E32-8as_v4': 'E32as_v4',
              'Standard_E64-32as_v4': 'E64as_v4', 'Standard_E64-16as_v4': 'E64as_v4',
              'Standard_E96-48as_v4': 'E96as_v4', 'Standard_E96-24as_v4': 'E96as_v4', 'Standard_E4-2ads_v5': 'E4ads_v5',
              'Standard_E8-4ads_v5': 'E8ads_v5', 'Standard_E8-2ads_v5': 'E8ads_v5', 'Standard_E16-8ads_v5': 'E16ads_v5',
              'Standard_E16-4ads_v5': 'E16ads_v5', 'Standard_E32-16ads_v5': 'E32ads_v5',
              'Standard_E32-8ads_v5': 'E32ads_v5', 'Standard_E64-32ads_v5': 'E64ads_v5',
              'Standard_E64-16ads_v5': 'E64ads_v5', 'Standard_E96-48ads_v5': 'E96ads_v5',
              'Standard_E96-24ads_v5': 'E96ads_v5', 'Standard_E4-2as_v5': 'E4as_v5', 'Standard_E8-4as_v5': 'E8as_v5',
              'Standard_E8-2as_v5': 'E8as_v5', 'Standard_E16-8as_v5': 'E16as_v5', 'Standard_E16-4as_v5': 'E16as_v5',
              'Standard_E32-16as_v5': 'E32as_v5', 'Standard_E32-8as_v5': 'E32as_v5', 'Standard_E64-32as_v5': 'E64as_v5',
              'Standard_E64-16as_v5': 'E64as_v5', 'Standard_E96-48as_v5': 'E96as_v5',
              'Standard_E96-24as_v5': 'E96as_v5', 'Standard_GS4-8': 'GS4', 'Standard_GS4-4': 'GS4',
              'Standard_GS5-16': 'GS5', 'Standard_GS5-8': 'GS5', 'Standard_DS11-1_v2': 'DS11_v2',
              'Standard_DS12-2_v2': 'DS12_v2', 'Standard_DS12-1_v2': 'DS12_v2', 'Standard_DS13-4_v2': 'DS13_v2',
              'Standard_DS13-2_v2': 'DS13_v2', 'Standard_DS14-8_v2': 'DS14_v2', 'Standard_DS14-4_v2': 'DS14_v2',
              'Standard_M416-208s_v2': 'M416s_v2', 'Standard_M416-208ms_v2': 'M416ms_v2'}


exceptional_profiles = {
    # both win/linux ids did not find for following NV series, so added mapping
    "Standard_NV12s_v2": "NV12",
    "Standard_NV24s_v2": "NV24",
    "Standard_NV6s_v2": "NV6",

    # HB series in eastus region
    "Standard_HB120-16rs_v2": "HB120rs_v2",
    "Standard_HB120-32rs_v2": "HB120rs_v2",
    "Standard_HB120-64rs_v2": "HB120rs_v2",
    "Standard_HB120-96rs_v2": "HB120rs_v2",

    "Standard_HB120-16rs_v3": "HB120rs_v3",
    "Standard_HB120-32rs_v3": "HB120rs_v3",
    "Standard_HB120-64rs_v3": "HB120rs_v3",
    "Standard_HB120-96rs_v3": "HB120rs_v3",


    # linux based ids did not find for following M* series, so added mapping
    "Standard_M64": "M64s",
    "Standard_M64m": "M64ms",
    "Standard_M128m": "M128ms",
    "Standard_M128": "M128s",

}

exceptional_profiles.update(constrained_hw_profile)
