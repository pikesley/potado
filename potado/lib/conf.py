import yaml


class Conf(dict):
    """Configuration object."""

    def __init__(self):  # pylint: disable=W0231
        """Construct."""
        self.update(yaml.safe_load(open('conf/conf.yaml')))
