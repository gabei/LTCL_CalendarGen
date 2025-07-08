import pytest
from util.util import format_time


class TestFormatTime:
    def test_format_time_AM(self):
        """Test for AM times. Seconds are ignored."""
        assert format_time("11:30:13 -0500") == "11:30am"
        assert format_time("00:30:86 -0500") == "12:30am"
        assert format_time("09:46:24 -0500") == "9:46am"
        assert format_time("10:00:59 -0500") == "10:00am"
        assert format_time("3:33:33 -0500") == "3:33am"

    def test_format_time_PM(self):
        """Test for PM times. Seconds are ignored."""
        assert format_time("14:30:12 -0500") == "2:30pm"
        assert format_time("15:45:23 -0500") == "3:45pm"
        assert format_time("23:59:59 -0500") == "11:59pm"
        assert format_time("12:00:34 -0500") == "12:00pm"
        assert format_time("20:15:57 -0500") == "8:15pm"

    def test_format_time_empty(self):
        with pytest.raises(ValueError, match="Times cannot be empty strings."):
            format_time("")

    def test_format_time_invalid_type(self):
        with pytest.raises(ValueError, match="Time must be a string."):
            format_time(12345)
