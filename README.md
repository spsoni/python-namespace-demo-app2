# python-namespace-demo-app2


This is a `sub-command` GIT repository called `app2`

Implementation module for sub-command `app2` is `namespace_demo.app2`

**Note 1:** We have `namespace_demo.main_app2.py` to wrap CLI. We are not overwriting base module `namespace_demo.main`.

**Note 2**: main cli is still from base module `demo-cli = "namespace_demo.main_app2:cli"` so that app2 is available as sub-command
