import yaml

def load_yaml_as_dict(file_path: str) -> dict:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)