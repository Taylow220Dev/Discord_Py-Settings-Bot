import discord
from discord.ext import commands
from discord import app_commands
from operation import MathService
from fromStr import large_num

intent = discord.Intents.all()
intent.message_content = True
NumberFormat = commands.Bot(command_prefix="/", intents=intent)

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

@NumberFormat.tree.command(name="sub", description="Sub 2 values")
@app_commands.describe(value1="Number", value2="Number")
async def sub(interaction: discord.Interaction, value1: str, value2: str):
    try:
        num1 = MathService.to_float(value1)
        num2 = MathService.to_float(value2)
    except ValueError:
        await interaction.response.send_message("Invalid input. Please provide valid numbers.")
        return

    from_larg = large_num()
    result = MathService.sub(num1, num2)
    toStr = from_larg.toStr(result)
    
    new_title = "Result from sub value1 - value2"
    embed = discord.Embed(
        title=new_title,
        description=f"{value1} - {value2} = {result}",
        color=discord.Color.red()
    )
    embed.add_field(name="Result", value=result, inline=False)
    embed.add_field(name="To Short", value=toStr, inline=False)
    
    await interaction.response.send_message(embed=embed)

@NumberFormat.tree.command(name="div", description="Add 2 values")
@app_commands.describe(value1="Number", value2="Number")
async def div(interaction: discord.Interaction, value1: str, value2: str):
    try:
        num1 = MathService.to_float(value1)
        num2 = MathService.to_float(value2)
    except ValueError:
        await interaction.response.send_message("Invalid input. Please provide valid numbers.")
        return

    from_larg = large_num()
    result = MathService.div(num1, num2)
    toStr = from_larg.toStr(result)
    
    new_title = "Result from dividing value1 / value2"
    embed = discord.Embed(
        title=new_title,
        description=f"{value1} / {value2} = {result}",
        color=discord.Color.red()
    )
    embed.add_field(name="Result", value=result, inline=False)
    embed.add_field(name="To Short", value=toStr, inline=False)
    
    await interaction.response.send_message(embed=embed)

@NumberFormat.tree.command(name="mul", description="mul 2 values")
@app_commands.describe(value1="Number", value2="Number")
async def mul(interaction: discord.Interaction, value1: str, value2: str):
    try:
        num1 = MathService.to_float(value1)
        num2 = MathService.to_float(value2)
    except ValueError:
        await interaction.response.send_message("Invalid input. Please provide valid numbers.")
        return

    from_larg = large_num()
    result = MathService.mul(num1, num2)
    toStr = from_larg.toStr(result)
    
    new_title = "Result from multiply value1 * value2"
    embed = discord.Embed(
        title=new_title,
        description=f"{value1} * {value2} = {result}",
        color=discord.Color.red()
    )
    embed.add_field(name="Result", value=result, inline=False)
    embed.add_field(name="To Short", value=toStr, inline=False)
    
    await interaction.response.send_message(embed=embed)

@NumberFormat.tree.command(name="log", description="log 2 values")
@app_commands.describe(value1="Number", value2="Number")
async def log(interaction: discord.Interaction, value1: str, value2: str):
    try:
        num1 = MathService.to_float(value1)
        num2 = MathService.to_float(value2)
    except ValueError:
        await interaction.response.send_message("Invalid input. Please provide valid numbers.")
        return

    from_larg = large_num()
    result = MathService.log(num1, num2)
    toStr = from_larg.toStr(result)
    
    new_title = f"Result from log(value1, value2)"
    embed = discord.Embed(
        title=new_title,
        description=f"log({num1}, {num2}) = {result}",
        color=discord.Color.red()
    )
    embed.add_field(name="Result", value=result, inline=False)
    embed.add_field(name="To Short", value=toStr, inline=False)
    
    await interaction.response.send_message(embed=embed)

@NumberFormat.tree.command(name="short", description="for Example 1000 to 1k")
@app_commands.describe(value1="Number")
async def short(interaction: discord.Interaction, value1: str):
    try:
        num1 = MathService.to_float(value1)
    except ValueError:
        await interaction.response.send_message("Invalid input. Please provide valid numbers.")
        return

    from_larg = large_num()
    toStr = from_larg.toStr(num1)
    
    new_title = f"Short"
    embed = discord.Embed(
        title=new_title,
        description=f"{toStr}",
        color=discord.Color.red()
        )
    embed.add_field(name="Original Value", value=num1, inline=False)
    
    await interaction.response.send_message(embed=embed)

    
@NumberFormat.tree.command(name="pow", description="Power of ex. 10^3")
@app_commands.describe(value1="Number", value2="Number")
async def short(interaction: discord.Interaction, value1: str, value2: str):
    try:
        num1 = MathService.to_float(value1)
        num2 = MathService.to_float(value2)
    except ValueError:
        await interaction.response.send_message("Invalid input. Please provide valid numbers.")
        return

    from_larg = large_num()
    result = MathService.pow(num1, num2)
    toStr = from_larg.toStr(result)
    
    new_title = f"Pow"
    embed = discord.Embed(
        title=new_title,
        description=f"{toStr}",
        color=discord.Color.red()
        )
    embed.add_field(name="Original Value", value=f"{num1}^{num2}={result}", inline=False)
    
    await interaction.response.send_message(embed=embed)

@NumberFormat.tree.command(name="help", description="To Help figure out where i put my dinner at")
async def help(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Help find the commands",
        description="must use `/` before using a command",
        color=discord.Color.orange()
    )
    embed.add_field(
        name="add",
        value="Add 2 Values",
        inline=True
    )
    embed.add_field(
        name="div",
        value="Div 2 values",
        inline=True
    )
    embed.add_field(
        name="log",
        value="log(value1, value2)",
        inline=True
    )
    embed.add_field(
        name="mul",
        value="Mul 2 values",
        inline=True
    )
    embed.add_field(
        name="short",
        value="short ex. 1000 to 1k",
        inline=True
    )
    embed.add_field(
        name="sub",
        value="Sub 2 values",
        inline=True
    )
    embed.add_field(
        name="pow",
        value="Pow value1^value2",
        inline=True
    )
    await interaction.response.send_message(embed=embed)

NumberFormat.run()