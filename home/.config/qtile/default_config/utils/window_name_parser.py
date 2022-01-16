def parse_window_name(window_name: str):
    if "Mozilla Firefox" in window_name:
        return "Mozilla Firefox"

    return window_name.split("-")[-1].strip()
