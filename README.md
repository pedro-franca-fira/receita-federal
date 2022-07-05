# API RECEITA FEDERAL = CPF/CNPJ/PF

<h2> CNPJ </h2>

1. Consumimos o endpoint `/consulta/cnpj/[cnpj]`

    <ul>
      <li>OBS: <strong>CNPJ</strong> deve conter 14 digitos</li>
    </ul>
  
2. Depois é inserido em 3 tables as informações retornadas da API

    <ul> <h2>Tables</h2>
    <li> <strong>QSA</strong> tabela relacionada a sócios da empresa</li>
    <li><strong>info_empresa</strong> tabela relacionada a informações gerais da empresa</li>
    <li><strong>atividades_secundarias</strong> tabela relacionada a atividades secundarias a empresa</li>
    </ul>
