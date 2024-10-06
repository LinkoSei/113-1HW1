# 主程式 攝氏轉華氏的函數
def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32

# 單元測試 使用 unittest 模組進行測試
import unittest

class TestTemperatureConversion(unittest.TestCase):
    # 測試正數攝氏轉換
    def test_positive_celsius(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212)  # 100°C = 212°F
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32)     # 0°C = 32°F
        self.assertAlmostEqual(celsius_to_fahrenheit(37), 98.6)  # 37°C ≈ 98.6°F

    # 測試負數攝氏轉換
    def test_negative_celsius(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40)  # -40°C = -40°F
        self.assertAlmostEqual(celsius_to_fahrenheit(-20), -4)   # -20°C = -4°F
        
    # 測試邊界值轉換
    def test_boundary_celsius(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(1), 33.8)   # 1°C ≈ 33.8°F
        self.assertAlmostEqual(celsius_to_fahrenheit(-1), 30.2)  # -1°C ≈ 30.2°F

if __name__ == '__main__':
    unittest.main()
#單元測試是針對程式來進行檢驗的測試工作。