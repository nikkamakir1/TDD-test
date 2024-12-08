from app import double_number


def test_double_number():
    assert double_number(2) == 4  # 正常ケース
    assert double_number(-3) == -6  # 負の値
    assert double_number(0) == 0  # ゼロ
    assert double_number(100) == 200  # 大きな数
    assert double_number(-100) == -200  # 負の大きな数
