import ruamel.yaml


def config(path):
    """Load generic YAML loader."""
    yaml = ruamel.yaml.YAML()
    data = open(path).read()
    return yaml.load(data)


def settings():
    """Get the settings data."""
    return config('conf/settings.yaml')


def credentials():
    """Get the credentials data."""
    return config('conf/credentials.yaml')


def schedule():
    """Get the schedule data."""
    return config('conf/schedule.yaml')
