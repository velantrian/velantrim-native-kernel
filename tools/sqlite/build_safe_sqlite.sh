#!/usr/bin/env bash
set -euo pipefail

readonly sqlite_version="3.51.3"
readonly sqlite_archive_version="3510300"
readonly sqlite_archive_sha256="81f5be397049b0cae1b167f2225af7646fc0f82e4a9b3c48c9ea3a533e21d77a"
readonly sqlite_url="https://sqlite.org/2026/sqlite-autoconf-${sqlite_archive_version}.tar.gz"

if [[ $# -lt 1 || $# -gt 2 ]]; then
  echo "usage: $0 ABSOLUTE_INSTALL_PREFIX [PYTHON_EXECUTABLE]" >&2
  exit 2
fi

readonly install_prefix="$1"
readonly python_executable="${2:-python3}"
if [[ "$install_prefix" != /* || "$install_prefix" == "/" ]]; then
  echo "install prefix must be an absolute non-root path" >&2
  exit 2
fi

readonly build_root="$(mktemp -d /tmp/native-kernel-sqlite-build.XXXXXX)"
readonly archive_path="$build_root/sqlite.tar.gz"
trap 'rm -rf -- "$build_root"' EXIT

curl --fail --location --silent --show-error "$sqlite_url" --output "$archive_path"
echo "$sqlite_archive_sha256  $archive_path" | sha256sum --check --strict
tar --extract --gzip --no-same-owner --file "$archive_path" --directory "$build_root"

cd "$build_root/sqlite-autoconf-${sqlite_archive_version}"
./configure --prefix="$install_prefix" --disable-static --enable-shared
make -j2
make install

LD_LIBRARY_PATH="$install_prefix/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}" \
  "$python_executable" -c \
  "import sqlite3; assert sqlite3.sqlite_version == '${sqlite_version}', sqlite3.sqlite_version; print(sqlite3.sqlite_version)"
