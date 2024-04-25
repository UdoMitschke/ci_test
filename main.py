import os

import click
import yaml


@click.command()
@click.argument('path')
def read_yaml(path):
    file_path = path + "openapi.yml"
    with open(file_path, 'r') as file:
        try:
            yaml_content = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)
            return
        print(yaml_content)
        print_key_value_pairs(yaml_content)


def print_key_value_pairs(data, prefix=''):
    if not data['info']['active'] == 'true':
        return
    for key, value in data.items():
        if isinstance(value, dict):
            print_key_value_pairs(value, f"{prefix}{key}.")
        else:
            print(f"{prefix}{key}: {value}")


if __name__ == "__main__":
    read_yaml()
    output_file = os.getenv('GITHUB_OUTPUT')
    with open(output_file, "a") as myfile:
        myfile.write(f"TEST={True}")
