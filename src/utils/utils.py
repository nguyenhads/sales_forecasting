import yaml


def load_config(file_path):
    """Load configuration from a YAML file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            config_data = yaml.safe_load(file)
        return config_data
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error: File '{file_path}' not found.") from e
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error loading YAML file '{file_path}': {e}") from e
