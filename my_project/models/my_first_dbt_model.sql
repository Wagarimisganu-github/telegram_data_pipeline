-- models/example/my_first_dbt_model.sql

SELECT
    "Media Path",
    "Date",
    "Message",
    "ID",
    "Channel Username",
    "Channel Title"
FROM
    {{ source('my_source', 'cleaned_data') }}  -- Reference the source here
