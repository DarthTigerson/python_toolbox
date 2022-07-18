from function_os import os_clear_screen, os_delay, os_get_date_time

os_clear_screen('Hello world!')
os_delay(2)
print(f'Today is the {os_get_date_time("%d%m%Y")}')