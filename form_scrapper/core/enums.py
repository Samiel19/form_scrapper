class Regex:
    """Regex data"""

    PHONE_PATTERN = r'(\+7).(\d{3}).(\d{3}).(\d{2}).(\d{2})'
    EMAIL_PATTERN = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
    DATE_PATTERN_DOT = r'^(0?[1-9]|[12][0-9]|3[01])[\.](0?[1-9]|1[012])[\.]\d{4}$'
    DATE_PATTERN_DASH = r'^\d{4}[-](0?[1-9]|1[012])[-](0?[1-9]|[12][0-9]|3[01])$'
