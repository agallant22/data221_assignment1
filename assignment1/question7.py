# Time Conversion Fucnction

def convert_seconds(seconds):
    if seconds < 0 or seconds > 86399:
        return "Invalid input: seconds must be between 0 and 86399."

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    # Determine AM or PM
    am_pm = "AM" if hours < 12 else "PM"

    # Convert to 12-hour format
    hours_12 = hours % 12
    if hours_12 == 0:
        hours_12 = 12

    return f"{hours_12:02}:{minutes:02}:{secs:02} {am_pm}"

print(convert_seconds(30))