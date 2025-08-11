from ScrapperStrategies.tasty_scrapper_strategy import TastyScrapperStrategy
from ScrapperContext.scrapper_context import ScrapperContext

STRATEGIES = {
    "tasty": ["https://tasty.co/ingredient", TastyScrapperStrategy()],
}


def main():
    context = ScrapperContext()
    for name, (url, strategy) in STRATEGIES.items():
        context.set_strategy(strategy)
        try:
            result = context.execute(url)
            print(f"Results for {name}: {result}")
        except ValueError as e:
            print(f"Error for {name}: {e}")


if __name__ == "__main__":
    main()
