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

. "$(dirname "${0}")/common.sh" || exit 127

set_vars () {
    usage="
usage:
    $0 [-h]
    $0 [--help]"
    cwd="${PWD}"
    realenv=
    mk_flags=""
    project_root="$(dirname "$(dirname "$(realpath "${0}")")")"
    project_name="$(basename "${project_root}")"
    help_msg="

    DESCRIPTION: Run `make` in ${project_root}/docs folder

    Optional Arguments
    -h:\t\t\tshow usage command line and exit
    --help:\t\tshow this detailed help message and exit
    -r|--realenv:\tforce-override virtualenv check

    Positional Arguments
    All are passed \033[1mverbatim\033[m to make
"
}

unset_vars () {
    unset usage
    unset help_msg
    unset cwd
    unset realenv
    unset mk_flags
    unset project_root
    unset project_name
    cd "${cwd}" || exit 5
}

cli() {
    while test $# -gt 0; do
        case "${1}" in
            -h)
                clean_exit 0 "${usage}"
                ;;
            --help)
                printf "%s\n" "${usage}"
                # shellcheck disable=SC2059
                clean_exit 0 "${help_msg}"
                ;;
            -r|--realenv)
                realenv=true
                shift
                ;;
            *)
                if [ -z "${mk_flags}" ]; then
                    mk_flags="${1}"
                else
                    mk_flags="${mk_flags} ${1}"
                fi
                shift
                ;;
        esac
    done
}

make_docs () {
    pip install -U -r requirements.txt
    sphinx-build -b html "${project_root}/docs" \
        "${project_root}/docs/_build/html"
    }

main () {
    set_vars "$*"
    cli "$*"
    check_venv
    cd "${project_root}/docs" || exit 5
    make_docs
    clean_exit
}

main "$*"
