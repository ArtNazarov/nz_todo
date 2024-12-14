""" Модуль для переключения приложения между режимами """
from lib_nz_commandline_procs import commandline_mode
from lib_nz_commandline_procs import get_mode_from_commandline, get_project_id_from_commandline
from lib_nz_pipeline_procs import pipe_mode
from lib_nz_dialog_procs import dialog_mode
from lib_nz_scroll_table import scroll_mode_projects, scroll_mode_tasks
from lib_nz_servermode import server_mode

def switch_modes() -> None:
    """
    получает режим программы
    """
    mode = get_mode_from_commandline()
    match mode:
        case "pipe":  # в режиме конвеера
            pipe_mode()
        case "dialog":  # если в диалоговом
            dialog_mode()
        case "commandline":  # если в командном
            commandline_mode()
        case "scrollviewer:projects":
            scroll_mode_projects()
        case "scrollviewer:tasks":
            scroll_mode_tasks(get_project_id_from_commandline())
        case "server":
            server_mode()
        case _:  # неизвестный режим
            print("Unknown mode! Use mode=dialog|commandline|scrollviewer:projects|scrollviewer:tasks|pipe|server")
