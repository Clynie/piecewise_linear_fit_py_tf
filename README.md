# About
A library for fitting a continuous piecewise linear function f(x) to data. Just specify the number of line segments you desire and your data set.

Check out the [examples](https://github.com/cjekel/piecewise_linear_fit_py/tree/master/examples)!

Read the [blog post](http://jekel.me/2017/Fit-a-piecewise-linear-function-to-data/).

![Example of a continuous piecewise linear fit to a data set.](https://github.com/cjekel/piecewise_linear_fit_py/blob/master/examples/examplePiecewiseFit.png)

![Example of a continuous piecewise linear fit to a sin wave](https://github.com/cjekel/piecewise_linear_fit_py/blob/master/examples/sinWaveFit.png)

# Features
For a specified number of line segments, you can determine (and predict from) the optimal continuous piecewise linear function f(x). See [this example](https://github.com/cjekel/piecewise_linear_fit_py/blob/master/examples/fitForSpecifiedNumberOfLineSegments.py).

You can fit and predict a continuous piecewise linear function f(x) if you know the specific x locations where the line segments terminate. See [this example](https://github.com/cjekel/piecewise_linear_fit_py/blob/master/examples/fitWithKnownLineSegmentLocations.py).

If you want to pass different keywords for the SciPy differential evolution algorithm see [this example](https://github.com/cjekel/piecewise_linear_fit_py/blob/master/examples/fitForSpecifiedNumberOfLineSegments_passDiffEvoKeywords.py).

You can use a different optimization algorithm to find the optimal location for line segments by using the objective function that minimizes the sum of square of residuals. See [this example](https://github.com/cjekel/piecewise_linear_fit_py/blob/master/examples/useCustomOptimizationRoutine.py).

# How it works
This is based on a formulation of a piecewise linear least squares fit, where the user must specify the location of break points. A simple derivation of this fit has been done by [Golovchenko (2004)](http://golovchenko.org/docs/ContinuousPiecewiseLinearFit.pdf). The routine for fitting the piecewise linear function is based on Golovchenko's MATLAB code (which I can't seem to find on the internet), which I ported to Python. Alternatively you can view [this code](https://www.mathworks.com/matlabcentral/fileexchange/40913-piecewise-linear-least-square-fit).

Global optimization is used to find the best location for the user defined number of lline segments. I specifically use the [differential evolution](https://docs.scipy.org/doc/scipy-0.17.0/reference/generated/scipy.optimize.differential_evolution.html) algorithm in SciPy. I default the differential evolution algorithm to be aggressive, and it is probably overkill for your problem. So feel free to pass your own differential evolution keywords to the library. See [this example](https://github.com/cjekel/piecewise_linear_fit_py/blob/master/examples/fitForSpecifiedNumberOfLineSegments_passDiffEvoKeywords.py).

# Why
All other methods require the user to specify the specific location of break points, but in most cases the best location for these break points is unknown. It makes more sense to rather have the user specify the desired number of line segments, and then to quantitatively choose the best location for the ends of these line segments.

# Changelog
- 2017/10/31 bug fix related to the case where break points exactly equal to x data points ( as per issue https://github.com/cjekel/piecewise_linear_fit_py/issues/1 ) and added attributes .sep_data_x, .sep_data_y, .sep_predict_data_x for troubleshooting issues related to the separation of data points to their respective regions
- 2017/10/20 remove determinant calculation and use try-except instead, this will offer a larger performance boost for big problems. Change library name to something more Pythonic. Add version attribute.
- 2017/08/03 gradients (slopes of the line segments) now stored as piecewise_lin_fit.slopes (or myPWLF.slopes) after they have been calculated by performing a fit or predicting
- 2017/04/01 initial release

# Requirements
Python 2.7+ (Python 2.7 and Python 3.4 have been tested)

NumPy (Tested on version >= 1.11.3 )

SciPy (Tested on version >= 0.19.0)

# License
MIT License
