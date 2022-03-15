import pyfiglet


def get_banner(banner_name):

    ascii_banner = pyfiglet.figlet_format(banner_name)
    return ascii_banner