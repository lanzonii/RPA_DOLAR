from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.chrome.options import Options
import psycopg2

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.google.com/finance/quote/USD-BRL?sa=X&ved=2ahUKEwjv5IbThvSEAxXCBbkGHXTxAMEQmY0JegQIBhAv')
valor = driver.find_element(By.CLASS_NAME, 'YMlKec.fxKbKc')
valor = valor.text
driver.quit()
data = str(datetime.now()).split(' ')[0]
hora = str(datetime.now()).split(' ')[1].split('.')[0]
cotacao = float(valor.replace(',', '.'))


# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="dbcotacoes",
    user="postgres",
    password="1234",
    host="localhost"
)

# Create a cursor
cur = conn.cursor()

# Call the stored procedure with parameters
comando = "CALL INSERIR_TABELA(%s, %s, %s)"
args = (data, hora, cotacao)

# Execute the procedure
cur.execute(comando, args)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()