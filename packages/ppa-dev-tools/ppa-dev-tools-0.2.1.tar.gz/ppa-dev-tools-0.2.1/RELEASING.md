Releasing a New PPA Dev Tools Version
=====================================

Before you start
----------------

* Update local Git repository to the current `main` tip.  For a
  maintenance release (e.g. version 1.2.3), update to the current
  `stable-1.2` tip, instead.
* Commit everything that needs included in the release
* Verify the build system works without errors
  $ python3 setup.py bdist_wheel
  $ make build
* Verify the testsuite, lint, flake, etc. passes
  $ make check
  $ make coverage
* Verify the snapcraft config is ready
  $ snapcraft --debug
* Doublecheck all new dependencies are specified in packaging
* Doublecheck the INSTALL.md file is still up to date
* Write an entry in NEWS.md file with release notes

Prepare and commit files
------------------------

  $ export VERSION="X.Y.Z"
  $ make set-release-version
  $ git commit NEWS.md ppa/_version.py pyproject.toml snap/snapcraft.yaml -m "Releasing ${VERSION}"
  $ git tag -a -m "PPA Dev Tools ${VERSION}" "v${VERSION}"
  $ git push origin main "v${VERSION}"


Create the release directory
----------------------------

  $ cp -r ppa-dev-tools ./Releases/ppa-dev-tools-${VERSION}
  $ cd ./Releases/ppa-dev-tools-${VERSION}


Generate the sdist
------------------

  $ python setup.py sdist

* Push the sdist to pypi


Generate the debian package
---------------------------

    $ debuild -S -sa
    Push package to the PPA, wait for it to build


Generate the snap
-----------------

* Build the snap locally

  $ export SNAPCRAFT_BUILD_ENVIRONMENT_CPU=8 
  $ export SNAPCRAFT_BUILD_ENVIRONMENT_MEMORY=16G
  $ snapcraft

* Verify the snap

  $ sudo snap install ppa-dev-tools_v<version>-dirty_amd64.snap --dangerous --devmode
  ppa-dev-tools v0.2.0-dirty installed
  $ /snap/ppa-dev-tools/current/bin/ppa --version

* Push snap to the snap repository

  $ snapcraft login
  $ snapcraft upload --release edge *.snap

* Push the tag up to the repository


Announce release
----------------

    Add release announcement on Launchpad
    Send email to appropriate list(s)
    Update roadmap


Return to Development
---------------------

Add a final commit bumping the package version to a new development one

Finally, a manual `git push` (including tags) is required.
