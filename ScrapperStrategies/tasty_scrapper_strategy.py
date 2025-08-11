import requests
import selenium.webdriver
from selenium.webdriver.common.by import By
from ScrapperStrategies.scrapper_strategy import ScrapperStrategy


class TastyScrapperStrategy(ScrapperStrategy):
    def __init__(self):
        super().__init__()
        self._recipes = {}

    def scrape(self, url: str) -> dict[str, list[str]]:
        """Scrape recipes from the Tasty website."""
        with selenium.webdriver.Firefox() as driver:
            # Get all the ingredients
            driver.get(url)
            ingredient_names = [
                ingredient.get_attribute("href").split("/")[-1]
                for ingredient in driver.find_elements(
                    By.XPATH, "//li[@class='grouped-list__item']/a"
                )
            ]
            for ingredient_name in ingredient_names:
                # Get the total recipes for the current ingredient
                total_recipes = int(
                    requests.get(
                        f"https://tasty.co/api/proxy/tasty/feed-page?from=0&size=0&slug={ingredient_name}&type=ingredient"
                    ).json()["count"]
                )
                # Get the recipes for the current ingredient
                recipes = requests.get(
                    f"https://tasty.co/api/proxy/tasty/feed-page?from=0&size={total_recipes}&slug={ingredient_name}&type=ingredient"
                ).json()["items"]
                for recipe in recipes:
                    # Get the recipe's ingredients
                    # TODO: Get the recipe's ingredients from the recipe page
                    driver.get(f"https://tasty.co/recipe/{recipe['slug']}")
                    ingredients = [
                        ingredient.text
                        for ingredient in driver.find_elements(
                            By.XPATH, "//li[@class='ingredient xs-mb1 xs-mt0']"
                        )
                    ]
                    self._recipes[recipe["slug"]] = ingredients
        return self._recipes
