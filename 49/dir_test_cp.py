import os

from pathlib import Path

#当前路径
print(os.path.abspath('.'))

print(os.path.exists('E:\LearnPythonGithub'))


q = Path('E:/zzzz/xxx')
Path.mkdir(q,parents=True)