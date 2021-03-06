from discord.ext import commands
import sys
import traceback
class ErrorHandler(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if hasattr(ctx.command, "on_error"):
            return 

        error = getattr(error, "original", error)

        if isinstance(error, commands.CommandError):
            await ctx.send(f'Beep Beep! There is a problem with __**{ctx.message.content}**__')

        if isinstance(error, commands.CommandNotFound):
            return await ctx.send(
                f'\t↓↓ Command error ↓↓ ```fix\n{str(error)} ¯\_(ツ)_/¯\n```')

        if isinstance(error, commands.UserInputError):
            await ctx.send('Beep Beep! Your input is wrong ¯\_(ツ)_/¯ ')

        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
        


