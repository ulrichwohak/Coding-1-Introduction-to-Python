# Module 06: Writing Functions

Teach this module immediately after [Module 05: Conditionals and control flow](../module05-conditionals/).
[Module 07: Graphing](../module07-graphs-basics/) follows in the next session.

## Motivation

One of the best ways to improve your reach as a data scientist is to write functions. Functions allow automating common tasks in a more powerful and general way than copy-and-pasting. Writing a function has three big advantages over using copy-and-paste:

1. You can give a function an evocative name that makes your code easier to understand.
2. As requirements change, you only need to update code in one place, instead of many.
3. You eliminate the chance of making incidental mistakes when you copy and paste (i.e. updating a variable name in one place, but not in another).

Writing good functions is a lifetime journey. Even after using Python for many years, one can still learn new techniques and better ways of approaching old problems. The goal is not to teach you every esoteric detail of functions but to get you started with some pragmatic advice that you can apply immediately.

## This module

This module introduces functions, how they are structured and how to write them.
It compares positional and keyword arguments using the same power function,
including default values and mixed calls. The docstring example distinguishes
Python's general PEP 257 conventions from the optional NumPy-style layout.


## Learning outcomes
After successfully live-coding the material (see: [`functions.ipynb`](functions.ipynb)), students will know on

- how to create user-defined functions
- what is the structure of a function
- the difference between parameters and arguments, and how default values work
- how to call functions with positional arguments, keyword arguments, or both
- how to document inputs, returned values, and side effects in a docstring
- the use of the `help` function to retrieve function descriptions
- the use of `lambda` function

## Module Time

Ideal overall time: **20-30 mins**.


## Homework

*Type*: quick practice, approx 15 mins, together with [`module05-conditionals`](../module05-conditionals/).

Bootstrapping - using the [`sp500`](https://gabors-data-analysis.com/datasets/#sp500) data

  - download the cleaned data for `sp500` from [OSF](https://osf.io/h64z2/)
  - write a function, which calculates the bootstrap standard errors and confidence intervals based on these standard errors.
    - function should have an input for a) vector of prices, b) number of bootstraps, c) level for the confidence interval
  - create a new variable for `sp500`: `daily_return`, which is the difference in the prices from one day to the next day.
  - use this `daily_return` variable and calculate the 80% confidence interval based on bootstrap standard errors along with the mean.


## Further material

  - [Python tutorial: keyword arguments](https://docs.python.org/3.12/tutorial/controlflow.html#keyword-arguments)
  - [PEP 257: Docstring Conventions](https://peps.python.org/pep-0257/)
  - [NumPy-style docstring guide](https://numpydoc.readthedocs.io/en/latest/format.html)

  - Case study materials from Gabor's da_case_studies repository on generalization (with bootstrapping) is: [ch05-stock-market-loss-generalize](https://github.com/gabors-data-analysis/da_case_studies/tree/master/ch05-stock-market-loss-generalize) on testing are: [ch06-online-offline-price-test](https://github.com/gabors-data-analysis/da_case_studies/tree/master/ch06-online-offline-price-test) and [ch06-stock-market-loss-test](https://github.com/gabors-data-analysis/da_case_studies/tree/master/ch06-stock-market-loss-test)
