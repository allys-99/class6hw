# class6hw
plotting

References
  matplotlib series
  https://www.youtube.com/watch?v=q7Bo_J8x_dw&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF 

  Matplotlib Tutorial 3 bar charts and histograms
  https://www.youtube.com/watch?v=ZyTO4SwhSeE

  scatterplot
  https://www.youtube.com/watch?v=WbTOutpwPHs

  markers
  https://jakevdp.github.io/PythonDataScienceHandbook/04.02-simple-scatter-plots.html

  pandas dataframe tutorial

  https://www.youtube.com/watch?v=F6kmIpWWEdU

  3d code
  https://stackoverflow.com/questions/1985856/how-to-make-a-3d-scatter-plot-in-python


  good intro to panda
  https://www.youtube.com/watch?v=CmorAWRsCAw

  reset index
  https://cmdlinetips.com/2018/04/how-to-reset-index-in-pandas-dataframe/





# 1 Feature Histogram

Plotting each feature in a histogram is located in 

oneFeature/wineplotHist.py

>python wineplotHist.py

the mean and standard deviation is displayed

                                     Mean
Alcohol                          13.000618
Malic Acid                        2.336348
Ash                               2.366517

                           Standard Deviation
Alcohol                           0.811827
Malic Acid                        1.117146
Ash                               0.274344

-rw-r--r-- 1 plav 197609 17831 Feb 22 20:59 'hist_Alcalinity of Ash.png'
-rw-r--r-- 1 plav 197609 15357 Feb 22 20:59  hist_Alcohol.png
-rw-r--r-- 1 plav 197609 15084 Feb 22 20:59  hist_Ash.png
-rw-r--r-- 1 plav 197609 17552 Feb 22 20:59 'hist_Colour Intensity.png'
-rw-r--r-- 1 plav 197609 15416 Feb 22 20:59  hist_Flavanoids.png
-rw-r--r-- 1 plav 197609 13858 Feb 22 20:59  hist_Hue.png
-rw-r--r-- 1 plav 197609 18784 Feb 22 20:59  hist_Magnesium.png
-rw-r--r-- 1 plav 197609 17856 Feb 22 20:59 'hist_Malic Acid.png'
-rw-r--r-- 1 plav 197609 17495 Feb 22 20:59 'hist_Nonflavanoid Phenols.png'
-rw-r--r-- 1 plav 197609 20396 Feb 22 20:59 'hist_OD280_OD315 of diluted wines.png'
-rw-r--r-- 1 plav 197609 16308 Feb 22 20:59  hist_Proanthocyanins.png
-rw-r--r-- 1 plav 197609 15489 Feb 22 21:00  hist_Proline.png
-rw-r--r-- 1 plav 197609 16214 Feb 22 20:59 'hist_Total Phenols.png'

# 2 Features Scatter

the python script is located in
twoFeature/wineplotScat.py
>python wineplotScat.py  # to execute

The mean and standard deviation is displayed.
All the (78)filenames that were saved is also printed.

    fname= scat_Nonflavanoid PhenolsProanthocyanins.png
    fname= scat_Nonflavanoid PhenolsColour Intensity.png
    fname= scat_Nonflavanoid PhenolsHue.png
    fname= scat_Nonflavanoid PhenolsOD280_OD315 of diluted wines.png
    fname= scat_Nonflavanoid PhenolsProline.png
    fname= scat_ProanthocyaninsColour Intensity.png
    fname= scat_ProanthocyaninsHue.png
    fname= scat_ProanthocyaninsOD280_OD315 of diluted wines.png
    fname= scat_ProanthocyaninsProline.png
    fname= scat_Colour IntensityHue.png
    fname= scat_Colour IntensityOD280_OD315 of diluted wines.png
    fname= scat_Colour IntensityProline.png
    fname= scat_HueOD280_OD315 of diluted wines.png
    fname= scat_HueProline.png
    fname= scat_OD280_OD315 of diluted winesProline.png

# 3 Features 3D

The python script is in 
threeFeature/wineplot3DScat.py

python wineplot3DScat.py    # to execute

Many files are generated.  Ctrl-C to kill the script.

plotting 3D figure for :  Alcohol vs. Malic Acid vs. Ash
plotting 3D figure for :  Alcohol vs. Malic Acid vs. Alcalinity of Ash
plotting 3D figure for :  Alcohol vs. Malic Acid vs. Magnesium
plotting 3D figure for :  Alcohol vs. Malic Acid vs. Total Phenols
plotting 3D figure for :  Alcohol vs. Malic Acid vs. Flavanoids
plotting 3D figure for :  Alcohol vs. Malic Acid vs. Nonflavanoid Phenols
plotting 3D figure for :  Alcohol vs. Malic Acid vs. Proanthocyanins
plotting 3D figure for :  Alcohol vs. Malic Acid vs. Colour Intensity
plotting 3D figure for :  Alcohol vs. Malic Acid vs. Hue
plotting 3D figure for :  Alcohol vs. Malic Acid vs. OD280_OD315 of diluted wines
plotting 3D figure for :  Alcohol vs. Malic Acid vs. Proline
plotting 3D figure for :  Alcohol vs. Ash vs. Alcalinity of Ash
plotting 3D figure for :  Alcohol vs. Ash vs. Magnesium
plotting 3D figure for :  Alcohol vs. Ash vs. Total Phenols
plotting 3D figure for :  Alcohol vs. Ash vs. Flavanoids
plotting 3D figure for :  Alcohol vs. Ash vs. Nonflavanoid Phenols
plotting 3D figure for :  Alcohol vs. Ash vs. Proanthocyanins
plotting 3D figure for :  Alcohol vs. Ash vs. Colour Intensity
plotting 3D figure for :  Alcohol vs. Ash vs. Hue
plotting 3D figure for :  Alcohol vs. Ash vs. OD280_OD315 of diluted wines
plotting 3D figure for :  Alcohol vs. Ash vs. Proline
plotting 3D figure for :  Alcohol vs. Alcalinity of Ash vs. Magnesium
plotting 3D figure for :  Alcohol vs. Alcalinity of Ash vs. Total Phenols
plotting 3D figure for :  Alcohol vs. Alcalinity of Ash vs. Flavanoids
plotting 3D figure for :  Alcohol vs. Alcalinity of Ash vs. Nonflavanoid Phenols
plotting 3D figure for :  Alcohol vs. Alcalinity of Ash vs. Proanthocyanins
plotting 3D figure for :  Alcohol vs. Alcalinity of Ash vs. Colour Intensity
plotting 3D figure for :  Alcohol vs. Alcalinity of Ash vs. Hue
plotting 3D figure for :  Alcohol vs. Alcalinity of Ash vs. OD280_OD315 of diluted wines
plotting 3D figure for :  Alcohol vs. Alcalinity of Ash vs. Proline
plotting 3D figure for :  Alcohol vs. Magnesium vs. Total Phenols
plotting 3D figure for :  Alcohol vs. Magnesium vs. Flavanoids
plotting 3D figure for :  Alcohol vs. Magnesium vs. Nonflavanoid Phenols
plotting 3D figure for :  Alcohol vs. Magnesium vs. Proanthocyanins
plotting 3D figure for :  Alcohol vs. Magnesium vs. Colour Intensity
plotting 3D figure for :  Alcohol vs. Magnesium vs. Hue
plotting 3D figure for :  Alcohol vs. Magnesium vs. OD280_OD315 of diluted wines
plotting 3D figure for :  Alcohol vs. Magnesium vs. Proline
plotting 3D figure for :  Alcohol vs. Total Phenols vs. Flavanoids
plotting 3D figure for :  Alcohol vs. Total Phenols vs. Nonflavanoid Phenols
plotting 3D figure for :  Alcohol vs. Total Phenols vs. Proanthocyanins
plotting 3D figure for :  Alcohol vs. Total Phenols vs. Colour Intensity
plotting 3D figure for :  Alcohol vs. Total Phenols vs. Hue
plotting 3D figure for :  Alcohol vs. Total Phenols vs. OD280_OD315 of diluted wines
plotting 3D figure for :  Alcohol vs. Total Phenols vs. Proline
plotting 3D figure for :  Alcohol vs. Flavanoids vs. Nonflavanoid Phenols
plotting 3D figure for :  Alcohol vs. Flavanoids vs. Proanthocyanins
plotting 3D figure for :  Alcohol vs. Flavanoids vs. Colour Intensity
plotting 3D figure for :  Alcohol vs. Flavanoids vs. Hue
plotting 3D figure for :  Alcohol vs. Flavanoids vs. OD280_OD315 of diluted wines
plotting 3D figure for :  Alcohol vs. Flavanoids vs. Proline
plotting 3D figure for :  Alcohol vs. Nonflavanoid Phenols vs. Proanthocyanins
plotting 3D figure for :  Alcohol vs. Nonflavanoid Phenols vs. Colour Intensity
plotting 3D figure for :  Alcohol vs. Nonflavanoid Phenols vs. Hue
plotting 3D figure for :  Alcohol vs. Nonflavanoid Phenols vs. OD280_OD315 of diluted wines
plotting 3D figure for :  Alcohol vs. Nonflavanoid Phenols vs. Proline
plotting 3D figure for :  Alcohol vs. Proanthocyanins vs. Colour Intensity
plotting 3D figure for :  Alcohol vs. Proanthocyanins vs. Hue
plotting 3D figure for :  Alcohol vs. Proanthocyanins vs. OD280_OD315 of diluted wines
plotting 3D figure for :  Alcohol vs. Proanthocyanins vs. Proline
plotting 3D figure for :  Alcohol vs. Colour Intensity vs. Hue
plotting 3D figure for :  Alcohol vs. Colour Intensity vs. OD280_OD315 of diluted wines
plotting 3D figure for :  Alcohol vs. Colour Intensity vs. Proline
plotting 3D figure for :  Alcohol vs. Hue vs. OD280_OD315 of diluted wines
plotting 3D figure for :  Alcohol vs. Hue vs. Proline
plotting 3D figure for :  Alcohol vs. OD280_OD315 of diluted wines vs. Proline
plotting 3D figure for :  Malic Acid vs. Ash vs. Alcalinity of Ash
plotting 3D figure for :  Malic Acid vs. Ash vs. Magnesium
plotting 3D figure for :  Malic Acid vs. Ash vs. Total Phenols
plotting 3D figure for :  Malic Acid vs. Ash vs. Flavanoids
plotting 3D figure for :  Malic Acid vs. Ash vs. Nonflavanoid Phenols
plotting 3D figure for :  Malic Acid vs. Ash vs. Proanthocyanins
plotting 3D figure for :  Malic Acid vs. Ash vs. Colour Intensity
plotting 3D figure for :  Malic Acid vs. Ash vs. Hue
plotting 3D figure for :  Malic Acid vs. Ash vs. OD280_OD315 of diluted wines
plotting 3D figure for :  Malic Acid vs. Ash vs. Proline
plotting 3D figure for :  Malic Acid vs. Alcalinity of Ash vs. Magnesium
plotting 3D figure for :  Malic Acid vs. Alcalinity of Ash vs. Total Phenols
plotting 3D figure for :  Malic Acid vs. Alcalinity of Ash vs. Flavanoids
plotting 3D figure for :  Malic Acid vs. Alcalinity of Ash vs. Nonflavanoid Phenols
plotting 3D figure for :  Malic Acid vs. Alcalinity of Ash vs. Proanthocyanins
plotting 3D figure for :  Malic Acid vs. Alcalinity of Ash vs. Colour Intensity
plotting 3D figure for :  Malic Acid vs. Alcalinity of Ash vs. Hue
plotting 3D figure for :  Malic Acid vs. Alcalinity of Ash vs. OD280_OD315 of diluted wines
plotting 3D figure for :  Malic Acid vs. Alcalinity of Ash vs. Proline
plotting 3D figure for :  Malic Acid vs. Magnesium vs. Total Phenols
plotting 3D figure for :  Malic Acid vs. Magnesium vs. Flavanoids
plotting 3D figure for :  Malic Acid vs. Magnesium vs. Nonflavanoid Phenols
plotting 3D figure for :  Malic Acid vs. Magnesium vs. Proanthocyanins
QObject::~QObject: Timers cannot be stopped from another thread


