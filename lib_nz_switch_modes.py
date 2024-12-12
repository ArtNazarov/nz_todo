from lib_nz_commandline_procs import *
from lib_nz_pipeline_procs import *
from lib_nz_dialog_procs import *


def switch_modes() -> None:
    # получаем режим программы
    mode = get_mode_from_commandline()
    if (mode == "pipe"):  # в режиме конвеера
        pipe_mode()
    elif (mode == "dialog"):  # если в диалоговом
        dialog_mode()
    elif (mode == "commandline"):  # если в командном
        commandline_mode()
    else:  # неизвестный режим
        print("Unknown mode! Use mode=dialog or mode=commandline")