from enum import Enum


class _fanspeed_quantity(object):
	def __init__(self, name, pwm):
		self.name = name
		self.pwm = pwm


class fanspeed_quantities(Enum):
	AUTO = _fanspeed_quantity("auto", 0x00)
	SIXTY_PERCENT = _fanspeed_quantity("60 %", hex(60))
	SEVENTY_PERCENT = _fanspeed_quantity("70 %", hex(70))
	EIGHTY_PERCENT = _fanspeed_quantity("80 %", hex(80))
	NINTY_PERCENT = _fanspeed_quantity("90 %", hex(90))
	HUNDRED_PERCENT = _fanspeed_quantity("100 %", hex(100))
