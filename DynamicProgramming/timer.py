from time import perf_counter

class TimeThis:
    
    def __init__(self, section_desc: str) -> None:
        """Provide a title or useful information about what is being timed"""
        self.section_desc = section_desc

    def __enter__(self):
        self.start = perf_counter()
        return self.start

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = perf_counter()
        print(f"It took {self.end - self.start:.6f} seconds to {self.section_desc}")