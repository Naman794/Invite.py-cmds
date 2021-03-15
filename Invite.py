import discord

client = discord.Client(command_prefix = ' ', case_insensetive = True)

@client.command(name='Invite')
async def Invite(ctx):
    embed=discord.Embed(title = "header", color = 0x0000FF)
    """for creating hyperlinks just define the text along with bot invite link
    this will create the link turn blue in color which means if someone taps on the highlighted word,
    then they will redirected to the particular inviting webpage
    """
    embed.add_field(name='text', value='**[text](bot invite link)**', inline = False)
    await ctx.reply(embed=embed)
    #embed can be added more to make it fancy!
    #depends upon your vision 
