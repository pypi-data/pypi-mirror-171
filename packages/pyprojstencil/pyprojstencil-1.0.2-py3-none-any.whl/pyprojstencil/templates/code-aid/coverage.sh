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
    $0 [-y|--assume-yes] [-r|--realenv] [*] "
    cwd="${PWD}"
    realenv=
    ct_flags=""
    project_root="$(dirname "$(dirname "$(readlink -f "${0}")")")"
    project_name="$(basename "${project_root}")"
    help_msg="${usage}

    DESCRIPTION: Run unit tests in ${project_root}/tests folder
    and create a ${project_root}/docs/coverage.svg badge

    Optional Arguments
    -h:\t\t\tshow usage command line and exit
    --help:\t\tshow this detailed help message and exit
    -r|--realenv:\tforce-override virtualenv check

    Positional Arguments
    All are passed \033[1mverbatim\033[m to coverage
"
}

unset_vars () {
    unset usage
    unset help_msg
    unset cwd
    unset realenv
    unset ct_flags
    unset project_root
    unset project_name
    cd "${cwd}" || exit 65
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
            -y|--assume-yes)
                assume_yes="-y"
                shift
                ;;
            *)
                ct_flags="${ct_flags} ${1}"
                shift
                ;;
        esac
    done
}

coverage_test () {
    coverage run -m pytest --junitxml=report.xml "${project_root}/tests"
    coverage xml
    coverage-badge > "${project_root}/docs/coverage.svg"
}

main () {
    set_vars "$*"
    cli "$*"
    check_venv
    cd "${project_root}/tests" || clean_exit 65
    coverage_test
    clean_exit
}

main "$*"
