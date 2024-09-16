# Databricks notebook source
print("this is my first notebook")

# COMMAND ----------

# MAGIC %md
# MAGIC ## sample sql query
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT CONCAT('today''s date is ', current_date()) sysdate

# COMMAND ----------

# MAGIC %md
# MAGIC ## sample sql query - date format
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT CONCAT('today''s date is ', current_date()) , 
# MAGIC date_format(current_date(),'dd-MMM-yyyy') 

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup-05

# COMMAND ----------

# MAGIC %run /Workspace/Users/labuser7596433@vocareum.com/get-started-with-data-engineering-on-databricks-2.1.1/Includes/Classroom-Setup-05

# COMMAND ----------

print(f"Username:             {DA.username}")
print(f"Catalog Name:         {DA.catalog_name}")
print(f"Schema Name:          {DA.schema_name}")
print(f"Working Directory:    {DA.paths.working_dir}")
print(f"Dataset Location:     {DA.paths.datasets}")
