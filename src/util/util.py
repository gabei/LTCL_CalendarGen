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

    # remove timezone info
    time_str = time_str.split(" ")[0]

    hours, minutes, seconds = map(int, time_str.split(":"))

    def hours_are_pm(hours: int) -> bool:
        """Check if the hours are in PM."""
        if not isinstance(hours, int):
            raise ValueError("Hours must be an integer.")
        if not (0 <= hours < 24):
            raise ValueError("Hours must be between [0, 24).")
        return hours >= 12
