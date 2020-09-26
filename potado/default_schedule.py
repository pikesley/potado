from lib.default_schedule_builder import DefaultScheduleBuilder


def run():
    """Create a default schedule from existing Zones."""
    builder = DefaultScheduleBuilder()
    builder.yamlise()


if __name__ == "__main__":
    run()
