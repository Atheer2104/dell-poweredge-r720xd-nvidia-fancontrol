import subprocess
import shlex

def get_max_gpu_temperature():
	command = "nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader"
	result = subprocess.run(shlex.split(command), capture_output=True, text=True)

	if result.stderr:
		print(f"An error has occured when retriving gpu temperature data with the following \n {result.stderr}")
	else:
		output = result.stdout
		temps = [int(temp) for temp in output.split("\n") if temp.strip()]
		# print(temps)
		return max(temps)
