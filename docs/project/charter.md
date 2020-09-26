# Project Charter

## Business background

- Who is the client, what business domain the client is in.
  - RNS Ltd., is a UK-based online retailer of unique gift-ware. The company mainly
    sells their products to other businesses, wholesalers, in large batches.
- What business problems are we trying to address?
  - RNS Ltd., has decided to create a marketing division to promote their products
    and drive sales. However, they're **unaware of which customers
    they should focus their marketing efforts on**. Essentially they would like
    to segment their customer base, and **forecast the profitability of their
    customers**.

## Scope
- What data science solutions are we trying to build?
  - Time Series Forecasting (Predictive Modeling)
  - Unsupervised Machine Learning
- What will we do?
  - Clustering to determine market segments 
  - Time Series Forecasting and/or Deep Learning to forecast profitability
- How is it going to be consumed by the client?
  - Automated pipeline which continuously updates profitability forecasting
    and customer segments based on transaction data.

## Personnel
- Who are on this project:
	- XYZ Consultancy:
		- Project lead: Edward Amor
		- Data scientist(s): Edward Amor
	- Client:
		- Data administrator: John Doe
		- Business contact: Jane Doe
	
## Metrics
- What are the qualitative objectives? (e.g. reduce user churn)
  - Increase sales from marketing.
- What is a quantifiable metric  (e.g. reduce the fraction of users with 4-week inactivity)
  - Increase marketing sales to customers who are likely to be profitable.
- Quantify what improvement in the values of the metrics are useful for the customer scenario (e.g. reduce the fraction of users with 4-week inactivity by 20%)
  - Incrase marketing sales by 10% from the previous quarter(s) marketing sales volume
- What is the baseline (current) value of the metric? (e.g. current fraction of users with 4-week inactivity = 60%)
  - Currently 0% of purchases are generated through marketing.
- How will we measure the metric? (e.g. A/B test on a specified subset for a specified period; or comparison of performance after implementation to baseline)
  - Compare the historic average sales of a customer to the sales after marketing
    to determine the effect of marketing. 

## Plan
- Phases (milestones), timeline, short description of what we'll do in each phase.
  - Collection/Extraction
  - Cleaning
  - EDA
  - Feature Engineering
  - Segmenting/Clustering
    - k-means
    - Hierarchical clustering
  - Time Series Forecasting
    - Naive Modeling
    - ARIMA
    - Machine Learning
    - Deep Learning

## Architecture
- Data
  - What data do we expect? Raw data in the customer data sources (e.g. on-prem files, SQL, on-prem Hadoop etc.)
    - Initially excel files containing transaction data, but moving forward SQL database of transactions
- What tools and data storage/analytics resources will be used in the solution e.g.,
  - Python for feature construction, aggregation, sampling, modeling.
- How will the operationalized web service(s) be consumed in the business workflow of the customer? If applicable, write down pseudo code for the APIs of the web service calls.
  - How will the customer use the model results to make decisions
    - RNS Ltd., will utilize the model results to selectively market to customers.
  - Data movement pipeline in production
    - Transaction DB -> Pre-processing -> Modeling/Predictions/Clustering -> Dashboard
