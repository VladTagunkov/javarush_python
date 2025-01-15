from plyer import notification


notification.notify(
    title = "Remonder!",
    message = "Не забудьте о встрече в 15:00 сегодня",
    app_name = 'reminder',
    timeout = 1
)