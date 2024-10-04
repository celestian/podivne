# Podivné

## Co je cílem?

* Mít aplikačku ppp, která si založí log file a něco do něj píše. Logger této aplikačky =íše vše do logu, ale... od error levelu píše i na terminál.

* Testovat tuto ppp apku pomocí behave tak, aby běžela jako subprocess a bylo možné s ní interagovat. (inquererpy, subprocess, možná pexpect)


## Užitečné pžíkazy

```
nox -s dev && source .venv/bin/activate


behave --no-capture --no-capture-stderr features/

#deactivate
nox
```