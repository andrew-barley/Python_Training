#!/usr/bin/env python

import yaml
import json
from pprint import pprint

def main():
    #import yaml file
    with open("yaml_json.yml") as y:
        yaml_print = yaml.load(y)

    #load json file
    with open("yaml_json.json") as j:
        json_print = json.load(j)

    pprint(yaml_print)
    pprint(json_print)

if __name__ =="__main__":
    main()
