import pyautogui as pag
import time
import subprocess

username = "rameshkumar.mahato@entegrasources.com.np"
password = "Ramesh@9813"
timetrako_path = 'F:\\other program\\timetrako\\ssd ins\\Timetracko.exe'
initial_waiting_time = 2
move_time = 1
first_page_x_cor = 540
un_y = 308  # username y-coordinate
pw_y = 405  # password y-coordinate
si_y = 510  # sign in y-coordinate
sp_y = 605  # second page y-coordinate
ci_y = 267  # clock-in y-coordinate


def move_click(x, y, moving_time):
    pag.moveTo(x, y, moving_time)
    pag.click(x, y)


def move_click_write(x, y, moving_time, text):
    move_click(x, y, moving_time)
    pag.write(text, interval=0.1)


def move_click_sleep(x, y, moving_time, sleep_time):
    move_click(x, y, moving_time)
    pag.sleep(sleep_time)


def time_counter(x):
    for i in range(x):
        print("waited  time= 00:00:0" + str(i + 1) + "sec")
        time.sleep(1)


print(f"I am waiting upto {initial_waiting_time} second  to proceed the further operation, keep patience")
time_counter(initial_waiting_time)
print("Ok i am openning timetrako application.....")

subprocess.Popen(timetrako_path)
time.sleep(5)
print("Your app is opened!")

# move  the cursor for entering the username
move_click_write(first_page_x_cor, un_y, move_time, username)

# move for entering password
move_click_write(first_page_x_cor, pw_y, move_time, password)

# clicking the login bottom
move_click_sleep(first_page_x_cor, si_y, move_time, 1)

# after that process further
move_click_sleep(first_page_x_cor, sp_y, move_time, 1)

# clicking the clocking bottom
move_click_sleep(first_page_x_cor, ci_y, move_time, 1)
