import pyspark.sql.functions as sf
from pyspark.sql import DataFrame
from pyspark.sql.types import DecimalType


PRODUCTS_MAPPING = {
"pk":	            "ProductKey",
"psck":	            "ProductSubCategoryKey",
"name":	            "ProductName",
"stancost":	        "StandardCost",
"dealerprice":	    "DealerPrice",
"listprice":	    "ListPrice",
"color":	        "Color",
"size":	            "Size",
"range":	        "SizeRange",
"weight":	        "Weight",
"nameofmodel":	    "ModelName",
"ssl":	            "SafetyStockLevel",
"desc":	            "Description",

}


def get_products(products_raw: DataFrame) -> DataFrame:
    """Transform and filter Products data.

    1. Selecting needed columns, and cast data types.
    2. Apply the column name mapping.
    3. Create "ProfitMargin"
    4. Replace "NA" value with None.
    5. Drop duplicates.

    :param products_raw:   Raw Products data
    :return:                Cleaned, filtered, and transformed Products data.
    """

    return (
        products_raw
        .select(
            sf.col("pk").cast("int"),
            sf.col("psck").cast("int"),
            sf.col("name"),
            sf.col("stancost").cast(DecimalType(10,2)).alias("stancost"),
            sf.col("dealerprice").cast(DecimalType(10,2)).alias("dealerprice"),
            sf.col("listprice").cast("int").cast(DecimalType(10,2)).alias("listprice"),
            sf.col("color"),
            sf.col("size").cast("int"),
            sf.col("range"),
            sf.col("weight").cast("int").cast(DecimalType(10,2)).alias("weight"),
            sf.col("nameofmodel"),
            sf.col("ssl").cast("int"),
            sf.col("desc")
        )
        .withColumnsRenamed(PRODUCTS_MAPPING)
        .withColumn("ProfitMargin",sf.col("ListPrice") - sf.col("DealerPrice"))
        .replace("NA",None)
        .dropDuplicates()
    )
