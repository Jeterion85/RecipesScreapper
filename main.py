from ScrapperStrategies.tasty_scrapper_strategy import TastyScrapperStrategy
from ScrapperContext.scrapper_context import ScrapperContext

STRATEGIES = {"tasty": TastyScrapperStrategy()}


def main():
    context = ScrapperContext()
    for name, strategy in STRATEGIES.items():
        context.set_strategy(strategy)
        try:
            result = context.execute()
            print(f"Results for {name}: {result}")
        except ValueError as e:
            print(f"Error for {name}: {e}")


if __name__ == "__main__":
    main()
