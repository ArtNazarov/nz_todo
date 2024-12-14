About
===
The simplest notes

Running tests
===
```
./tests.sh
```
or
```
python run_tests.py
```

Requirements
===
prettytable

```
python -m venv .
source bin/activate
pip install prettytable
```

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
q для выхода
h для сведений о программе
lP для списка проектов
LP для списка проектов в табличной форме
+P для добавления проекта в список
vP чтобы посмотреть проект
eP чтобы отредактировать проект
xP чтобы удалить проект
+T чтобы добавить задачу в проект
lT чтобы посмотреть список задач в проекте
LT для списка задача к проекту в табличной форме
vT чтобы посмотреть параметры задачи проекта
xT чтобы удалить задачу из проекта
eT чтобы отредактировать задачу в проекте
mP - режим просмотра проектов
mT - режим просмотра задач
+F - фильтр на данные (при совпадении отображать)
-F - отмена фильтрации
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

For example, create file 'Instructions.txt'

```
opcode = "+P" ; project_id="testProject" #
opcode = "lP" #
opcode = "xP" ; project_id="testProject" #
opcode = "lP" 
```

Use it with cat
```
 cat Instructions.txt | python term_todos.py mode=pipe 
```
Examples

```
cat addProjects.txt | python term_todos.py mode=pipe
cat addTasks.txt | python term_todos.py mode=pipe
```

Will output:

```
Maybe new file: [Errno 2] No such file or directory: '/home/artem/nz_todo/index.projects'
testProject
Проект с ID 'testProject' успешно удалён.
Каталога /home/artem/nz_todo/project_testProject нет, удалять нечего
Проектов не найдено!
```

Deps graph
===
[View on Gauge](https://show.gauge.sh/?uid=82ba29cb-fbc0-417c-b2b4-2005b1978519)

