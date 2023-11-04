"""SimpleApp.py"""
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.functions import avg
import pandas as pd
from pyspark.sql.functions import col, explode, posexplode, collect_list, monotonically_increasing_id
#https://medium.com/bluekiri/check-your-pyspark-abilities-by-solving-this-quick-challenge-86f563a343dd

#replace filight numbers with name

spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
trips = pd.DataFrame({
    "origin": [
        "PMI",
        "ATH",
        "JFK",
        "HND"
    ],
    "destination": [
        "OPO",
        "BCN",
        "MAD",
        "LAX"
    ],
    "internal_flight_ids": [
        [2, 1],
        [3],
        [5, 4, 6],
        [8, 9, 7, 0]
    ]
})
trips = spark.createDataFrame(trips)
flights = pd.DataFrame({
    "internal_flight_id": [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    ],
    "public_flight_number": [
        "FR5763", "UT9586", "B4325", "RW35675", "LP656",
        "NB4321", "CX4599", "AZ8844", "KH8851", "OP8777"
    ]
})
flights = spark.createDataFrame(flights)
# add addiitonal ocl with flight ids mapped ot names
trips = trips \
    .withColumn("row_id", monotonically_increasing_id())
exploded = trips \
    .select(col("row_id"),
            explode(col("internal_flight_ids")) \
               .alias("internal_flight_id"))
exploded_with_flight_number= exploded.join(flights, exploded.row_id == flights.internal_flight_id,'inner')
collected = exploded_with_flight_number \
    .groupBy("row_id") \
    .agg(collect_list("public_flight_number") \
        .alias("public_flight_numbers"))
trips_with_flight_numbers = collected \
    .join(trips, on="row_id") \
    .drop("row_id") \
    .drop("internal_flight_ids")
#trips_with_flight_numbers.show()
# this is wrong since explode messes up the order  so use
#collected.show()

spark.stop()
