import socket  # Импорт модуля для работы с сетевыми соединениями

# -----------------------------------------------------------------------------
# 1. Создание TCP-сокета
# -----------------------------------------------------------------------------
# Создаем TCP-сокет для установления соединения с сервером.
# По умолчанию используется IPv4 (AF_INET) и протокол TCP (SOCK_STREAM),
# который гарантирует надежную доставку данных.
sock = socket.socket()

# -----------------------------------------------------------------------------
# 2. Настройка режима работы сокета
# -----------------------------------------------------------------------------
# Устанавливаем сокет в блокирующий режим (значение 1).
# Это означает, что операции (например, connect, send, recv) будут ожидать завершения,
# прежде чем продолжить выполнение программы.
sock.setblocking(1)

# -----------------------------------------------------------------------------
# 3. Установление соединения с сервером
# -----------------------------------------------------------------------------
# Выводим служебное сообщение о попытке соединения с сервером.
print("КЛИЕНТ: Попытка соединения с сервером на адресе localhost:9090...")
# Метод connect инициирует соединение с сервером, работающим на localhost на порту 9090.
sock.connect(('localhost', 9090))
# После успешного соединения выводим сообщение об установлении соединения.
print("КЛИЕНТ: Соединение с сервером установлено.")

# -----------------------------------------------------------------------------
# 4. Считывание строки со стандартного ввода
# -----------------------------------------------------------------------------
# Функция input() ожидает ввода от пользователя, выводя приглашение на экран.
# Введенная строка будет отправлена на сервер.
msg = input("Введите строку для отправки серверу: ")

# -----------------------------------------------------------------------------
# 5. Отправка данных на сервер
# -----------------------------------------------------------------------------
# Выводим сообщение о начале отправки данных.
print("КЛИЕНТ: Отправка данных серверу...")
# Преобразуем строку в байты с помощью метода encode() и отправляем их серверу.
sock.send(msg.encode())
print("КЛИЕНТ: Данные успешно отправлены серверу.")

# -----------------------------------------------------------------------------
# 6. Получение данных от сервера
# -----------------------------------------------------------------------------
# Выводим сообщение о том, что клиент ожидает ответ от сервера.
print("КЛИЕНТ: Ожидание ответа от сервера...")
# Метод recv() получает данные (до 1024 байт) от сервера.
data = sock.recv(1024)
# После получения данных выводим служебное сообщение.
print("КЛИЕНТ: Данные получены от сервера.")

# -----------------------------------------------------------------------------
# 7. Разрыв соединения с сервером
# -----------------------------------------------------------------------------
# Закрываем сокет для освобождения ресурсов и вывода сообщения о разрыве соединения.
sock.close()
print("КЛИЕНТ: Соединение с сервером закрыто.")

# -----------------------------------------------------------------------------
# 8. Вывод полученного ответа
# -----------------------------------------------------------------------------
# Декодируем полученные байты обратно в строку и выводим ответ сервера на экран.
print("Ответ от сервера:", data.decode())
