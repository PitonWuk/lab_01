"""
Завдання 1
Розроблення програми з таймером, що підраховує
час. Використати JSON для збереження стану таймера
(наприклад, поточний час) у файлі. При перезапуску
програми відновити час збереженого стану за
допомогою завантаження даних з JSON-файлу.

"""
import json
import time

timer_file = "timer_state.json"

def save_timer_state(timer):
    state = {"start_time": timer["start_time"], "elapsed_time": timer["elapsed_time"]}
    with open(timer_file, "w") as file:
        json.dump(state, file)

def load_timer_state():
    try:
        with open(timer_file, "r") as file:
            state = json.load(file)
        return state
    except FileNotFoundError:
        return None

def start_timer():
    timer = {"start_time": time.time(), "elapsed_time": 0}
    while True:
        try:
            user_input = input("Enter 'stop' to stop the timer: ")
            if user_input.lower() == "stop":
                break
        except KeyboardInterrupt:
            break

        current_time = time.time()
        timer["elapsed_time"] = current_time - timer["start_time"]
        print(f"Time: {timer['elapsed_time']:.2f} seconds")

        save_timer_state(timer)

    print("Timer is stopped.")
    return timer

def common_time():
    saved_state = load_timer_state()

    if saved_state:
        user_choice = input("Was detected saved timer. Restore (y/n)? ").lower()
        if user_choice == "y":
            start_time = saved_state["start_time"]
            elapsed_time = saved_state["elapsed_time"]
            timer = {"start_time": start_time, "elapsed_time": elapsed_time}
        else:
            timer = start_timer()
    else:
        timer = start_timer()

    print(f"Common time of timer: {timer['elapsed_time']:.2f} seconds")

common_time()

