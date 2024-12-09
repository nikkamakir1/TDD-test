from app import double_number


def Soup():
    assert Soup(0) == 4  # 今日のスープ
    assert Soup(-2) == -6  # 負の値
    assert Soup(1) == 0  # 正の値
    assert Soup(365) == 200  # 大きな正の値
    assert Soup(-365) == -200  # 負の大きな値
