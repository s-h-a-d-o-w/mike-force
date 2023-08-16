import sys
from os import path


def is_executable() -> bool:
    """
    Determine if the current script is packaged as an executable\n
    (EG: If packed into a .exe with PyInstaller)\n
    returns : True/False, if the script is an executable
    """

    return getattr(sys, "frozen", False)


def script_dir() -> str:
    """
    Get the path to the current script's directory, whether running as an executable or in an interpreter.\n
    returns : A string containing the path to the script directory.
    """

    return (
        path.dirname(sys.executable)
        if is_executable()
        else path.join(path.dirname(path.realpath(sys.argv[0])))
    )


def local_path(dir_name: str = "") -> str:
    """
    Get the absolute path to a local file/directory __MEIPASS or .), whether running as an executable or in an interpreter.\n
    returns : A string containing the path to the local file/directory
    """

    return (
        path.join(sys._MEIPASS, dir_name)  # type: ignore
        if is_executable()
        else path.join(script_dir(), dir_name)
    )
