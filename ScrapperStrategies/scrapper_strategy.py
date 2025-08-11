from abc import ABC, abstractmethod


class ScrapperStrategy(ABC):
    """Abstract base class for scrapper strategies"""

    @abstractmethod
    def scrape(self, url: str) -> dict[str, list[str]]:
        """Abstract method to scrape recipes from a given URL."""
        pass
