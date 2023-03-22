import yaml
import json


def save_json_file(data, namefile):
    with open(namefile, "w") as txt_file:
        for line in data:
            txt_file.write(" ".join(line))


def merge_yaml_files(files):
    merged_data = {}
    for file in files:
        with open(file, 'r') as stream:
            try:
                data = yaml.safe_load(stream)
                merged_data.update(data)
                json_formatted_str = json.dumps(data, indent=4)
                save_json_file(json_formatted_str, './data/'+(str(file)+'.json'))
            except yaml.YAMLError as exc:
                print(exc)
    return merged_data


def read_json_files(file_json):
    json_data = {}
    json_data2 = {}
    for file in file_json:
        with open(file, 'r') as stream:

            if file == './data/config2.json':
                json_data2 = json.load(stream)
                json_data["martins"].append(json_data2["martins"][0])
                json_formatted_str = json.dumps(json_data, indent=4)

               # Convert dictionary to YAML format
                yaml_str = yaml.dump(json.loads(json_formatted_str))
                print(yaml_str) 
                save_json_file(yaml_str, "./result/config")
                save_json_file(json_formatted_str, "./result/config.json")

            else :
               json_data = json.load(stream)

    return json_data

files = ['config1', 'config2']
file_json = ['./data/config1.json','./data/config2.json']
merge_yaml_files(files)
read_json_files(file_json)
