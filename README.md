# CoF-Intro2R: Homework 3

In this activity, you will practice using some of the data cleaning/wrangling functions we learned about in class. This starter repository includes three datasets, `Data/site_coords.csv`, `Data/trout.csv`, and `giant_salamanders.csv`. These all come from a public dataset from the [HJ Andrews Experimental Forest](https://andrewsforest.oregonstate.edu/) that can be accessed using the `lterdatasampler` R package. However, these are much "messier" versions of those datasets that require your data wrangling skills to whip them into shape before we can do much with them. Follow the steps below to complete the data wrangling for these data.

## Instructions

1. Create an R script called `R/hw3.R`. At the top of your script, load the `tidyverse` library.

2. Load each of the datasets into the environment using the `read_csv()` function from package `readr`. Be sure to use the "double-colon" syntax when calling the `here()` function from package `here`.

3. First, combine the trout data and giant salamander data into one dataset in *long format*. Name the resulting dataframe `verts` (for vertebrates).

4. Merge the sampling site location data into the long dataset.

    i. Notice that the `site_coords.csv` data has a site code in the `site` column. The other datasets do not have this column, but do have all the necessary information to create it. Construct a new column in the `verts` dataframe called `site` that combines the string `"MACK"` with the `section` and `reach` information such that the two datasets can be merged. *Hint: The `paste()` function may come in handy for this.*

    ii. Once your columns look like they match, use the `left_join()` function from `dplyr` to merge the two datasets. **Note that your final dataset should have the same number of rows as `verts` did before the merge.**
    
5. Now, let's clean up some of the data. First, notice the column names. There are spaces, parentheses, and a mixture of capital and lowercase letters. Your objective is to remove all spaces and replace them with an underscore (`"_"`), remove all parentheses, and convert all letters to lowercase. *Hint: the `tolower()` function will come in handy.*

6. Finally, let's clean up some of the data columns that have spaces or are in a less useful format. Specifically, remove all the spaces from the species names in the `species` column, replacing them with underscores, and convert all the letters to lowercase. Then, convert the `sample_date` column to class `date` with format `ymd` (year, month, day) using the `lubridate` package.

7. Save your cleaned dataset as `Data/hja_verts_cleaned.csv` using `write_csv()`. 




