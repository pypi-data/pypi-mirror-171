# pyfirth

The <code>pyfirth</code> package implements a very basic Firth-penalized logistic regression model for rare event data. There are likely more efficient and versatile methods out there.

## Dependencies

1) numpy
2) scipy
3) pandas
4) statsmodels

## Installation

The software package can be installed using pip by running the following command:
pip install PyFirth

##  Example

Here is a simple example made by binarizing some continuous data to create rare event data. Note, the Firth-penalized model is slightly more conservative.

``` python
    from pyfirth.PyFirth import PyFirth 
    import statsmodels.api as sm

    dta = sm.datasets.fair.load_pandas().data

    #create a rare count dataset by binning affair time into extreme not extreme
    dta["extreme_affairs"] = (dta["affairs"] > 10.0).astype(float)
    dta = sm.add_constant(dta)
    logit_mod = sm.Logit(dta["extreme_affairs"], dta[['const','occupation', 'educ', 'occupation_husb','rate_marriage','age','yrs_married','children','religious']])
    fitted_mod=logit_mod.fit()
    print('Logistic Regression Marriage Rating (Beta, SE, P): {0:.2f}, {1:.2f}, {2:.2e}'.format(fitted_mod.params['rate_marriage'],fitted_mod.bse['rate_marriage'],fitted_mod.pvalues['rate_marriage']))
    
    firth_test=PyFirth(dta,['const','occupation', 'educ', 'occupation_husb','rate_marriage','age','yrs_married','children','religious'],'extreme_affairs',hasconst=True)
    firth_output=firth_test.fit('rate_marriage')
    print('Firth Logistic Regression Marriage Rating (Beta, SE, P): {0:.2f}, {1:.2f}, {2:.2e}'.format(firth_output['ParamTable'].loc['rate_marriage']['BETA'],firth_output['ParamTable'].loc['rate_marriage']['SE'],firth_output['PVal']))

```

``` 
Optimization terminated successfully.
         Current function value: 0.037929
         Iterations 12
Logistic Regression Marriage Rating (Beta, SE, P): -0.79, 0.13, 3.85e-10
Firth Logistic Regression Marriage Rating (Beta, SE, P): -0.78, 0.12, 2.17e-09
```
