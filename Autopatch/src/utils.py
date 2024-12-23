def escape(input_value):
    """Sanitize input to prevent injection attacks."""
    return input_value.replace("'", "\\'").replace('"', '\\"')
