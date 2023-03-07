import chartmogul

# Set up your ChartMogul API key
config = chartmogul.Config('YOUR-API-KEY-HERE')

# Just to test if everything is working properly. Followed the instructions provided in https://github.com/chartmogul/chartmogul-python
# We should get a "Pong". :)
chartmogul.Ping.ping(config).get()

# Set the date range for which you want to retrieve the MRR data. Two ranges will be setup, one for Q1 and another until April.
start_date = "2019-01-01"
end_date = "2019-04-30"
end_q1_date = "2019-03-31"

# Retrieve the MRR data using ChartMogul's Metrics API. More info is provided in https://dev.chartmogul.com/reference/retrieve-mrr
mrr = chartmogul.Metrics.mrr(
    config=config,
    start_date=start_date,
    end_date=end_date,
    interval="month"
).get()

# Retrieve the MRR data using ChartMogul's Metrics API. More info is provided in https://dev.chartmogul.com/reference/retrieve-mrr
mrrQ1 = chartmogul.Metrics.mrr(
    config=config,
    start_date=start_date,
    end_date=end_q1_date,
    interval="month"
).get()

# Calculate the total MRR for Q1 2019. The result is divided by 100 because values are in cents.
total_mrr = sum(entry.mrr for entry in mrrQ1.entries) / 100

# Print the total MRR for Q1 2019 (using f-strings for better readability)
print(f'Total MRR for Q1 2019: ${total_mrr}\n')

# Extracting and printing the MRR value for each month. The result is divided by 100 because values are in cents.
# Using the strftime function to extract the month name from the datetime object.
for entry in mrr.entries:
    month_mrr = entry.mrr / 100
    month_name = entry.date.strftime("%B")
    print(f'{month_name}: ${month_mrr}')
