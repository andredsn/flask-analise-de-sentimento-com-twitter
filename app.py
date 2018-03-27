from flask import Flask, render_template
from analise_sentimento import calcularClasses, calcularPercentualTotal, main, getDataFrame

# instancia o objeto flask
app = Flask(__name__)

# cria a rota para o index
@app.route("/")
def index():
    
    # chama a função que inicia o programa (back end)
    main()
    
    # pega o dataframe criado já com a última classificação após a busca no twitter
    df =getDataFrame()
    
    # pega a quantidade de tweets classsificados como inseguros, seguros e neutros
    quantidade=calcularClasses(df)
    
    # pega o percentual de tweets classsificados como inseguros, seguros e neutros
    percentual=calcularPercentualTotal(df)
    
    # pega o texto e classe do último tweet classificado
    texto=df['texto'].tail(1).values
    sentimento=df['sentimento'].tail(1).values
    
    # renderiza no template os dados buscados
    return render_template("index.html", quantidade=quantidade, percentual=percentual, total=len(df), texto=texto[0], sentimento=sentimento[0])

#inicia o servidor flask
app.run(debug=True, use_reloader=True)