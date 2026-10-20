from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1561683410668355655/2HEwtemIL7iWFf4DOik_43LpPX5pnkdSf6hg93iIiSixMpqqiae1YjL68MJJgaNCIi-b", content="HI")

webhook.execute()