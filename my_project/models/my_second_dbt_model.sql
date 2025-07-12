-- models/my_second_dbt_model.sql

select 
    "Media Path",
    "Date",
    "Message",
    "ID",
    "Channel Username",
    "Channel Title"
from {{ ref('my_first_dbt_model') }}  -- Reference the first model
