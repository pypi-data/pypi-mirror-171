<p align="center" style="text-align:center;">
    <img alt="pyDVL Logo" src="https://raw.githubusercontent.com/appliedAI-Initiative/pyDVL/develop/logo.svg" width="200"/>
</p>

<p align="center" style="text-align:center;">
    A library for data valuation.
</p>

<p align="center" style="text-align:center;">
    <a href="https://github.com/appliedAI-Initiative/pyDVL/actions/workflows/tox.yaml">
        <img src="https://github.com/appliedAI-Initiative/pyDVL/actions/workflows/tox.yaml/badge.svg" alt="Build Status"/>
    </a>
</p>

<p align="center" style="text-align:center;">
    <strong>
    <a href="https://appliedAI-Initiative.github.io/pyDVL">Docs</a>
    </strong>
</p>

# Installation

To install the latest release use:

```shell
$ pip install pyDVL
```

You can also install the latest development version from [TestPyPI](https://test.pypi.org/project/pyDVL/):

```shell
pip install pyDVL --index-url https://test.pypi.org/simple/
```

For more instructions and information refer to the [Installing pyDVL section](https://appliedAI-Initiative.github.io/pyDVL/install.html)
of the documentation.

# Usage

pyDVL requires Memcached in order to cache certain results and speed-up computation.

You need to run it either locally or using Docker:

```shell
docker container run -it --rm -p 11211:11211 memcached:latest -v
```

Caching is enabled by default but can be disabled if not needed or desired. 

Once that's done you should start by creating a Dataset object with your train and test splits.
Then, you should create a model instance and a Utility object that will wrap the dataset, the model
and the scoring function. Finally, you should use one of the methods defined in the library to compute
the data valuation. Here we use Truncated Montecarlo Shapley because it is the most efficient.

Put all together:

```python
import numpy as np
from pydvl.utils import Dataset, Utility
from pydvl.shapley.montecarlo import truncated_montecarlo_shapley
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X, y = np.arange(100).reshape((50, 2)), np.arange(50)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=16
)
dataset = Dataset(X_train, X_test, y_train, y_test)
model = LinearRegression()
utility = Utility(model, dataset)
values, errors = truncated_montecarlo_shapley(u=utility, max_iterations=100)
```

For more instructions and information refer to the [Getting Started section](https://appliedAI-Initiative.github.io/pyDVL/getting-started.html) 
of the documentation 

Refer to the [Examples section](https://appliedAI-Initiative.github.io/pyDVL/examples/index.html) of the documentation for more detailed examples.

# Contributing

Please open new issues for bugs, feature requests and extensions. See more details about the structure and
workflow in the [developer's readme](README-dev.md).

# License

pyDVL is distributed under [LGPL-3.0](https://www.gnu.org/licenses/lgpl-3.0.html). 
A complete version can be found in two files: [here](LICENSE) and [here](COPYING.LESSER).

All contributions will be distributed under this license.
