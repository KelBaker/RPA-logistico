import random 
from config.settings import * 
import pandas as pd

def gerar_codigo():
    return "789" + "".join(str(random.randint(0,9)) for _ in range(10))

def gerar_excel(valor_maximo, qtd_max_produtos=300):
    total = 0
    produtos = []

    while total < valor_maximo and len(produtos) < qtd_max_produtos:
        valor_unit = round(random.uniform(VALOR_UNIT_MIN, VALOR_UNIT_MAX), 2)
        estoque = random.randint(ESTOQUE_MIN, ESTOQUE_MAX)
        valor_produto = valor_unit * estoque

        if total + valor_produto > valor_maximo:
            estoque = int((valor_maximo - total) / valor_unit)
            if estoque <= 0:
                break 
            valor_produto = valor_unit * estoque

        produtos.append({
            "codigo_produto": gerar_codigo(),
            "descricao": "Produto gerado",
            "estoque_atual": f"[estoque] un",
            "valor_unit": valor_unit
        })

        total += valor_produto

    df = pd.DataFrame(produtos)
    df.to_excel("excel/estoque_gerado.xlsx", index=False)

    print(f"Excel gerado com valor total aproximado: R$ {round(total,2)}")