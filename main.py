import asyncio

from fanspeed_quantities import fanspeed_quantities
from ipmi_command import set_fan_speed
from nvidia_temprature_reader import get_max_gpu_temperature


SLEEP_DURATION = 1


async def main():
	while True:
		max_gpu_temp = await get_max_gpu_temperature()

		if max_gpu_temp >= 75:
			fanspeed_quantity = fanspeed_quantities.HUNDRED_PERCENT
			await set_fan_speed(fanspeed_quantity)
			print(f"max gpu temp: {max_gpu_temp} - set fan speed to {fanspeed_quantity.value.name}")
		elif max_gpu_temp >= 65:
			fanspeed_quantity = fanspeed_quantities.NINTY_PERCENT
			await set_fan_speed(fanspeed_quantity)
			print(f"max gpu temp: {max_gpu_temp} - set fan speed to {fanspeed_quantity.value.name}")
		elif max_gpu_temp >= 60:
			fanspeed_quantity = fanspeed_quantities.EIGHTY_PERCENT
			await set_fan_speed(fanspeed_quantity)
			print(f"max gpu temp: {max_gpu_temp} - set fan speed to {fanspeed_quantity.value.name}")
		elif max_gpu_temp >= 55:
			fanspeed_quantity = fanspeed_quantities.SEVENTY_PERCENT
			await set_fan_speed(fanspeed_quantity)
			print(f"max gpu temp: {max_gpu_temp} - set fan speed to {fanspeed_quantity.value.name}")
		elif max_gpu_temp >= 50:
			fanspeed_quantity = fanspeed_quantities.SIXTY_PERCENT
			await set_fan_speed(fanspeed_quantity)
			print(f"max gpu temp: {max_gpu_temp} - set fan speed to {fanspeed_quantity.value.name}")
		else:
			await set_fan_speed(fanspeed_quantities.AUTO)
			print(f"max gpu temp: {max_gpu_temp} - set fan speed to {fanspeed_quantities.AUTO.value.name}")

		await asyncio.sleep(SLEEP_DURATION)

asyncio.run(main())



