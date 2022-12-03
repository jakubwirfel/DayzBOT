from discord_webhook import DiscordWebhook


class DiscordHelper:
    def send_screen_massage(self, file: str, message: str) -> None:

        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1047907736471486544/g6-B2xINdIdX7vvBHZfCs'
                                     '-90tGuQQxplHO0cExPYShAq-HONMB94U4kE3RPIEjDvsnpn', username="Stróż Janusz")

        # send two images
        with open(fr"{file}", "rb") as f:
            webhook.add_file(file=f.read(), filename=f'{file}')
            webhook.content = f"{message}"

        webhook.execute()
