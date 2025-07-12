-- models/transformed_cleaned_data.sql

WITH aggregated_data AS (
    SELECT
        "Channel Username",
        DATE("Date") AS message_date,
        COUNT(*) AS message_count,
        STRING_AGG("Message", ', ') AS all_messages
    FROM
        {{ source('my_source', 'cleaned_data') }}  -- Ensure this matches the source name
    GROUP BY
        "Channel Username",
        DATE("Date")
)

SELECT
    "Channel Username",
    message_date,
    message_count,
    all_messages
FROM
    aggregated_data
ORDER BY
    "Channel Username", message_date
