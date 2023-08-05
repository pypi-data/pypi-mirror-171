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
    $0 -h
    $0 --help
    $0 [-y|--assume-yes] [-r|--realenv] [*]"
    cwd="${PWD}"
    realenv=
    assume_yes=""
    in_flags=""
    project_dir="$(dirname "$(dirname "$(readlink -f "${0}")")")"
    project_name="$(basename "${project_dir}")"
    help_msg="${usage}

    DESCRIPTION: install \033[3m${project_name}/requirements.txt\033[m
       on ${VIRTUAL_ENV:-user\'s environment}


    Optional Arguments
    -h:\t\t\tshow usage command line and exit
    --help:\t\tshow this detailed help message and exit
    -r|--realenv:\tforce-override virtualenv check

    Positional Arguments
    All are passed \033[1mverbatim\033[m to pip install
"
}

unset_vars () {
    cd "${cwd}" || exit 5
    unset usage
    unset help_msg
    unset cwd
    unset realenv
    unset in_flags
    unset project_dir
    unset project_name
}

cli() {
    while test $# -gt 0; do
        case "${1}" in
            -h)
                clean_exit 0 "${usage}"
                ;;
            --help)
                clean_exit 0 "${help_msg}"
                ;;
            -r|--realenv)
                realenv=true
                shift
                ;;
            *)
                in_flags="${in_flags} ${1}"
                shift
                ;;
        esac
    done
}

pip_install () {
    # DONT: we do WANT to glob this
    # shellckeck disable=SC2086
    pip install -U -r ../requirements.txt
    pip install -U -r ./requirements.txt
    pip install -U -r ../docs/requirements.txt
}

main () {
    set_vars "$*"
    cli "$*"
    cd "${project_dir}/code-aid" || clean_exit 65
    check_venv
    pip_install
    clean_exit
}

main "$*"
