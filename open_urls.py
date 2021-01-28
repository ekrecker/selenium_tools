import sys
import fileinput
from pathlib import Path
from selenium import webdriver


if Path(sys.argv[1]).exists():
	count = 0
	driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe")
	for line in fileinput.input():
		print(line)

		driver.get(line)
		count += 1
		driver.execute_script("window.open()")
		driver.switch_to.window(driver.window_handles[count])

	for i in range(count):
		driver.switch_to.window(driver.window_handles[i])
		driver.refresh()

else:
	print("ARG Error !!!\nplease specify files")
	exit(1)
