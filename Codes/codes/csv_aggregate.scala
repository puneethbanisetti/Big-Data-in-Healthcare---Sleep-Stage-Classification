/*loading data from csv to aggregate*/
var PATH="ST7152J0-PSG.csv"

var df= spark.read.format("csv").option("header", "true").load(PATH)

df=df.selectExpr("cast(time as int) time","cast(val1 as float) val1","cast(val2 as float) val2","cast(val3 as float) val3","cast(val4 as float) val4","label")

df=df.select(df("time")/300 as "time",df("label"),df("val1"),df("val2"),df("val3"),df("val4"))

df=df.selectExpr("cast(time as int) time","cast(val1 as float) val1","cast(val2 as float) val2","cast(val3 as float) val3","cast(val4 as float) val4","label")

var df2 =df.groupBy("time").agg(collect_list("val1") as "val1",collect_list("val1") as "val2",collect_list("val3") as "val3",collect_list("val4") as "val4",first("label") as "labels")

df2=df2.selectExpr("time","cast(val1 as string) val1","cast(val2 as string) val2","cast(val3 as string) val3","cast(val4 as string) val4","labels")

df2.filter(df2("labels")==="Sleep stage W").count()

df2.repartition(1).write.option("header","true").csv("outpat1")