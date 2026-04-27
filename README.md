# ENVS231 PM2.5 Python Practical

Welcome to the ENVS231 PM2.5 Python practical.

In this practical you will use Python in Google Colab to analyse three anonymous PM2.5 air pollution datasets. You will calculate summary statistics, create a figure using Python code, and write a short interpretation of your results.

PM2.5 means particulate matter with a diameter of 2.5 micrometres or smaller. In this practical, PM2.5 concentration is measured in micrograms per cubic metre, written as µg/m³.

---

## What you will do

You will:

1. Open the Google Colab notebook.
2. Enter your student ID.
3. Load your three anonymous PM2.5 datasets.
4. Calculate statistics for each dataset.
5. Write Python code to create a figure.
6. Submit your answers through Microsoft Forms.

The datasets are anonymous. You will not know the monitoring locations.

---

## Open the notebook

Use the Colab link provided on Canvas.

The notebook will start by loading the data using:

```python
datetime, dat1, dat2, dat3 = make_data(student_id)
```

This gives you:

```python
datetime
dat1
dat2
dat3
```

`datetime` is the time axis.

`dat1`, `dat2` and `dat3` are your three anonymous PM2.5 datasets.

---

## What you need to submit

Everything is submitted through Microsoft Forms.

You will submit:

1. Your student ID and name.
2. Statistics for Dataset 1.
3. Statistics for Dataset 2.
4. Statistics for Dataset 3.
5. The Python code used to create your figure.
6. A short interpretation essay.

You do not need to upload the raw data.

---

## Statistics to calculate

For each of the three datasets, calculate:

1. Mean
2. Standard deviation
3. Median
4. Maximum
5. Minimum
6. Variance
7. Modal bin count using 9 equal-width bins
8. Modal bin midpoint using 9 equal-width bins
9. 5th percentile
10. 95th percentile

Enter values to 3 decimal places where appropriate.

---

## Modal bin explanation

The modal bin is not exactly the same as the normal mode.

PM2.5 is continuous data, so exact repeated values are not always meaningful. Instead, you will divide the data into bins and find the bin with the highest count.

For this practical:

- use 9 equal-width bins;
- the bins should span from the minimum PM2.5 value to the maximum PM2.5 value;
- the modal bin count is the number of values in the busiest bin;
- the modal bin midpoint is halfway between the two edges of that bin.

The notebook includes a worked example using simple data.

---

## Figure task

You need to write Python code that creates one figure containing:

- three PM2.5 time series plots;
- three PM2.5 histograms;
- clear titles;
- axis labels with units;
- a mean line on each time series plot;
- mean + 1 standard deviation line;
- mean - 1 standard deviation line;
- legends where appropriate.

You will upload the code used to create the figure to Microsoft Forms.

---

## Interpretation essay

Write 250 to 300 words comparing your three anonymous PM2.5 datasets.

Your answer should:

- identify which dataset has the highest typical PM2.5 concentration;
- identify which dataset is most variable;
- identify which dataset shows the strongest evidence of short-lived pollution episodes;
- compare the histogram shapes;
- use at least four numerical values from your own statistics;
- suggest plausible environmental or meteorological explanations;
- explain one limitation of interpreting anonymous datasets without site metadata.

Do not claim to know the monitoring location.

For example, avoid statements such as:

> Dataset 1 is next to a motorway.

Instead, use careful wording such as:

> Dataset 1 has a higher maximum and wider spread, which could suggest short-lived pollution episodes. However, without location metadata, the source cannot be confirmed.

---

## AI policy

You may use AI tools to help with coding or debugging.

You must not use AI tools to write the interpretation essay.

The interpretation essay must be your own writing.

---

## What to submit in Microsoft Forms

Submit:

```text
Student ID
Full name

Dataset 1 statistics
Dataset 2 statistics
Dataset 3 statistics

Figure code upload

Blind interpretation essay
Academic declaration
```

The academic declaration confirms that your interpretation essay is your own writing.

---

## Tips

Check that:

- your student ID is entered correctly;
- you use your own datasets;
- your statistics are entered to 3 decimal places;
- your figure code creates all six required plots;
- your axes include units;
- your essay uses numbers from your own results;
- your essay does not invent locations or sources.

---

## Final reminder

The aim of the practical is not just to get the right numbers.

The aim is to learn how to use Python to explore real environmental data, create clear figures, and interpret what the data show while recognising what cannot be known from anonymous data alone.
