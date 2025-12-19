import threading
import queue
import pickle
import gzip
import os

class AsyncPersistence:
    def __init__(self, path):
        self.path = path
        self.queue = queue.Queue(maxsize=1)
        self.stop_event = threading.Event()
        self.thread = threading.Thread(
            target=self._worker, daemon=True
        )
        self.thread.start()

    def request_save(self, data):
        if self.queue.full():
            try:
                self.queue.get_nowait()
            except queue.Empty:
                pass
        try:
            self.queue.put_nowait(data)
        except queue.Full:
            pass

    def _worker(self):
        while not self.stop_event.is_set():
            try:
                data = self.queue.get(timeout=0.2)
            except queue.Empty:
                continue
            try:
                raw = pickle.dumps(data, protocol=pickle.HIGHEST_PROTOCOL)
                compressed = gzip.compress(raw)
                tmp = self.path + ".tmp"
                with open(tmp, "wb") as f:
                    f.write(compressed)
                os.replace(tmp, self.path)
            except Exception:
                pass

    def load(self, default):
        if not os.path.exists(self.path):
            return default
        with open(self.path, "rb") as f:
            compressed = f.read()
        raw = gzip.decompress(compressed)
        return pickle.loads(raw)

    def close(self):
        self.stop_event.set()
        self.thread.join(timeout=1)
