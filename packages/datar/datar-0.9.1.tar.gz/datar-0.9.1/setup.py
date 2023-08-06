# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datar',
 'datar.base',
 'datar.core',
 'datar.core.backends',
 'datar.core.backends.pandas',
 'datar.core.backends.pandas.api',
 'datar.core.backends.pandas.core',
 'datar.datar',
 'datar.datasets',
 'datar.dplyr',
 'datar.forcats',
 'datar.tibble',
 'datar.tidyr']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.3,<2.0',
 'pdtypes>=0.0,<0.1',
 'pipda>=0.8,<0.9',
 'python-simpleconf[toml]>=0.5,<0.6']

extras_require = \
{'modin': ['modin>=0.10,<0.11'],
 'scipy': ['scipy>=1.6,<2.0'],
 'slugify': ['python-slugify>=6,<7'],
 'wcwidth': ['wcwidth>=0.2,<0.3']}

setup_kwargs = {
    'name': 'datar',
    'version': '0.9.1',
    'description': 'Port of dplyr and other related R packages in python, using pipda.',
    'long_description': '# datar\n\nA Grammar of Data Manipulation in python\n\n<!-- badges -->\n[![Pypi][6]][7] [![Github][8]][9] ![Building][10] [![Docs and API][11]][5] [![Codacy][12]][13] [![Codacy coverage][14]][13]\n\n[Documentation][5] | [Reference Maps][15] | [Notebook Examples][16] | [API][17] | [Blog][18]\n\n<img width="30%" style="margin: 10px 10px 10px 30px" align="right" src="logo.png">\n\n`datar` is a re-imagining of APIs of data manipulation libraries in python (currently only `pandas` supported) so that you can manipulate your data with it like with `dplyr` in `R`.\n\n`datar` is an in-depth port of `tidyverse` packages, such as `dplyr`, `tidyr`, `forcats` and `tibble`, as well as some functions from base R.\n\n## Installation\n\n```shell\npip install -U datar\n\n# install pdtypes support\npip install -U datar[pdtypes]\n\n# install dependencies for modin as backend\npip install -U datar[modin]\n# you may also need to install dependencies for modin engines\n# pip install -U modin[ray]\n```\n\n## Example usage\n\n```python\nfrom datar import f\nfrom datar.dplyr import mutate, filter, if_else\nfrom datar.tibble import tibble\n# or\n# from datar.all import f, mutate, filter, if_else, tibble\n\ndf = tibble(\n    x=range(4),  # or c[:4]  (from datar.base import c)\n    y=[\'zero\', \'one\', \'two\', \'three\']\n)\ndf >> mutate(z=f.x)\n"""# output\n        x        y       z\n  <int64> <object> <int64>\n0       0     zero       0\n1       1      one       1\n2       2      two       2\n3       3    three       3\n"""\n\ndf >> mutate(z=if_else(f.x>1, 1, 0))\n"""# output:\n        x        y       z\n  <int64> <object> <int64>\n0       0     zero       0\n1       1      one       0\n2       2      two       1\n3       3    three       1\n"""\n\ndf >> filter(f.x>1)\n"""# output:\n        x        y\n  <int64> <object>\n0       2      two\n1       3    three\n"""\n\ndf >> mutate(z=if_else(f.x>1, 1, 0)) >> filter(f.z==1)\n"""# output:\n        x        y       z\n  <int64> <object> <int64>\n0       2      two       1\n1       3    three       1\n"""\n```\n\n```python\n# works with plotnine\n# example grabbed from https://github.com/has2k1/plydata\nimport numpy\nfrom datar.base import sin, pi\nfrom plotnine import ggplot, aes, geom_line, theme_classic\n\ndf = tibble(x=numpy.linspace(0, 2*pi, 500))\n(df >>\n  mutate(y=sin(f.x), sign=if_else(f.y>=0, "positive", "negative")) >>\n  ggplot(aes(x=\'x\', y=\'y\')) +\n  theme_classic() +\n  geom_line(aes(color=\'sign\'), size=1.2))\n```\n\n![example](./example.png)\n\n```python\n# very easy to integrate with other libraries\n# for example: klib\nimport klib\nfrom pandas import Series\nfrom pipda import register_verb\nfrom datar.datasets import iris\nfrom datar.dplyr import pull\n\ndist_plot = register_verb(Series, func=klib.dist_plot)\niris >> pull(f.Sepal_Length) >> dist_plot()\n```\n\n![example](./example2.png)\n\n\n[1]: https://tidyr.tidyverse.org/index.html\n[2]: https://dplyr.tidyverse.org/index.html\n[3]: https://github.com/pwwang/pipda\n[4]: https://tibble.tidyverse.org/index.html\n[5]: https://pwwang.github.io/datar/\n[6]: https://img.shields.io/pypi/v/datar?style=flat-square\n[7]: https://pypi.org/project/datar/\n[8]: https://img.shields.io/github/v/tag/pwwang/datar?style=flat-square\n[9]: https://github.com/pwwang/datar\n[10]: https://img.shields.io/github/workflow/status/pwwang/datar/Build%20and%20Deploy?style=flat-square\n[11]: https://img.shields.io/github/workflow/status/pwwang/datar/Build%20Docs?label=Docs&style=flat-square\n[12]: https://img.shields.io/codacy/grade/3d9bdff4d7a34bdfb9cd9e254184cb35?style=flat-square\n[13]: https://app.codacy.com/gh/pwwang/datar\n[14]: https://img.shields.io/codacy/coverage/3d9bdff4d7a34bdfb9cd9e254184cb35?style=flat-square\n[15]: https://pwwang.github.io/datar/reference-maps/ALL/\n[16]: https://pwwang.github.io/datar/notebooks/across/\n[17]: https://pwwang.github.io/datar/api/datar/\n[18]: https://pwwang.github.io/datar-blog\n[19]: https://github.com/pwwang/datar-cli\n',
    'author': 'pwwang',
    'author_email': 'pwwang@pwwang.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/pwwang/datar',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
