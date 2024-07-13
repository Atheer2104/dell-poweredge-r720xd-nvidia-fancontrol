from enum import Enum

class _fanspeed_quantity(object):
	def __init__(self, name, pwm):
		self.name = name
		self.pwm = pwm


class FanspeedQuantities(Enum):
	AUTO = _fanspeed_quantity("auto", 0x00)
	FOURTY_PERCENT = _fanspeed_quantity("40 %", hex(40)) 
	FIVTY_PERCENT = _fanspeed_quantity("50 %", hex(50)) 
	SIXTY_PERCENT = _fanspeed_quantity("60 %", hex(60))
	SEVENTY_PERCENT = _fanspeed_quantity("70 %", hex(70))
	EIGHTY_PERCENT = _fanspeed_quantity("80 %", hex(80))
	NINTY_PERCENT = _fanspeed_quantity("90 %", hex(90))
	HUNDRED_PERCENT = _fanspeed_quantity("100 %", hex(100))
