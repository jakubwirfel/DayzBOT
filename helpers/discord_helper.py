from discord_webhook import DiscordWebhook

from utils.config import Config


class DiscordHelper:
    @staticmethod
    def send_screen_massage(file: str, message: str) -> None:
        webhook = DiscordWebhook(url=Config.DISCORD_WEBHOOK, username="Stróż Janusz")

        # send two images
        with open(fr"{file}", "rb") as f:
            webhook.add_file(file=f.read(), filename=f'{file}')
            webhook.content = f"{message}"

        webhook.execute()
