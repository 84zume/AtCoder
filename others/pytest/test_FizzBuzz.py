class FizzBuzz:
    def translate(self, num):
        return (str)(num)


def test_1が入力されたとき文字列の1を出力する():
    # Arrange
    fizzbuzz = FizzBuzz()
    # Act & Assert
    assert "1" == fizzbuzz.translate(1)


def test_2が入力されたとき文字列の2を出力する():
    # Arrange
    fizzbuzz = FizzBuzz()
    # Act & Assert
    assert "2" == fizzbuzz.translate(2)
