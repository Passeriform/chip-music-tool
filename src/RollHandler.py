class Region:
    def __init__(self, x, y, note) -> None:
        self.x: int = x
        self.y: int = y
        self.note: str = note

class RollHandler:
    def __init__(self) -> None:
        self.regions: list[Region] = [Region(i % 128, i // 128, "#000000") for i in range(128 * 32)]
        self.offset: int = 0 # selected tile

    def save(self, filename: str) -> None:
        with open(filename, 'w') as f:
            for region in self.regions:
                f.write(f"{region.x},{region.y},{region.note}\n")