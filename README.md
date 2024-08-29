# Графовый семантический движок

## Установка

```shell
pip install git+https://github.com/smer44/graph-semantical-engine.git
```

## Использование

Запустите графический интерфейс для создания, сохранения и открытия графов:
```shell
gse
```

Либо:

```shell
python -m gse.gui
```

## Концепция

[Концепция](CONCEPT.md)

## Встраивание GOL (Graph object language) в стороннее приложение

```python
from gse import gol  # Импортируйте модуль

# Загрузите GOL-файл в программу:
gol.load(file)
print(gol.loads(text))

# Сохраните GOL в файл:
gol.dump(item, file)
print(gol.dumps(item))

```

## Инструменты получения данных из wikidata

### tut_wikidata_sparkql_superclasses

Выполните:

```shell
gse-wd-sparkql Q146 cat
```

Либо:

```shell
python -m gse.tut_wikidata.tut_wikidata_sparkql_superclasses Q146 cat
```

Где `Q146` - идентификатор сущности, `cat` - наименование сущности.

Команда выдаст примерно следующее:
```text
http://www.wikidata.org/entity/Q55983715 - domesticated animal
http://www.wikidata.org/entity/Q729 - mammal
```

### tut_wikidata_soap

Выполните:

```shell
gse-wd-soap Q146
```

Либо:

```shell
python -m gse.tut_wikidata.tut_wikidata_soap Q146
```

Где `Q146` - идентификатор сущности.

Команда выдаст примерно следующее:
```text
Q55983715 - domesticated animal
Q729 - mammal
```

### tut_wikidata_get_label

Выполните:

```shell
gse-wd-label cat
```

Либо:

```shell
python -m gse.tut_wikidata.tut_wikidata_get_label cat
```

Где `cat` - наименование сущности.

Команда выдаст примерно следующее:
```text
http://www.wikidata.org/entity/Q146 - cat
```