def day_type_for(key):
    """Determine the dayType."""
    if key == "mon-fri":
        return "MONDAY_TO_FRIDAY"
    if key in ["saturday", "sunday"]:
        return key.upper()
    return None  # nocov
