#!/usr/bin/env python
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.contrib.completers import WordCompleter
from pygments.lexers.sql import SqlLexer

sql_completer = WordCompleter(['SELECT', 'SHOW', 'FROM', 'WHERE'], ignore_case=True)

while True:
    inp = prompt(u'> ',
                 history=FileHistory('history.txt'),
                 auto_suggest=AutoSuggestFromHistory(),
                 completer=sql_completer,
                 lexer=SqlLexer
                 )
    print(inp)
