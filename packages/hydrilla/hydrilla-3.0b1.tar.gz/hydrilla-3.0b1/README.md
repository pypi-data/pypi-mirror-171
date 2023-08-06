# Hydrilla&Haketilo

Haketilo is a tool to modify pages being opened in a web browser. It can block
pages' scripts and optionally inject user-specified ones.

Haketilo started as a browser extension (a WebExtension) with a dedicated user
scripts repository server, Hydrilla. It has since been rewritten as an HTTP
proxy. This repository contains the Python code of Hydrilla and Haketilo.

## Getting started

At the moment the recommended method of using Haketilo and Hydrilla is through
the [GNU Guix](https://guix.gnu.org/) package manager. Installation from Python
wheel is also possible but not described here.

Build instructions have been most recently tested with Guix version
1.3.0-26.fd00ac7.

### Building locally (from release tarball)

Assuming GNU Guix is already installed and working, we can execute the following
command in the project root to spawn a shell with Hydrilla & Haketilo available
inside.

```
guix environment -L . --ad-hoc -e '(@ (hydrilla) hydrilla)'
```

We can then make a test by running one of the programs, e.g.
```
haketilo --version
```

To instead install Haketilo & Hydrilla into the current Guix profile, treat your
terminal with the following incantation

```
guix package -L . -e '(@ (hydrilla) hydrilla)'
```

### Building locally (from git checkout)

Due to some nuances of the setuptools-scm tool we're using, it is necessary to
generate a project source tarball under `dist/` before building the Guix
package.

```
guix environment -L . -e '(@ (hydrilla) hydrilla)' -- python3 -m build -s
```

After that, we can start a shell with Hydrilla & Haketilo installed

```
guix environment -L . --ad-hoc -e '(@ (hydrilla) hydrilla-dist-tarball)'
```

or just install to Guix profile

```
guix package -L . -e '(@ (hydrilla) hydrilla-dist-tarball)'
```

or build a binary package suitable for distribution to other GNU/Linux users

```
guix pack -L . -RR \
    -S /hydrilla=bin/hydrilla \
    -S /hydrilla-builder=bin/hydrilla-builder \
    -S /hydrilla-server=bin/hydrilla-server \
    -S /haketilo=bin/haketilo \
    -e '(@ (hydrilla) hydrilla-dist-tarball)'
```

### Running from source

During development, it is convenient to run the tools being worked on without
putting them in a package. To spawn a shell with all development dependencies
installed, run

```
guix environment -L . -e '(@ (hydrilla) hydrilla)'
```

For software to run, we first need to compile message catalogs and make sure the
relevant metadata has been extracted from git by setuptools-scm. Inside the
shell we just spawned, we run

```
# The following command, besides building a source tarball, generates the
# src/hydrilla/_version.py file we need.
python3 -m build -s
# Generate .mo file(s) for gettext.
./setup.py compile_catalog
```

Tools can be manually tested by telling Python interpreter tu execute the
relevant module, e.g

```
PYTHONPATH=./src/ python3 -m hydrilla.mitmproxy_launcher --version
```

#### Running tests

Hydrilla uses pytest. Tests can be run with

```
pytest
```

Please refer to the
[pytest documentation](https://docs.pytest.org/en/stable/how-to/usage.html) for
more details.

#### Working on message catalogs

There are 3 commands we'll want to use.

```
# Generate a message catalog template (src/hydrilla/locales/messages.pot)
./setup.py extract_messages
# Merge the generated template into existing .po catalog file(s)
./setup.py update_catalog
# Generate .mo file(s) that will be loaded by gettext
./setup.py compile_catalog
```

Please refer to the
[Babel documentation](https://babel.pocoo.org/en/latest/messages.html#message-extraction)
for more details.

#### Exiting Guix environment

Once we're done hacking on the project, we can type

```
exit
```

in the shell... or just hit `Ctrl+d`.

### User documentation

Please look at
[our wiki](https://hydrillabugs.koszko.org/projects/haketilo/wiki) for
instructions on how to operate Haketilo and Hydrilla.

## Contributing, asking for help, giving feedback, reporting bugs

Development occurs on
[our issue tracker](https://hydrillabugs.koszko.org/projects/haketilo). You can
also write directly to [Wojtek](mailto:koszko@koszko.org) if you prefer.

## Copying

Hydrilla is Copyright (C) 2021-2022 Wojtek Kosior and contributors, entirely available under the GNU Affero General Public License version 3 or later. Some files might also give you broader permissions, see comments inside them.

*I, Wojtek Kosior, thereby promise not to sue for violation of this project's license. Although I request that you do not make use of this code in a proprietary program, I am not going to enforce this in court.*
