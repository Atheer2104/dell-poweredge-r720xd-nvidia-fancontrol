import subprocess
import asyncio

from loguru import logger

async def get_max_gpu_temperature():
	command = "nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader"
	# result = subprocess.run(shlex.split(command), capture_output=True, text=True)
	proc = await asyncio.create_subprocess_shell(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	stdout, stderr = await proc.communicate()
	stdout, stderr = stdout.decode("utf-8"), stderr.decode("utf-8")

	if stderr:
		logger.error(f"An error has occured when retriving gpu temperature data with the following \n {stderr}")
	else:
		temps = [int(temp) for temp in stdout.split("\n") if temp.strip()]
		return max(temps)
