# Deblurring
algorithm to deconvolute one-dimensional data using the Richardson-Lucy algorithm.
This algorithm takes in two inputs, the transfer matrix of the setup and the recorded data. It then uses the two inputs to display the results adjusted for noise as well as blurring.

Deblurring.ipynb can deconvolute the original step function exactly as expected because there is no noise.

deblurring with noise can be implemented to data that is suspected to have some sort of noise from it. Therefore, recorded data is not just a result of the transfer matrix but also a result of additional noise. This noise is important to note because depending on its size, the user may have to adjust the regularization weight and the number of iterations to minimize noise amplification.
