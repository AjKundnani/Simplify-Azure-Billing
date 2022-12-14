import copy
import pdb

from vsdx import VisioFile

RES_PROPERTIES = {
    "Public IP Address": {
        "type": "Microsoft.Network/publicIPAddresses",
        "region": "location",
        "usagePeriod": "20h",
        "metadata": {
            "sku": "publicIpSku"
        }
    },

    "Load Balancers": {
        "type": "Microsoft.Network/loadBalancer",
        "region": "location",
        "usagePeriod": "20h",
        "metadata": {
            "sku": "LB-type",
            "rules": 20,
            "dataProcessedGB": 6
        }
    },

    "Virtual Machine": {
        "type": "Microsoft.Compute/virtualMachines",
        "region": "US East",
        "usagePeriod": "20h",
        "metadata": {
            "hardwareProfile": "Standard_D1_v2",
            "imageReference": {
                "publisher": "MicrosoftWindowsServer",
                "offer": "WindowsServer",
                "sku": "[parameters('OSVersion')]",
                "version": "latest",
                "storageAccountType": "StandardSSD_LRS"
            },
            "dataDisks": [
                {
                    "diskSizeGB": 1023,
                    "diskId": 0,
                    "storageAccountType": "Empty"
                }
            ]
        }
    }
}



def get_resources_from_visio(visio_file):
    with VisioFile(visio_file) as vis:
        # open first page
        page = vis.pages[0]
        # Page.child_shapes and Page.all_shapes properties
        # page_top_shapes = page.child_shapes  # just those Shapes directly under Page
        # all_shapes_in_page = page.all_shapes  #
        all_shapes = [i.text.strip() for i in page.all_shapes if 'microsoft' in i.tag and i.text]
        res = []
        for shap in all_shapes:
            shape_type = shap.split("-")[0].strip()
            shape_type = shape_type.split("(")[0].strip()
            res_name = shap.split("-")[1].strip()
            if shape_type in RES_PROPERTIES:
                new_res = copy.deepcopy(RES_PROPERTIES[shape_type])
                new_res.update({"name": res_name})
                res.append(new_res)

        print(res)
        return res


# get_resources_from_visio("Drawing.vsdx")