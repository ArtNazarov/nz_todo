About
===
The simplest notes

Usage
===
The dialog (interactive) mode

```
    python term_todos.py mode=dialog
```
or

```
    python term_todos.py
```

App menu in dialog mode is:

```
Путь к индексному файлу со списком проектов index.projects установлен в /home/artem/nz_todo/index.projects
Выбери действие...
q для выхода
h для сведений о программе
lP для списка проектов
+P для добавления проекта в список
vP чтобы посмотреть проект
eP чтобы отредактировать проект
xP чтобы удалить проект
+T чтобы добавить задачу в проект
lT чтобы посмотреть список задач в проекте
vT чтобы посмотреть параметры задачи проекта
xT чтобы удалить задачу из проекта
eT чтобы отредактировать задачу в проекте
```

The commandline mode like
```
    python term_todos.py mode=commandline opcode=vP
```

To specify project_id: ``` project_id=someProjectId ``` 

To specify task_id: ``` task_id=someProjectId ``` 

To specify opcode: ``` opcode=CODE ```

The opcode values:

- lP for listing projects
- +P to add new project
- vP to view project info
- +I to add info about project
- eI to edit info about project
- xP to erase project
- lT for listing tasks (in the some project)
- +T to add new task
- eT to edit new task
- xT to erase some task
- vT to view some task

To specify properties (fields) values: ```.someFieldName=someFieldValue```

Script creates index.projects file in app directory with list of projects.
For each new project will be create folder project_ProjectName that
contained values of attributes in files names ProjectName.AttrName

Script creates index.tasks file in project directory with list of tasks ID.
For each new task will be create folder task_TaskId that
contained values of attributes in files names taskId.AttrName

Pipe mode
===

Use like:

```
echo ' opcode = "+P" ; project_id="test" #  opcode = "lP" ' | python term_todos.py mode=pipe
```

