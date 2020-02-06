# About

**This repo is not actively maintained.**

This is a depreciated version of [pwlf](https://github.com/cjekel/piecewise_linear_fit_py), which used TensorFlow as the linear algebra backend. I wasn't keeping this TensorFlow port up-to-date with the latest and greatest changes to pwlf so it didn't make sense to keep this. 

This library is for fitting continuous piecewise linear functions to data. Just specify the number of line segments you desire and provide the data.

# How to use

```python
import numpy as np
import matplotlib.pyplot as plt
import pwlftf

# your data
y = np.array([0.00000000e+00, 9.69801700e-03, 2.94350340e-02,
              4.39052750e-02, 5.45343950e-02, 6.74104940e-02,
              8.34831790e-02, 1.02580042e-01, 1.22767939e-01,
              1.42172312e-01, 0.00000000e+00, 8.58600000e-06,
              8.31543400e-03, 2.34184100e-02, 3.39709150e-02,
              4.03581990e-02, 4.53545600e-02, 5.02345260e-02,
              5.55253360e-02, 6.14750770e-02, 6.82125120e-02,
              7.55892510e-02, 8.38356810e-02, 9.26413070e-02,
              1.02039790e-01, 1.11688258e-01, 1.21390666e-01,
              1.31196948e-01, 0.00000000e+00, 1.56706510e-02,
              3.54628780e-02, 4.63739040e-02, 5.61442590e-02,
              6.78542550e-02, 8.16388310e-02, 9.77756110e-02,
              1.16531753e-01, 1.37038283e-01, 0.00000000e+00,
              1.16951050e-02, 3.12089850e-02, 4.41776550e-02,
              5.42877590e-02, 6.63321350e-02, 8.07655920e-02,
              9.70363280e-02, 1.15706975e-01, 1.36687642e-01,
              0.00000000e+00, 1.50144640e-02, 3.44519970e-02,
              4.55907760e-02, 5.59556700e-02, 6.88450940e-02,
              8.41374060e-02, 1.01254006e-01, 1.20605073e-01,
              1.41881288e-01, 1.62618058e-01])
x = np.array([0.00000000e+00, 8.82678000e-03, 3.25615100e-02,
              5.66106800e-02, 7.95549800e-02, 1.00936330e-01,
              1.20351520e-01, 1.37442010e-01, 1.51858250e-01,
              1.64433570e-01, 0.00000000e+00, -2.12600000e-05,
              7.03872000e-03, 1.85494500e-02, 3.00926700e-02,
              4.17617000e-02, 5.37279600e-02, 6.54941000e-02,
              7.68092100e-02, 8.76596300e-02, 9.80525800e-02,
              1.07961810e-01, 1.17305210e-01, 1.26063930e-01,
              1.34180360e-01, 1.41725010e-01, 1.48629710e-01,
              1.55374770e-01, 0.00000000e+00, 1.65610200e-02,
              3.91016100e-02, 6.18679400e-02, 8.30997400e-02,
              1.02132890e-01, 1.19011260e-01, 1.34620080e-01,
              1.49429370e-01, 1.63539960e-01, -0.00000000e+00,
              1.01980300e-02, 3.28642800e-02, 5.59461900e-02,
              7.81388400e-02, 9.84458400e-02, 1.16270210e-01,
              1.31279040e-01, 1.45437090e-01, 1.59627540e-01,
              0.00000000e+00, 1.63404300e-02, 4.00086000e-02,
              6.34390200e-02, 8.51085900e-02, 1.04787860e-01,
              1.22120350e-01, 1.36931660e-01, 1.50958760e-01,
              1.65299640e-01, 1.79942720e-01])
# your desired line segment end locations
x0 = np.array([min(x), 0.039, 0.10, max(x)])

# initialize TF piecewise linear fit with your x and y data
my_pwlf = pwlftf.PiecewiseLinFitTF(x, y, dtype='float32)

# fit the data with the specified break points
# (ie the x locations of where the line segments
# will terminate)
my_pwlf.fit_with_breaks(x0)

# predict for the determined points
xHat = np.linspace(min(x), max(x), num=10000)
yHat = my_pwlf.predict(xHat)
```

# Features
For a specified number of line segments, you can determine (and predict from) the optimal continuous piecewise linear function f(x). See [this example](https://github.com/cjekel/piecewise_linear_fit_py_tf_/blob/master/examples/fitForSpecifiedNumberOfLineSegments.py).

You can fit and predict a continuous piecewise linear function f(x) if you know the specific x locations where the line segments terminate. See [this example](https://github.com/cjekel/piecewise_linear_fit_py_tf/blob/master/examples/fitWithKnownLineSegmentLocations.py).

If you want to pass different keywords for the SciPy differential evolution algorithm see [this example](https://github.com/cjekel/piecewise_linear_fit_py_tf/blob/master/examples/fitForSpecifiedNumberOfLineSegments_passDiffEvoKeywords.py).

You can use a different optimization algorithm to find the optimal location for line segments by using the objective function that minimizes the sum of square of residuals. See [this example](https://github.com/cjekel/piecewise_linear_fit_py_tf/blob/master/examples/useCustomOptimizationRoutine.py).

Instead of using differential evolution, you can now use a multi-start gradient optimization with fitfast() function. You can specify the number of starting points to use. The default is 2. This means that a latin hyper cube sampling (space filling DOE) of 2 is used to run 2 L-BFGS-B optimizations. See [this example](https://github.com/cjekel/piecewise_linear_fit_py_tf/blob/master/examples/sineWave_time_compare.py) which runs fit() function, then runs the fitfast() to compare the runtime differences!

# Installation

Or clone the repo
```
git clone https://github.com/cjekel/piecewise_linear_fit_py_tf.git
```

then install with pip
```
[sudo] pip install ./piecewise_linear_fit_py_tf
```

# How it works
This [paper](https://github.com/cjekel/piecewise_linear_fit_py_tf/raw/master/paper/pwlf_Jekel_Venter_v2.pdf) explains how this library works in detail.

This is based on a formulation of a piecewise linear least squares fit, where the user must specify the location of break points. See [this post](http://jekel.me/2018/Continous-piecewise-linear-regression/) which goes through the derivation of a least squares regression problem if the break point locations are known. Alternatively check out [Golovchenko (2004)](http://golovchenko.org/docs/ContinuousPiecewiseLinearFit.pdf).

Global optimization is used to find the best location for the user defined number of line segments. I specifically use the [differential evolution](https://docs.scipy.org/doc/scipy-0.17.0/reference/generated/scipy.optimize.differential_evolution.html) algorithm in SciPy. I default the differential evolution algorithm to be aggressive, and it is probably overkill for your problem. So feel free to pass your own differential evolution keywords to the library. See [this example](https://github.com/cjekel/piecewise_linear_fit_py_tf/blob/master/examples/fitForSpecifiedNumberOfLineSegments_passDiffEvoKeywords.py).

# Changelog
All changes now stored in [CHANGELOG.md](https://github.com/cjekel/piecewise_linear_fit_py_tf/blob/master/CHANGELOG.md)

# Requirements
Python 2.7+

```
numpy >= 1.14.0
scipy >= 1.2.0
pyDOE >= 0.3.8
setuptools >= 38.6.0
tensorflow < 2.0.0
```


# License
MIT License

# Citation

```bibtex
@Manual{pwlf,
	author = {Jekel, Charles F. and Venter, Gerhard},
	title = {{pwlf:} A Python Library for Fitting 1D Continuous Piecewise Linear Functions},
	year = {2019},
	url = {https://github.com/cjekel/piecewise_linear_fit_py}
}
```
