###################
USER-CONFIGURATION
###################
Configuration is handled by `xdgpspconf <https://pradyparanjpe.gitlab.io/xdgpspconf/>`__

Custom configuration, may be supplied using the command line flag `-c`

*********************
Configuration format
*********************
Following keys are accepted with string values;
all other keys are rejected.

- **version**: program version
- **description**: program description
- **years**: copyright years
- **license**: (case-sensitive) [currently available: LGPLv3, GPLv3, Apache, MIT]
- **license_header**: custom license header
- **pyversion**: python version for virtual environment
- **author**: Full name of author
- **email**: Email address of author
- **url**: Project URL
- **uname**: username of author (git, pypi, etc)
- **githost**: e.g. github, gitlab, etc.
- **branch**: default starting branch

Example:
==========

.. code-block:: yaml
   :caption: ${XDG_CONFIG_HOME:-${HOME}/.config}/ppstencil.yml

    version: "0!0.0dev0"
    description: "A Useful project"
    years: "2020-2022"
    license: "LGPLv3"
    pyversion: "3"
    author: "Pradyumna Paranjape"
    email: "pradyparanjpe@rediffmail.com"
    url: "https://gitlab.com/pradyparanjpe/pyprojstencil.git"
    uname: "pradyparanjpe"
    githost: "github"
    branch: "master"

.. warning::

  - all values in the configuration file will be converted to ``str``.
