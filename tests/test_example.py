import pytest # pytest imported and bound locally

with pytest.raises(ZeroDivisionError) as exeption:
    8/0

assert str(exeption.value) == "division by zero"