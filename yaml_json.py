#!/usr/bin/env python

import yaml
import json

def main():

    yaml_file = 'yaml_json.yml'
    json_file = 'yaml_json.json'

    my_list = ['this is a list']
    my_list.append('hey')
    my_list.append('python')
    my_list.append('go')
    my_list.append({})
    my_list[-1]
    my_list[-1]['ip.addr'] = '192.168.1.1'
    my_list[-1]['phone'] = '7027675309'

    with open(yaml_file, "w") as f:
        f.write(yaml.dump(my_list, default_flow_style=False))

    with open(json_file, "w") as y:
        json.dump(my_list, y)

if __name__ == "__main__":
    main()
