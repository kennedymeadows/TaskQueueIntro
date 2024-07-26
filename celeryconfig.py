broker_url = "amqp://guest:guest@192.168.49.2:30072//"
result_backend = "redis://192.168.49.2:30379/0"

task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]
timezone = "America/Los_Angeles"
enable_utc = True
