## Content Based Movie Recommender Engine
Movie Recommender Engine using Machine learning.

## Documentation
This repository contains the code for building movie recommendation engine.

### About Dataset
All the information related to dataset is the below.
## Dataset
* we have used TMDB 5000 Movie Dataset in order to build movie recommendation Engine.
* you need to download the dataset [this link](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).
* Put dataset inside `input_data` folder.

### Dataset Details
In my Case Study, I have investigated a dataset containing information about 10,000 movies collected from The Movie Database (TMDb).

I downloaded the TMDB 5000 Movie Dataset which is divided into two parts tmdb_5000_Credits and tmdb_5000_Movies and we saved it as ‘Credits.csv’, ‘Movies.csv’.

In this project, I will provide various visualizations to identify patterns in the data.

* The data are contained in the following files.
```
tmdb_5000_credits.csv
tmdb_5000_movies.csv
```

## Movies Dataset having following columns
* budget
* genres
* homepage
* id
* keywords
* original_language
* original_title
* overview
* popularity
* production_companies
* production_countries
* release_date
* revenue
* runtime
* spoken_languages
* status
* tagline
* title
* vote_average
* vote_count

### after sorting movies dataset details
* genres
* keyword
* id
* title
* overview

## Credit dataset
* movie_id
* title
* cast
* crew


More details about the contents and use of all these files is given in README.txt


## Dependencies
* Python >=3.5
* pandas
* numpy
* pickle
* pillow
* lottie
* requests
* webbroswer
* scikit-learn
* scikit-surprise
* heroku
* streamlit
* pycharm
* jupyter notebook
* jupyter lab
* visual Studio Code

![alt text](https://github.com/mahak-dev/Movie-Recommender-Engine/blob/main/graph.jpeg)
![alt text](https://github.com/mahak-dev/Movie-Recommender-Engine/blob/main/architect.jpeg)

### Dataset Approach

This project is divided into two parts:

The Story of Film: This section aims at narrating the history, trivia and facts behind the world of cinema through the lens of data. Casts, Crews, Budgets, etc. through the years. Through the two models, we also aim at discovering what features have the most significant impact in determining revenue and success.

Movie Recommender Systems: This part is focused around building various kinds of recommendation engines; namely the Simple Generic Recommender, the Content Based Filter and the User Based Filter. 

My Approach
Data Collection: Data was collected from the MovieLens website and through a script that queried for data from various TMDB Endpoints.
Data Wrangling: The datasets were uploaded to a dataframe and explored. Null values were filled in wherever appropriate and polluted values were discarded or wrangled.
EDA: Extensive data visualisation and summary statistics were used to extract insights and pattern from the various datasets. The history, facts and trivia behind movies were narrated through data.
Machine Learning: Gradient Boosting Classifer and Regressor were trained on our feature engineered dataset to predict movie success and revenue respectively. Their feature importances were noted to gain insights into what factors influence the revenues of a movie relative to budget.
Recommendation Systems: Four different recommendation systems were built using various ideas and algorithms such as IMDB's Weighted Rating, Content Based Filtering and Collaborative Filtering.


A Gradient Boosting Regressor and Classifier were built in Jupyter to predict Movie Revenue and Success respectively with a Score of 0.78 and 0.8 respectively.
In addition, four recommendation engines were built based on different ideas and algorithms:

Simple Recommender: The IMDB Weighted Rating System was used to calculate ratings on which the sorting was finally performed.                       
   Hybrid Engine: I brought together ideas from content and collaborative filtering to build an engine that gave movie suggestions to a particular user based on the estimated ratings that it had internally calculated for that user.
   
   ----
   ### Here is the Project link 
[Profile](https://mahak-gupta.herokuapp.com/).
[Project](https://mrs-engine.herokuapp.com/).
