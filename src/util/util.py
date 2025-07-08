from datetime import date


def format_time(time_str: str) -> str:
    """
    Format time string from 24hr to AM/PM.

      Parameters:
        time_str {str} —— The time string in 24-hour format (e.g., "14:30:00 -0500").

      Raises:
        ValueError if time_str is not a string or is empty.

      Returns:
        formatted_time {str} —— Formatted  time string in AM/PM format (e.g., "2:30pm").
    """

    if not isinstance(time_str, str):
        raise ValueError("Time must be a string.")

    time_str = time_str.strip()
    if not time_str:
        raise ValueError("Times cannot be empty strings.")

    # remove timezone, eval HH:MM:SS
    time_str = time_str.split(" ")[0]
    hours, minutes, seconds = time_str.split(":")

    int_hours = int(hours)
    if int_hours == 0:
        hours = "12"
    elif int_hours > 12:
        hours = str(int_hours - 12)
    else:
        hours = str(int_hours)

    formatted_time = f"{hours}:{minutes}" + ("am" if int_hours < 12 else "pm")
    return formatted_time
