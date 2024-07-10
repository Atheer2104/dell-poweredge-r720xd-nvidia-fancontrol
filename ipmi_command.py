import subprocess
import asyncio

from fanspeed_quantities import fanspeed_quantities


# -------------------- IPMI CONFIGURATIONS ----------------------------
IPMIHOST = "192.168.68.109"
IPMIUSER = "root"
IPMIPASSWORD = "xxxx"
IPMIKEY = "0000000000000000000000000000000000000000"

last_fanspeed_quantity_name = None

async def set_fan_speed(fanspeed_quantity: fanspeed_quantities):
	global last_fanspeed_quantity_name
	match fanspeed_quantity.value.name:
		case fanspeed_quantities.AUTO.value.name:
			command = f"ipmitool -I lanplus -H {IPMIHOST} -U {IPMIUSER} -P {IPMIPASSWORD} -y {IPMIKEY} raw 0x30 0x30 0x01 0x01"
			proc = await asyncio.create_subprocess_shell(command, stderr=subprocess.PIPE)

			_, stderr = await proc.communicate()
			stderr = stderr.decode("utf-8")

			if stderr:
				print(
					f'An error has occured when setting fan speed to "{fanspeed_quantity.value.name}" with the following message \n {stderr}'
				)

			if last_fanspeed_quantity_name != fanspeed_quantities.AUTO.value.name:
				last_fanspeed_quantity_name = fanspeed_quantities.AUTO.value.name
				print("set last speed to auto")

		case _:
			if last_fanspeed_quantity_name != fanspeed_quantity.value.name:
				last_fanspeed_quantity_name = fanspeed_quantity.value.name
				print(f"set last speed to {last_fanspeed_quantity_name}")

				# setting manual control
				command = f"ipmitool -I lanplus -H {IPMIHOST} -U {IPMIUSER} -P {IPMIPASSWORD} -y {IPMIKEY} raw 0x30 0x30 0x01 0x00"
    
				proc = await asyncio.create_subprocess_shell(command, stderr=subprocess.PIPE)
				_, stderr = await proc.communicate()

				print("setting manual control")
				if stderr:
					print(
						f"An error has occured when enabling manual fanspeed (required) to set custom pwm value with the following message \n {stderr}"
					)

			pwm = fanspeed_quantity.value.pwm
			command = f"ipmitool -I lanplus -H {IPMIHOST} -U {IPMIUSER} -P {IPMIPASSWORD} -y {IPMIKEY} raw 0x30 0x30 0x02 0xff {pwm}"

			proc = await asyncio.create_subprocess_shell(command, stderr=subprocess.PIPE)
			_, stderr = await proc.communicate()

			if stderr:
				print(
					f'An error has occured when setting fan speed to "{fanspeed_quantity.value.name}" with the following message \n {stderr}'
				)
