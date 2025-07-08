import pytest
from util.util import util


class TestFormatTime:
    def test_format_time_empty(self):
        with pytest.raises(ValueError, match="Times cannot be empty strings."):
            util.format_time("")

    def test_format_time_invalid_type(self):
        with pytest.raises(ValueError, match="Time must be a string."):
            util.format_time(12345)
