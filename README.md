# Counting-passwords
Простой скрипт для рутинных задач брутеров.
Принимает 3 аргумента:
  ifile - путь до входного файла, из которого будет браться база.
  ofile - путь до выходного файла, в который поместится информация вида <password - repitions>
  --separator - использующийся базой разделитель.

Пример:
    counting_passwords.py ifile='path/to/input/file' ofile='path/to/output/file' --separator=;
