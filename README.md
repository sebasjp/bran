# Bran package

This is a python module to build confidence intervals bootstrap given a confidence level. This a first version builded from scratch like a project in Software Engineer course in the Udacity's Nanodegree - Machine Learning Engineer.

The Bran name came from the *Game of Thrones* serie. Bran Stark son of Eddard Stark, Invernalia's Mr.

<p align="center">
  <img src="https://smoda.elpais.com/wp-content/uploads/2019/04/bran.jpg" width="350">
</p>


This package is in **TestPyPi repository**. Unit tests are still missing.

# Dependences

This package requires:
* NumPy (>= 1.13.3)

# User installation

`pip install -i https://test.pypi.org/simple/ bran`

# How to use bran?

```
from bran import BootstrapCI
import numpy as np

alpha = 0.05
bootstrap = BootstrapCI(alpha = alpha)

x =  = np.random.rand(100)
li, ls = bootstrap.calculate_ci(x)
```
