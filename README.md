# Classification-of-Iris-Flowers
This is a machine learning project in python that classifies Iris flowers into the species type on the basis of their dimensions using K -nearest neighbors algorithm.
This is a basic Machine learning project in python that uses the K-Nearest Neighbour algorithm to classify Iris flowers into their respective species.
The dataset is got from a library in python.


**Requirements**

The basic requirements to run this program are:

=>Python 3.6.9

=>numpy-1.18.2

=>scikit-learn-0.22.2

=>scipy-1.4.1

**Description**

The dataset that we use for this program has a lot of data  samples of Iris flowers of the species Iris setosa, Iris virginica and Iris versicolor

The data we have in terms of:

Length of sepals

Width of sepals

Length of petals

Width of petals

**Working**

The program takes the dataset using the load_iris() function present in the sklearn that we imported in the beginning.
We split the dataset into training and testing parts for the respective purposes.
We then train our model using the KNN algorithm and then use the predict method to predict the model and give us the output.
