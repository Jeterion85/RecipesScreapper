from ScrapperStrategies.scrapper_strategy import ScrapperStrategy


class ScrapperContext:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy: ScrapperStrategy) -> None:
        """Set the scraping strategy."""
        self.strategy = strategy

    def execute(self) -> dict[str, list[str]]:
        """Execute the scraping strategy."""
        if not self.strategy:
            raise ValueError("Scraping strategy is not set.")
        return self.strategy.scrape()
