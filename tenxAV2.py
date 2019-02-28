import json

with open('data.json') as f:
    data = json.load(f)

json_output = dict()
def abc(json_input, lookup_key):
    if isinstance(json_input, dict):
        for k, v in json_input.iteritems():
            if k == lookup_key:
                yield v
            else:
                for child_val in abc(v, lookup_key):
                    yield child_val
    elif isinstance(json_input, list):
        for item in json_input:
            for item_val in abc(item, lookup_key):
                yield item_val

quantity_23 = []
quantity_50 = []
quantity_260 = []
for item in abc(data['data']['100gm'], "quantity"):
    quantity_23.append(23*item/100)
    quantity_50.append(50*item/100)
    quantity_260.append(260*item/100)



