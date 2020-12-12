# AMOUNT_LIMITS_CONFIG can have an unlimited number of key:value.
# AMOUNT_LIMITS_CONFIG must be a dict. The key is seconds and the value is limit. {seconds: limit}
# Key and value must be an integer. {60: 3000}
# Checking runs from left to right.
AMOUNT_LIMITS_CONFIG: dict = {10: 1000, 60: 3000, 3600: 20000}
