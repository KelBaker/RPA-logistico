import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def extrair_unidade(texto):
    return int(re.search(r"\d+", texto).group())

def rodar_rpa():
    df = pd.read_excel("excel/estoque_gerado.xlsx")

    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000")

    for _, row in df.iterrows():
        quantidade = extrair_unidade(row["estoque_atual"])

        driver.find_element(By.ID, "codigo_produto").send_keys(row["codigo_produto"])
        driver.find_element(By.ID, "quantidade").send_keys(str(quantidade))
        driver.find_element(By.ID, "btn_confirmar").click()

        time.sleep(0.2)

    driver.quit()
