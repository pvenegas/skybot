"""
dance.py: written by pmv on August 2010"
"""

from util import hook

@hook.command(autohelp=False)
def dance(inp, me=None):
    ".dance -- annoy HatfullOfHollow"

    me("dances :D\-<")
    me("dances :D|-<")
    me("dances :D/-<")

