import asyncio
from loguru import logger

from lib.fanspeed_quantities import FanspeedQuantities
from lib.ipmi_command import set_fan_speed
from lib.nvidia_temprature_reader import get_max_gpu_temperature
from lib.logger import initalize_logger

SLEEP_DURATION = 5

async def main():
	initalize_logger()
	
	while True:
		max_gpu_temp = await get_max_gpu_temperature()

		if max_gpu_temp >= 75:
			fanspeed_quantity = FanspeedQuantities.HUNDRED_PERCENT
			await set_fan_speed(fanspeed_quantity)
			logger.info(f"max gpu temp: {max_gpu_temp} - set fan speed to {fanspeed_quantity.value.name}")
		elif max_gpu_temp >= 65:
			fanspeed_quantity = FanspeedQuantities.NINTY_PERCENT
			await set_fan_speed(fanspeed_quantity)
			logger.info(f"max gpu temp: {max_gpu_temp} - set fan speed to {fanspeed_quantity.value.name}")
		elif max_gpu_temp >= 60:
			fanspeed_quantity = FanspeedQuantities.EIGHTY_PERCENT
			await set_fan_speed(fanspeed_quantity)
			logger.info(f"max gpu temp: {max_gpu_temp} - set fan speed to {fanspeed_quantity.value.name}")
		elif max_gpu_temp >= 55:
			fanspeed_quantity = FanspeedQuantities.SEVENTY_PERCENT
			await set_fan_speed(fanspeed_quantity)
			logger.info(f"max gpu temp: {max_gpu_temp} - set fan speed to {fanspeed_quantity.value.name}")
		elif max_gpu_temp >= 50:
			fanspeed_quantity = FanspeedQuantities.SIXTY_PERCENT
			await set_fan_speed(fanspeed_quantity)
			logger.info(f"max gpu temp: {max_gpu_temp} - set fan speed to {fanspeed_quantity.value.name}")
		elif max_gpu_temp >= 45:
			fanspeed_quantity = FanspeedQuantities.FOURTY_PERCENT
			await set_fan_speed(fanspeed_quantity)
			logger.info(f"max gpu temp: {max_gpu_temp} - set fan speed to {fanspeed_quantity.value.name}")
		else:
			fanspeed_quantity = FanspeedQuantities.AUTO
			await set_fan_speed(fanspeed_quantity)
			logger.info(f"max gpu temp: {max_gpu_temp} - set fan speed to {fanspeed_quantity.value.name}")

		await asyncio.sleep(SLEEP_DURATION)

asyncio.run(main())



