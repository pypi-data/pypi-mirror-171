#!/usr/bin/env sh
# -*- coding: utf-8; mode: shell-script; -*-
#
# Copyright 2021 Pradyumna Paranjape
# This file is part of pyprojstencil.
#
# pyprojstencil is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyprojstencil is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pyprojstencil.  If not, see <https://www.gnu.org/licenses/>.
#

# Always run this script from its immediate parent folder


check_venv() {
    if [ -z "${VIRTUAL_ENV}" ] && [ ! ${realenv} ]; then
        printf "\033[1;31m[ERROR]\033[m Not working in a virtualenv\n\n" >&2
        printf "    \033[32m[Recommended]\033[m " >&2
        echo "activate virtualenv by typing without '# ':" >&2
        printf "        # \033[97msource " >&2
        printf "%s/.venv/bin/activate\033[m\n\n" "${project_dir}">&2
        printf "    \033[31m[Risky]\033[m " >&2
        printf "else, use --realenv flag to override this error\n" >&2
        printf "        \033[33mDo this only if " >&2
        printf "you understand virtualenv\033[m\n\n" >&2
        echo "Aborting..."
        exit 1
    fi
}


# NOTE: This file is borrowed from my own project Prady_sh_scripts
# on 2022-02-15
# Copyright 2020-2022 Pradyumna Paranjape
#
# This file is part of Prady_sh_scripts.
# Prady_sh_scripts is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Prady_sh_scripts is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Prady_sh_scripts.  If not, see <https://www.gnu.org/licenses/>.
#
# Files in this project contain regular utilities and aliases for linux (fc34)

# common functions used by all shell scripts


clean_exit() {
    unset_vars
    if [ -n "${1}" ] && [ "${1}" -ne "0" ]; then
        if [ -n "${2}" ]; then
            # shellcheck disable=SC2059
            printf "${2}\n" >&2
        fi
        # shellcheck disable=SC2086
        exit ${1}
    fi
    if [ -n "${2}" ]; then
        # shellcheck disable=SC2059
        printf "${2}\n"
    fi
    exit 0
}


check_one() {
    for dep in "$@"; do
        if command -v "${dep}" >/dev/null 2>&1; then
            return
        fi
    done
    clean_exit 127 "none of [$*] found"
}

check_dependencies() {
    for dep in "$@"; do
        if ! command -v "${dep}" >/dev/null 2>&1; then
            clean_exit 127 "'${dep}' not found"
        fi
    done
}

posix_rename() {
    # $1: target strings
    # $2: substring to be replaced
    # $3: substring to put
    if [ "${2}" = "${3}" ]; then
        printf "%s" "${1}"
        return
    fi
    if [ ! "${2#*${3}}" = "${2}" ]; then
        temp="$(posix_rename "${1}" "${2}" "___")"
        target="$(posix_rename "${temp}" "___" "${3}")"
        printf "%s" "${target}"
        return
    fi
    target="${1}"
    while [ ! "${target}" = "${target#*${2}}" ]; do
        target="${target%%${2}*}${3}${target#*${2}}"
    done
    printf "%s" "${target}"
}
