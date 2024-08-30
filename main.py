import discord
from discord.ext import commands
from discord import app_commands
from operation import MathService
from fromStr import large_num

NumberFormat = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@NumberFormat.event
async def on_ready():
    print(f"Logged in as {NumberFormat.user.name}")
    try:
        sync = await NumberFormat.tree.sync()
        print(f"Synced command(s): {len(sync)}")
    except Exception as e:
        print(f"Error syncing commands: {e}")

@NumberFormat.tree.command(name="add", description="Add 2 values")
@app_commands.describe(value1="Number", value2="Number")
async def add(interaction: discord.Interaction, value1: str, value2: str):
    try:
        num1 = MathService.to_float(value1)
        num2 = MathService.to_float(value2)
    except ValueError:
        await interaction.response.send_message("Invalid input. Please provide valid numbers.")
        return

    from_larg = large_num()
    result = MathService.add(num1, num2)
    toStr = from_larg.toStr(result)
    
    new_title = "Result from adding value1 + value2"
    embed = discord.Embed(
        title=new_title,
        description=f"{value1} + {value2} = {result}",
        color=discord.Color.red()
    )
    embed.add_field(name="Result", value=result, inline=False)
    embed.add_field(name="To Short", value=toStr, inline=False)
    
    await interaction.response.send_message(embed=embed)

NumberFormat.run()
