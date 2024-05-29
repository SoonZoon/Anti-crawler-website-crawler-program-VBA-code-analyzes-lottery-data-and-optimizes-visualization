import pandas as pd
from selenium import webdriver
from io import StringIO
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
webdriver_service = Service()
driver = webdriver.Edge()
driver.get("http://")
def sync_data():
    while True:
        try:
            driver.refresh()
            time.sleep(5)
            def remove_duplicates_from_csv(file_path):
                df = pd.read_csv(file_path)
                df.drop_duplicates(inplace=True)
                df.to_csv(file_path, index=False)
            dfs = pd.read_html(StringIO(driver.page_source))
            dfs = [df.iloc[:, :9] for df in dfs]
            for i in range(len(dfs)):
                dfs[i] = dfs[i][~dfs[i].astype(str).apply(lambda row: row.str.contains('-').any(), axis=1)]
                dfs[i].to_csv("H:/caipiao/DTS/temp.csv", mode='a', index=False, header=False)
            remove_duplicates_from_csv("C:/temp.csv")
            print("Data synced successfully.")
        except Exception as e:
            print("An error occurred while syncing data: ", e)
        time.sleep(15)
        df = pd.read_csv("C:/temp.csv")
        df.fillna("X", inplace=True)
        df.to_csv("C:/temp.csv", index=False)
sync_data()