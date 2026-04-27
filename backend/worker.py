import redis
from rq import Worker, Queue
from app.workers.tasks import process_prompt

redis_conn = redis.Redis(host="redis", port=6379)  # ✅ FIXED

if __name__ == "__main__":
    queue = Queue(connection=redis_conn)
    worker = Worker([queue], connection=redis_conn)
    worker.work()