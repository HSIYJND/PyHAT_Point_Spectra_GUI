from pysat.spectral.spectral_data import spectral_data
from pysat.regression.pls_sm import pls_sm
import pandas as pd
maskfile = "C:/Users/nicholas/Desktop/mask_minors_noise.csv"
unknowndatacsv = "C:/Users/nicholas/Desktop/lab_data_averages_pandas_format.csv"
db = "C:/Users/nicholas/Desktop/full_db_mars_corrected_dopedTiO2_pandas_format.csv"
outpath = "C:/Users/nicholas/Desktop/Output"

data = pd.read_csv(db, header=[0, 1])
data = spectral_data(data)
unknown_data = pd.read_csv(unknowndatacsv, header=[0, 1])
unknown_data = spectral_data(unknown_data)
unknown_data.interp(data.df['wvl'].columns)

data.mask(maskfile)
unknown_data.mask(maskfile)

ranges3 = [(0, 350), (350, 470), (470, 1000)]

data3 = data
data3.norm(ranges3)
unknown_data3 = unknown_data
unknown_data3.norm(ranges3)

el = 'SiO2'
nfolds_test = 6
testfold_test = 4
nfolds_cv = 5
testfold_cv = 3

compranges = [[-20, 50], [30, 70], [60, 100], [0, 120]]
nc = 20

data3.stratified_folds(nfolds=nfolds_test, sortby=('meta', el))
data3_train = data3.rows_match(('meta', 'Folds'), [testfold_test], invert=True)
data3_test = data3.rows_match(('meta', 'Folds'), [testfold_test])

ncs = [7, 7, 5, 9]
traindata = [data3_train.df, data3_train.df, data1_train.df, data3_train.df]
testdata = [data3_test.df, data3_test.df, data1_test.df, data3_test.df]

sm = pls_sm()
sm.fit(traindata, compranges, ncs, el, figpath=outpath)
predictions_train = sm.predict(traindata)
predictions_test = sm.predict(testdata)
blended_train = sm.do_blend(predictions_train, traindata[0]['meta'][el])
blended_test = sm.do_blend(predictions_test)
sm.final(testdata[0]['meta'][el],
         blended_test,
         el=el,
         xcol='Ref Comp Wt. %',
         ycol='Predicted Comp Wt. %',
         figpath=outpath)
