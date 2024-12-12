""" Модуль для переключения приложения между режимами """
from lib_nz_commandline_procs import commandline_mode
from lib_nz_commandline_procs import get_mode_from_commandline
from lib_nz_pipeline_procs import pipe_mode
from lib_nz_dialog_procs import dialog_mode


def switch_modes() -> None:
    """
    получает режим программы
    """
    mode = get_mode_from_commandline()
    if mode == "pipe":  # в режиме конвеера
        pipe_mode()
    elif mode == "dialog":  # если в диалоговом
        dialog_mode()
    elif mode == "commandline":  # если в командном
        commandline_mode()
    else:  # неизвестный режим
        print("Unknown mode! Use mode=dialog or mode=commandline")
