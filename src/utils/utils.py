import yaml


def load_config(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{file_path} not found.")
    except yaml.YAMLError as e:
        raise yaml.YAMLError()