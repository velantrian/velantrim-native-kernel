# 🚀 Быстрый старт Native Kernel

**[English](./QUICKSTART.md) · [Русский](./QUICKSTART.ru.md)**

> **Граница:** это исследовательский репозиторий. Запуск тестов не разрешает production-использование, не расширяет assertion map и не доказывает substrate neutrality.

## 1. Требования

- Python 3.11 или 3.12;
- Bash;
- для сборки закреплённого SQLite: `curl`, `sha256sum`, `tar`, C-компилятор, `make` и стандартные build tools;
- опционально PostgreSQL 16 или 18 и Psycopg для integration tests.

Сейчас репозиторий запускается из корня checkout с семантикой `PYTHONPATH=.`. Опубликованного Python package и поддерживаемого контракта `pip install` пока нет.

## 2. Быстрая проверка semantic core

Из корня репозитория:

```bash
python -m unittest discover -s tests -p 'test_semantic_core.py' -v
python -m unittest discover -s tests -p 'test_p1_manifest.py' -v
python -m compileall -q native_kernel
```

Эти проверки охватывают технологически нейтральное semantic core и P1 manifest. Они не проверяют PostgreSQL, SQLite WAL, C3 equivalence, C4 shadow evaluation или C5 rehearsal.

## 3. Почему системный SQLite может быть отклонён

SQLite profile открывает WAL только тогда, когда **фактически linked** библиотека Python `sqlite3` имеет версию SQLite 3.51.3 или новее. Старые версии намеренно отклоняются fail-closed: ADR-0023 не принимает их для текущего safe-runtime profile.

Проверить версию, которую реально загружает Python:

```bash
python -c 'import sqlite3; print(sqlite3.sqlite_version)'
```

Ошибка из-за старого linked SQLite не является пропущенной проверкой безопасности и не должна превращаться в pass.

## 4. Сборка закреплённого SQLite 3.51.3

```bash
tools/sqlite/build_safe_sqlite.sh \
  /tmp/native-kernel-sqlite-3.51.3 \
  "$(command -v python)"
```

Запустить Python с этой shared library:

```bash
export LD_LIBRARY_PATH="/tmp/native-kernel-sqlite-3.51.3/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
python -c 'from native_kernel.sqlite_profile import linked_sqlite_version; print(linked_sqlite_version())'
```

Ожидаемый вывод:

```text
3.51.3
```

Build script загружает официальный source archive, проверяет закреплённый SHA-256 до распаковки, собирает библиотеку в явном non-root prefix и проверяет, что именно загрузил Python. См. [`../tools/sqlite/README.md`](../tools/sqlite/README.md).

## 5. SQLite unit checks

После экспорта `LD_LIBRARY_PATH`:

```bash
python -m unittest discover -s tests -p 'test_sqlite_profile_unit.py' -v
python -m unittest discover -s tests -p 'test_p5_manifest.py' -v
python tools/profiles/validate_p5_manifest.py
```

Часть integration tests также требует PostgreSQL и переменных окружения ниже.

## 6. PostgreSQL integration setup

Установить текущий CI-диапазон драйвера:

```bash
python -m pip install -r profiles/postgresql-reference-v0/requirements-p2-ci.txt
```

Подготовить disposable PostgreSQL database и задать:

```bash
export NK_TEST_POSTGRES_DSN='postgresql://postgres:postgres@127.0.0.1:5432/native_kernel_test'
```

Затем запустить соответствующие integration suites:

```bash
python -m unittest discover -s tests -p 'test_p2_postgresql_integration.py' -v
python -m unittest discover -s tests -p 'test_p5_cross_profile_integration.py' -v
```

Используйте только тестовую базу. Репозиторий не предоставляет production IAM, backup, HA, compliance или deployment policy.

## 7. Полный локальный discovery

```bash
python -m unittest discover -s tests -v
```

Результаты нужно трактовать строго:

- PostgreSQL-only tests могут быть skipped без `NK_TEST_POSTGRES_DSN`;
- SQLite profile tests должны fail-closed, если Python связан с неподдерживаемой версией SQLite;
- локальный pass не равен repository CI evidence;
- repository CI evidence ограничено точным commit, workflow, matrix и сохранёнными artifacts.

## 8. Что прочитать перед изменением кода

1. [`../AGENTS.md`](../AGENTS.md)
2. [`../STATUS.md`](../STATUS.md)
3. [`ai/README.md`](./ai/README.md)
4. [`GLOSSARY.ru.md`](./GLOSSARY.ru.md)
5. соответствующие ADR и profile documents

Правила contribution и синхронизации: [`../CONTRIBUTING.md`](../CONTRIBUTING.md).
