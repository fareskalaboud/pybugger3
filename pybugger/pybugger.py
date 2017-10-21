import random
from pybugger import myaixterm

color = myaixterm

color.aix_init()

def string_constructor(args, foreground="normal", background="normal"):
    if foreground != "rainbow":
        foreground = "" if foreground == "normal" else color.aix_fg(foreground)
        background = "" if background == "normal" else color.aix_bg(background)

        res = foreground + background

        for arg in args:
            res += arg

        res = res + color.aix_normal()

        return res
    else:
        colors = color.get_all_colors()
        res = ""

        for arg in args:
            res += arg

        rainbow_string = ""

        for character in list(res):
            foreground = color.aix_bg(colors[getRandomKey(colors)])
            background = color.aix_fg(colors[getRandomKey(colors)])
            rainbow_string += foreground + background + character

        rainbow_string += color.aix_normal()

        return rainbow_string

def getRandomKey(dictionary):
    return random.sample(list(dictionary), 1).pop()

def default(*args):
    """Format the arguments with a default forgreound and background."""
    print(string_constructor(args))

def success(*args):
    """Format the arguments with a green forgreound."""
    print(string_constructor(args, "green"))

def mega_success(*args):
    """Format the arguments with a white forgreound and a green background."""
    print(string_constructor(args, "white", "green"))

def warning(*args):
    """Format the arguments with a yellow forgreound."""
    print(string_constructor(args, "yellow"))

def mega_warning(*args):
    """Format the arguments with a white forgreound and a yellow background."""
    print(string_constructor(args, "black", "fullyellow"))

def info(*args):
    """Format the arguments with a cyan forgreound."""
    print(string_constructor(args, "cyan"))

def mega_info(*args):
    """Format the arguments with a white forgreound and a cyan background."""
    print(string_constructor(args, "white", "cyan"))

def error(*args):
    """Format the arguments with a red forgreound."""
    print(string_constructor(args, "brightred"))

def mega_error(*args):
    """Format the arguments with a white forgreound and a red background."""
    print(string_constructor(args, "white", "red"))

def randomize(*args):
    """Format the arguments with a random forgreound and background."""
    print(string_constructor(args, "rainbow"))

def inverted(*args):
    """Format the arguments with a black foreground and white background."""
    print(string_constructor(args, "black", "white"))

def custom(args, fg="normal", bg="normal"):
    """Format the single argument with a custom foreground and background."""
    print(string_constructor(args, fg, bg))

def test():
    """A test method to print out examples."""
    print("")
    print("pybugger.success(*lyric)")
    success("\"We're no strangers to love,")
    print("")
    print("pybugger.mega_success(*lyric)")
    mega_success("You know the rules and so do I")
    print("")
    print("pybugger.info(*lyric)")
    info("A full commitment's what I'm thinking of")
    print("")
    print("pybugger.mega_info(*lyric)")
    mega_info("You wouldn't get this from any other guy")
    print("")
    print("pybugger.warning(*lyric)")
    warning("I just wanna tell you how I'm feeling")
    print("")
    print("pybugger.mega_warning(*lyric)")
    mega_warning("Gotta make you understand,")
    print("")
    print("pybugger.error(*lyric)")
    error("Never gonna give you up")
    print("")
    print("pybugger.mega_error(*lyric)")
    mega_error("Never gonna let you down")
    print("")
    print("pybugger.randomize(*lyric)")
    randomize("Never gonna run around and desert you")
    print("")
    print("pybugger.custom(lyric, \"color119\", \"color93\")")
    custom("Never gonna make you cry", "color119", "color93")
    print("")
    print("pybugger.inverted(*lyric)")
    inverted("Never gonna say goodbye.")
    print("")
    print("pybugger.default(*lyric)")
    default("Never gonna tell a lie and hurt you.\"")
    print("")
