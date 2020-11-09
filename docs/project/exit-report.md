# Exit Report of Project *Marketing Analysis* for Customer *RNS Ltd.*

Customer: RNS Ltd.

Team Members: Edward Amor

## Overview

Unaware of which customers they should focus their marketing efforts on, we
were tasked with using clustering and classification to segment customers and
predict future customer value respectively. Clustering allowed us to identify
groupings for our customer base where we otherwise didn't have any. Whereas,
classification allowed us to predict the future value of a customer to our client
based on their transaction history.

## Business Domain

Our client RNS Ltd., is a UK-based online retailer of unique gift-ware. The company 
mainly sells their products to other businesses, wholesalers, in large batches.

## Business Problem

The problem RNS Ltd. faced was trouble bootstrapping their marketing department.
Since the department was still in its infancy they needed an analysis of their`
customer base, along with some way to identify who to market to in the future.
Identifying who your best customers are is vitally important because they provide
the majority of your revenue. 

> "20% of your customers generate 80% of the revenue".

## Data Processing

Original Dataset Schema:

InvoiceNo: Invoice number. Nominal. A 6-digit integral number uniquely assigned to 
each transaction. If this code starts with the letter 'c', it indicates a 
cancellation.
StockCode: Product (item) code. Nominal. A 5-digit integral number uniquely assigned 
to each distinct product.
Description: Product (item) name. Nominal.
Quantity: The quantities of each product (item) per transaction. Numeric.
InvoiceDate: Invice date and time. Numeric. The day and time when a transaction was 
generated.
UnitPrice: Unit price. Numeric. Product price per unit in sterling (Â£).
CustomerID: Customer number. Nominal. A 5-digit integral number uniquely assigned to 
each customer.
Country: Country name. Nominal. The name of the country where a customer resides.

Processing:

We take the transaction data, and transform it to create 3 distinct features aligning 
with the RFM marketing research structure. The result is a multivariate time series
which we use to train a classification algorithm.

Output Dataset Schema:

Output a 1 for a high priority customer, 0 for a low priority customer.

## Modeling, Validation

For modeling, we used a variety of classification algorithms, training them to assess
baseline what their results looked like. For testing validation, we split our dataset
into 5 partitions, maintaining the time dimensionality to prevent data leakage.

##	Benefits
	
###	Customer Benefit

This has an immense benefit for our client, as it gives them a clear direction to
begin marketing. By keeping our output binary and simple it also reduces confusion
on what type of customer they will be marketing to.

## Learnings

### Domain

One of the learnings from this project, was the various metrics use to evaluate
how much a customer is worth to a business. We used the standard market research metrics associated with RFM as they are domain standard.

###	What's unique about this project, specific challenges

Unique about this project is that we don't start with labels for our data and
instead have to generate them using clustering. Then based on our clustering we
perform predictive modeling. This means this is sort of a second order project
as it involves unsupervised along with supervised learning.

## Links

http://www.inderscience.com/offer.php?id=75325

## Next Steps
 
Our current model doesn't fully incorporate the time component. Overall I'd rate this project as a D in terms of value, it requires alot more analysis of the transaction history. Along with a better clustering, and predictive modeling scores.
