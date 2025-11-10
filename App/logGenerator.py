import time


class logGenerator:


    def __init__(self):
        self._loopCount = 0


    def inc(self):
        self._loopCount += 1
        return self._loopCount

    def println(self):
        from datetime import datetime
        from datetime import timezone

        utc_now = datetime.now(timezone.utc).isoformat()


        print(f"[{utc_now}] -- {self._loopCount} --")

    def run(self):

        while True:
            self.inc()
            self.println()
            time.sleep(1)
    pass


def main():
    loggerGanerator = logGenerator()
    loggerGanerator.run()
    pass

if __name__ == '__main__':
    main()