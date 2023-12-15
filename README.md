# DGMR.be
Implementing the DGMR model as a nowcasting solution over Belgium.
___

data: RMI radar data

context: Maastricht Science Program - Bachelor Thesis Research

In a previous study by Ravuri et al., DGMR has been showed to perform better than pySTEPS and some other nowcasting solutions. This study was run with radar precipitation data from the United Kingdom that was used to train and test the model, and a test run using data from the United States (Ravuri et al., 2021). 

The aim of this project will be to see how DGMR performs when tasked with the prediction of particular events over Belgium, like the floods of 2021 for example. Here, a particular event would be a period of heavy rainfall, as these are the most important for the model to predict accurately for it to be a viable nowcasting solution
(Ravuri et al., 2021). The direct adaptation of a pre-trained model to a different context is not a given, it is possible that DGMR learns implicit effects of the U.K.s’ landscape on the evolution of precipitation which will then wrongly affect the models’ forecasts over Belgium. The data used will be radar precipitation data, more precisely quantitative precipitation estimate (QPE) values mapped over Belgium, made available by the Royal Meteorological Institute (RMI) of Belgium for the context of this project.

# Citation 
___
    '''
    author={Suman Ravuri and Karel Lenc and Matthew Willson and Dmitry Kangin and Remi Lam and Piotr Mirowski and Megan Fitzsimons and Maria Athanassiadou and Sheleem Kashem and Sam Madge and Rachel Prudden Amol Mandhane and Aidan Clark and Andrew Brock and Karen Simonyan and Raia Hadsell and Niall Robinson Ellen Clancy and Alberto Arribas† and Shakir Mohamed},
    title={Skillful Precipitation Nowcasting using Deep Generative Models of Radar},
    journal={Nature},
    volume={597},
    pages={672--677},
    year={2021}
    }
    '''
link: https://www.nature.com/articles/s41586-021-03854-z