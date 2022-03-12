# SlashDiscord
A extreemly simple, straight forward slash command library for discord.

### Why we are here
Since the main discord.py library was archived, we wanted to create a new library
that was built from the ground up for simple slash commands
By building from the ground up, we are able to make an extreemly small, lightweight
library that keeps it simple, stupid.

## Usage
First, define any of your functions
> def ping():
>     return "Hey pong!"

Then, initialize the function as a slash command object
> ping_command = slashReppo.Command("ping", 1, "ping", handler=ping)

Then, start an instantiation of your client with your commands
> _client = slashReppo.Client("your_token", int(your_intents), "your_app_id", commands=[ping_command])  

If you have not registered thse commands
> _client.register()

And finally connect
> _client.connect()
