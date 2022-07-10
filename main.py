import discord
from discord.ui import Button, View, Select
#SECRET CONTAINING YOUR TOKEN in form of token="token"
import secret
import asyncio

#Basic stuff if you want to use Intenets and setups your tree 
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)
guild_id = "ID GOES HERE"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await tree.sync(guild = discord.Object(id = guild_id))

#The shop command
@tree.command(
    guild = discord.Object(id = guild_id), 
    name = "shop", 
    description = "A Shop For Buying Roles", 
)
async def slash(interaction: discord.Interaction):
    #Gets the discord ID of the person that ran the command
    discord_id = str(interaction.user)
    
    #The View that the user can interact with

    #Shop Options
    options = Select(placeholder="Roles",max_values= 1,options=[
        discord.SelectOption(
            label="Role 1",
            value= "Role_1"
        ),
        discord.SelectOption(
            label="Role 2",
            value= "Role_2"
        )
    ])

    #Back Button
    back = Button(label="Leave", style=discord.ButtonStyle.red)

    #The Callbacks for the view, this is where main code is ran on what they chose
    #Options
    async def shop_callback(interaction):
        #Checks to see who clicked so other people can use on other peoples shop
        if str(interaction.user) == discord_id:
            #Gets what the user chosed from the options
            choice = options.values[0]

            #Do somthing here with the choice ---MAIN CODE GOES HERE---
            print(choice)
            embed = discord.Embed(title="Cloutziie Role Shop",description="Allright you have bought: "+choice)
            view.remove_item(options)
            view.remove_item(back)
            await interaction.response.edit_message(embed=embed,view=view)
            await asyncio.sleep(5)
            #await interaction.message.delete()

    #Back Button
    async def button_back(interaction):
        #Checks to see who clicked so other people can use on other peoples shop
        if str(interaction.user) == discord_id:
            view.remove_item(options)
            view.remove_item(back)
            embed = discord.Embed(title="Cloutziie Role Shop",description="Allright Later.")
            await interaction.response.edit_message(embed=embed,view=view)
            await asyncio.sleep(5)
            await interaction.message.delete()
    #Shop View
    #Creates the View
    view = View()

    #Adds the options and back button to the view
    view.add_item(options)
    view.add_item(back)

    #Sets the callback for the view
    options.callback = shop_callback
    back.callback = button_back

    #Displays it all for the user
    embed = discord.Embed(title="Cloutziie Role Shop", description="Looking to buy some roles", color=0x00ff00)
    await interaction.response.send_message(embed=embed,view=view)


client.run(secret.token)
