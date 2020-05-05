/*aggregating all files for exploratory data analysis*/

var df= spark.read.format("csv").option("header", "true").load("patdata/*.csv")

println("Total data points are-")

println(df.count())

println("Total data points classified as Wake are-")
println(df.filter(df("labels")==="Sleep stage W").count())

println("Total data points classified as stage 1 are-")
println(df.filter(df("labels")==="Sleep stage 1").count())

println("Total data points classified as stage 2 are-")
println(df.filter(df("labels")==="Sleep stage 2").count())

println("Total data points classified as stage 3 are-")
println(df.filter(df("labels")==="Sleep stage 3").count())

println("Total data points classified as stage 4 are-")
println(df.filter(df("labels")==="Sleep stage 4").count

println("Total data points classified as stage R are-")
println(df.filter(df("labels")==="Sleep stage R").count())