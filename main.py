from ScrapperStrategies.tasty_scrapper_strategy import TastyScrapperStrategy
from ScrapperStrategies.matthewryle_scrapper_strategy import MatthewRyleScrapperStrategy
from ScrapperContext.scrapper_context import ScrapperContext

STRATEGIES = {
    "tasty": ["https://tasty.co/ingredient", TastyScrapperStrategy()],
    "matthewryle": ["https://matthewryle.com/recipes", MatthewRyleScrapperStrategy()],
}


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
