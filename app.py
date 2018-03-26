from flask import Flask, render_template
from analise_sentimento import calcularClasses, lerCSV, calcularPercentualTotal, main

# instancia o objeto flask
app = Flask(__name__)

# cria a rota para o index
@app.route("/")
def index():
    
    # chama a função que inicia o programa (back end)
    main()
    
    # ler o arquivo com twets
    df=lerCSV("tweets_classificados")
    
    # pega a quantidade de tweets classsificados como inseguros, seguros e neutros
    quantidade=calcularClasses(df)
    
    # pega o percentual de tweets classsificados como inseguros, seguros e neutros
    percentual=calcularPercentualTotal(df)
    
    # renderiza no template os dados buscados
    return render_template("index.html", quantidade=quantidade, percentual=percentual)

#inicia o servidor flask
app.run(debug=True, use_reloader=True)