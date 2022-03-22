import SlashDiscord
# token = (token)
# app_id = (app_id)
client = SlashDiscord.Client(token, 0, app_id, log_level=10)

def pong(ctx):
    return "Hey pong!"

pongCommand = SlashDiscord.Command("ping", 1, "pong", handler=pong)
client.push(pongCommand)
client.register()
client.connect()
