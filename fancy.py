white = "\033[37m"
black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
purple = "\033[35m"
cyan = "\033[36m"

reset = "\033[0;0m"
bold = "\033[1m"
underline = "\033[4m"
italic = "\033[3m"


class Colors:
    def __init__(self):
        self.white = white
        self.black = black
        self.red = red
        self.green = green
        self.yellow = yellow
        self.blue = blue
        self.purple = purple
        self.cyan = cyan
        self.reset = reset
        self.bold = bold
        self.underline = underline
        self.italic = italic

    def print_red(self, text):
        return f"{red}{text}{reset}"

    def print_green(self, text):
        return f"{green}{text}{reset}"

    def print_yellow(self, text):
        return f"{yellow}{text}{reset}"

    def print_blue(self, text):
        return f"{blue}{text}{reset}"

    def print_purple(self, text):
        return f"{purple}{text}{reset}"

    def print_cyan(self, text):
        return f"{cyan}{text}{reset}"

    def print_bold(self, text, color=white):
        return f"{color}{bold}{text}{reset}"

    def print_underline(self, text, color=white):
        return f"{color}{underline}{text}{reset}"

    def print_italic(self, text, color=white):
        return f"{color}{italic}{text}{reset}"

    def print_bold_underline(self, text, color=white):
        return f"{color}{bold}{underline}{text}{reset}"

    def print_bold_italic(self, text, color=white):
        return f"{color}{bold}{italic}{text}{reset}"

    def print_underline_italic(self, text, color=white):
        return f"{color}{underline}{italic}{text}{reset}"

    def print_bold_underline_italic(self, text, color=white):
        return f"{color}{bold}{underline}{italic}{text}{reset}"

    def print_color(self, text, color=white):
        return f"{color}{text}{reset}"

    def log_info(self, text):
        return f"[{cyan}{bold}*{reset}] {text}"

    def log_success(self, text):
        return f"[{green}{bold}+{reset}] {text}"

    def log_error(self, text):
        return f"[{red}{bold}-{reset}] {text}"

    def log_warning(self, text):
        return f"[{yellow}{bold}!{reset}] {text}"

    def log_debug(self, text):
        return f"[{blue}{bold}#{reset}] {text}"

    def log_question(self, text):
        return f"[{purple}{bold}?{reset}] {text}"


colors = Colors()


if __name__ == "__main__":
    colors = Colors()
    # print(colors.print_red("Hello, world!"))
    # print(colors.print_green("Hello, world!"))
    # print(colors.print_yellow("Hello, world!"))
    # print(colors.print_blue("Hello, world!"))
    # print(colors.print_purple("Hello, world!"))
    # print(colors.print_cyan("Hello, world!"))
    # print(colors.print_pink("Hello, world!"))
    # print(colors.print_bold("Hello, world!"))
    # print(colors.print_underline("Hello, world!"))
    # print(colors.print_italic("Hello, world!"))
    # print(colors.print_bold_underline("Hello, world!"))
    # print(colors.print_bold_italic("Hello, world!"))
    # print(colors.print_underline_italic("Hello, world!"))
    # print(colors.print_bold_underline_italic("Hello, world!"))
    # print(colors.print_color("Hello, world!", color=red))
    # print(colors.log_info("Hello, world!"))
    # print(colors.log_success("Hello, world!"))
    # print(colors.log_error("Hello, world!"))
    # print(colors.log_warning("Hello, world!"))
    # print(colors.log_debug("Hello, world!"))
    # print(colors.log_question("Hello, world!"))
