import yaml


def read_yaml(file_path):
    with open(file_path, 'r') as file:
        try:
            yaml_content = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)
            return
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
    read_yaml('/Users/udomitschke/private/ci_test/all_folder/f1/openapi.yml')
    print(f'::set-output name=test_report::{True}')
