# DGMR.be
Implementing the DGMR model as a nowcasting solution over Belgium.

data: RMI radar data

context: Maastricht Science Program - Bachelor Thesis Research

In a previous study by Ravuri et al., DGMR has been showed to perform better than
pySTEPS and some other nowcasting solutions. This study was run with radar precipitation data
from the United Kingdom that was used to train and test the model, and a test run using data
from the United States (Ravuri et al., 2021). The aim of this project will be to see how DGMR
performs when tasked with the prediction of particular events over Belgium, like the floods of
2021 for example. Here, a particular event would be a period of heavy rainfall, as these are the
most important for the model to predict accurately for it to be a viable nowcasting solution
(Ravuri et al., 2021). The direct adaptation of a pre-trained model to a different context is not a
given, it is possible that DGMR learns implicit effects of the U.K.s’ landscape on the evolution
of precipitation which will then wrongly affect the models’ forecasts over Belgium. The data
used will be radar precipitation data, more precisely quantitative precipitation estimate (QPE)
values mapped over Belgium, made available by the Royal Meteorological Institute (RMI) of
Belgium for the context of this project.

Ravuri, S., Lenc, K., Willson, M., Kangin, D., Lam, R., Mirowski, P., Fitzsimons, M.,
Athanassiadou, M., Kashem, S., Madge, S., Prudden, R., Mandhane, A., Clark, A.,
Brock, A., Simonyan, K., Hadsell, R., Robinson, N., Clancy, E., Arribas, A., &amp;
Mohamed, S. (2021). Skilful precipitation nowcasting using deep generative models of
radar. Nature, 597(7878), 672–677. https://doi.org/10.1038/s41586-021-03854-z