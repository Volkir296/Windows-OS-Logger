import os
import subprocess
import time

# Создание пути к рабочему столу
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
log_file_path = os.path.join(desktop_path, "dxdiag_log.txt")

# Запуск dxdiag c параметром сохронения лога
subprocess.run(["dxdiag", "/t", log_file_path])

# Создание делея в 2 секунды, дабы убедиться, что файл создан
time.sleep(2)

# Проверочка, был ли создан лог
if os.path.exists(log_file_path):
    print(f"Лог сохранён на рабочем столе:  {log_file_path}")
else:
    print("Не удалось сохранить лог dxdiag")