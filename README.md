RPM Build Environment for rtl8812au
===================================

Overview
--------
Environment to build rpm package of [aircrack-ng/rtl8812au][rtl8812au_repo] in
Yocto Env. for Cyclone V SoC.

[rtl8812au_repo]: https://github.com/aircrack-ng/rtl8812au

How to build
------------
```sh
$ rpmbuild -ba --clean <path to this repository top>/SPECS/<target to build>.spec
```

Requirement
-----------
* rpmbuild

License
-------
Please see `LICENSE.md` file for details.

