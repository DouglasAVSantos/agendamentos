import sqlite3
from datetime import datetime

municipes = [
    {
        "nome": "Samuel Thomas Gabriel da Rocha",
        "idade": 43,
        "cpf": "73778474090",
        "rg": "432136186",
        "data_nasc": "08/04/1979",
        "sexo": "Masculino",
        "signo": "Áries",
        "mae": "Hadassa Melissa",
        "pai": "Benício Rafael Raul da Rocha",
        "email": "samuel-darocha73@lanchesdahora.com.br",
        "senha": "T6ygiEP6zA",
        "cep": "54715200",
        "endereco": "Rua Julião Neto",
        "numero": 407,
        "bairro": "Penedo",
        "cidade": "São Lourenço da Mata",
        "estado": "PE",
        "telefone_fixo": "8137482197",
        "celular": "81987922159",
        "altura": "1,71",
        "peso": 66,
        "tipo_sanguineo": "A-",
        "cor": "preto"
    },
    {
        "nome": "Letícia Isabel Freitas",
        "idade": 38,
        "cpf": "33655223609",
        "rg": "465710554",
        "data_nasc": "19/01/1984",
        "sexo": "Feminino",
        "signo": "Capricórnio",
        "mae": "Camila Raimunda",
        "pai": "Arthur Gael Freitas",
        "email": "leticia-freitas74@hotelruby.com.br",
        "senha": "BHzkLs4eab",
        "cep": "68902356",
        "endereco": "Passagem Cleonice Santos Azevedo",
        "numero": 501,
        "bairro": "Muca",
        "cidade": "Macapá",
        "estado": "AP",
        "telefone_fixo": "9626075031",
        "celular": "96982372399",
        "altura": "1,62",
        "peso": 72,
        "tipo_sanguineo": "B-",
        "cor": "amarelo"
    },
    {
        "nome": "Jéssica Mariah da Paz",
        "idade": 22,
        "cpf": "16886320424",
        "rg": "323230994",
        "data_nasc": "03/02/2000",
        "sexo": "Feminino",
        "signo": "Aquário",
        "mae": "Bruna Analu Francisca",
        "pai": "Renato Sebastião da Paz",
        "email": "jessica_mariah_dapaz@mtc.eng.br",
        "senha": "f5LzB28ru0",
        "cep": "79902534",
        "endereco": "Travessa Guiné",
        "numero": 230,
        "bairro": "Jardim Jamaica",
        "cidade": "Ponta Porã",
        "estado": "MS",
        "telefone_fixo": "6738834560",
        "celular": "67992910186",
        "altura": "1,73",
        "peso": 76,
        "tipo_sanguineo": "B+",
        "cor": "azul"
    },
    {
        "nome": "Andreia Louise Priscila Souza",
        "idade": 32,
        "cpf": "00378780000",
        "rg": "371200581",
        "data_nasc": "21/04/1990",
        "sexo": "Feminino",
        "signo": "Touro",
        "mae": "Carolina Luana Larissa",
        "pai": "Calebe Anderson Souza",
        "email": "andreia-souza97@supercleanlav.com.br",
        "senha": "O33W7jW88G",
        "cep": "79602180",
        "endereco": "Rua Manoel Ferreira da Rocha",
        "numero": 162,
        "bairro": "Centro",
        "cidade": "Três Lagoas",
        "estado": "MS",
        "telefone_fixo": "6725186787",
        "celular": "67986094362",
        "altura": "1,75",
        "peso": 57,
        "tipo_sanguineo": "O-",
        "cor": "vermelho"
    },
    {
        "nome": "Danilo Gabriel Osvaldo da Cunha",
        "idade": 20,
        "cpf": "87488248104",
        "rg": "302643898",
        "data_nasc": "01/03/2002",
        "sexo": "Masculino",
        "signo": "Peixes",
        "mae": "Nina Mariane",
        "pai": "Pedro Benedito da Cunha",
        "email": "danilo-dacunha81@geniustyres.com.br",
        "senha": "qp06DRxysl",
        "cep": "68020554",
        "endereco": "Rua Curuauma",
        "numero": 414,
        "bairro": "Diamantino",
        "cidade": "Santarém",
        "estado": "PA",
        "telefone_fixo": "9326214985",
        "celular": "93988187363",
        "altura": "1,92",
        "peso": 58,
        "tipo_sanguineo": "B-",
        "cor": "vermelho"
    },
    {
        "nome": "Vitor Enrico Ryan Jesus",
        "idade": 29,
        "cpf": "89367023197",
        "rg": "198838578",
        "data_nasc": "08/01/1993",
        "sexo": "Masculino",
        "signo": "Capricórnio",
        "mae": "Ester Raquel",
        "pai": "Diego Rafael Cauê Jesus",
        "email": "vitor_enrico_jesus@trimempresas.com.br",
        "senha": "jgtcXyRSK4",
        "cep": "33170550",
        "endereco": "Rua Vinte e Dois",
        "numero": 354,
        "bairro": "Duquesa II (São Benedito)",
        "cidade": "Santa Luzia",
        "estado": "MG",
        "telefone_fixo": "3129366717",
        "celular": "31985476335",
        "altura": "1,95",
        "peso": 83,
        "tipo_sanguineo": "B-",
        "cor": "azul"
    },
    {
        "nome": "Patrícia Benedita Gomes",
        "idade": 57,
        "cpf": "55488678905",
        "rg": "481371485",
        "data_nasc": "22/02/1965",
        "sexo": "Feminino",
        "signo": "Peixes",
        "mae": "Andreia Laura Kamilly",
        "pai": "Sebastião Sebastião Fernando Gomes",
        "email": "patricia.benedita.gomes@agacapital.com.br",
        "senha": "5w5D5lobGh",
        "cep": "79041580",
        "endereco": "Avenida Coronel Ulisses de Lima",
        "numero": 515,
        "bairro": "Jardim São Lourenço",
        "cidade": "Campo Grande",
        "estado": "MS",
        "telefone_fixo": "6736335944",
        "celular": "67987185319",
        "altura": "1,65",
        "peso": 58,
        "tipo_sanguineo": "A-",
        "cor": "verde"
    },
    {
        "nome": "Igor Gael André Aragão",
        "idade": 76,
        "cpf": "96401785942",
        "rg": "153789815",
        "data_nasc": "27/01/1946",
        "sexo": "Masculino",
        "signo": "Aquário",
        "mae": "Sabrina Elisa Sophie",
        "pai": "Daniel Ricardo Pedro Aragão",
        "email": "igor.gael.aragao@panevale.com.br",
        "senha": "ZSoxRrw5L2",
        "cep": "33170490",
        "endereco": "Rua Dezesseis",
        "numero": 484,
        "bairro": "Duquesa II (São Benedito)",
        "cidade": "Santa Luzia",
        "estado": "MG",
        "telefone_fixo": "3138364255",
        "celular": "31999431935",
        "altura": "1,74",
        "peso": 110,
        "tipo_sanguineo": "AB-",
        "cor": "amarelo"
    },
    {
        "nome": "Geraldo Anderson Pereira",
        "idade": 26,
        "cpf": "64856766430",
        "rg": "223547797",
        "data_nasc": "22/02/1996",
        "sexo": "Masculino",
        "signo": "Peixes",
        "mae": "Vitória Hadassa",
        "pai": "Pedro Victor Pereira",
        "email": "geraldo_pereira@fiorecomunicacao.com.br",
        "senha": "KaGhMLLqDw",
        "cep": "22750450",
        "endereco": "Rua Almirante Mário Franca",
        "numero": 830,
        "bairro": "Anil",
        "cidade": "Rio de Janeiro",
        "estado": "RJ",
        "telefone_fixo": "2127877752",
        "celular": "21981469138",
        "altura": "1,96",
        "peso": 87,
        "tipo_sanguineo": "A+",
        "cor": "roxo"
    },
    {
        "nome": "Bernardo Guilherme Levi das Neves",
        "idade": 20,
        "cpf": "96103187974",
        "rg": "443784723",
        "data_nasc": "25/03/2002",
        "sexo": "Masculino",
        "signo": "Áries",
        "mae": "Luana Emanuelly Daiane",
        "pai": "Bryan Martin das Neves",
        "email": "bernardo_dasneves@gm.com",
        "senha": "d9p0cmuIt1",
        "cep": "69306375",
        "endereco": "Rua Wai-Wai",
        "numero": 805,
        "bairro": "Nossa Senhora Aparecida",
        "cidade": "Boa Vista",
        "estado": "RR",
        "telefone_fixo": "9528213366",
        "celular": "95987228298",
        "altura": "1,61",
        "peso": 95,
        "tipo_sanguineo": "A-",
        "cor": "amarelo"
    },
    {
        "nome": "Rita Catarina Julia Pires",
        "idade": 28,
        "cpf": "24542391167",
        "rg": "487978547",
        "data_nasc": "22/03/1994",
        "sexo": "Feminino",
        "signo": "Áries",
        "mae": "Agatha Fabiana Luana",
        "pai": "Gustavo João Luan Pires",
        "email": "ritacatarinapires@asproplastic.com.br",
        "senha": "CFEz61FaYe",
        "cep": "49090129",
        "endereco": "Rua J",
        "numero": 768,
        "bairro": "Bugio",
        "cidade": "Aracaju",
        "estado": "SE",
        "telefone_fixo": "7925112347",
        "celular": "79985366291",
        "altura": "1,66",
        "peso": 59,
        "tipo_sanguineo": "O+",
        "cor": "roxo"
    },
    {
        "nome": "Diego Benjamin Tiago Melo",
        "idade": 41,
        "cpf": "57654697449",
        "rg": "136342048",
        "data_nasc": "09/01/1981",
        "sexo": "Masculino",
        "signo": "Capricórnio",
        "mae": "Nina Sônia Raquel",
        "pai": "Roberto Pietro Márcio Melo",
        "email": "diego.benjamin.melo@arysta.com.br",
        "senha": "QjG4w7ahmA",
        "cep": "69911846",
        "endereco": "Rua Turiba",
        "numero": 410,
        "bairro": "Ayrton Sena",
        "cidade": "Rio Branco",
        "estado": "AC",
        "telefone_fixo": "6827548843",
        "celular": "68985945470",
        "altura": "2,00",
        "peso": 70,
        "tipo_sanguineo": "O+",
        "cor": "vermelho"
    },
    {
        "nome": "Mateus Osvaldo Ian Ramos",
        "idade": 80,
        "cpf": "43503632387",
        "rg": "215079048",
        "data_nasc": "10/03/1942",
        "sexo": "Masculino",
        "signo": "Peixes",
        "mae": "Sophia Tereza Vanessa",
        "pai": "Francisco Ryan Ramos",
        "email": "mateus.osvaldo.ramos@vmetaiscba.com.br",
        "senha": "T6Cz0GRKrX",
        "cep": "32185180",
        "endereco": "Rua Duque de Caxias",
        "numero": 124,
        "bairro": "Nacional",
        "cidade": "Contagem",
        "estado": "MG",
        "telefone_fixo": "3128544567",
        "celular": "31992520997",
        "altura": "1,89",
        "peso": 93,
        "tipo_sanguineo": "O+",
        "cor": "preto"
    },
    {
        "nome": "Clara Clara Luzia Rodrigues",
        "idade": 78,
        "cpf": "98841628596",
        "rg": "187481088",
        "data_nasc": "01/02/1944",
        "sexo": "Feminino",
        "signo": "Aquário",
        "mae": "Isis Carolina Giovana",
        "pai": "Cláudio Gabriel Rodrigues",
        "email": "claraclararodrigues@accor.com.br",
        "senha": "wPAgXecKX4",
        "cep": "29160661",
        "endereco": "Alameda Periquito",
        "numero": 703,
        "bairro": "Alphaville Jacuhy",
        "cidade": "Serra",
        "estado": "ES",
        "telefone_fixo": "2735950928",
        "celular": "27984934827",
        "altura": "1,52",
        "peso": 53,
        "tipo_sanguineo": "A-",
        "cor": "azul"
    },
    {
        "nome": "Eduardo Oliver Nicolas Araújo",
        "idade": 32,
        "cpf": "77890721960",
        "rg": "464152264",
        "data_nasc": "26/03/1990",
        "sexo": "Masculino",
        "signo": "Áries",
        "mae": "Valentina Heloisa Antonella",
        "pai": "Luiz Miguel Araújo",
        "email": "eduardo_araujo@estagiarios.com",
        "senha": "Tl5tzUgiLe",
        "cep": "58038332",
        "endereco": "Travessa São Gonçalo",
        "numero": 530,
        "bairro": "Manaíra",
        "cidade": "João Pessoa",
        "estado": "PB",
        "telefone_fixo": "8328781236",
        "celular": "83997299130",
        "altura": "1,64",
        "peso": 76,
        "tipo_sanguineo": "AB-",
        "cor": "preto"
    },
    {
        "nome": "Iago Renato Severino da Rosa",
        "idade": 26,
        "cpf": "15885654832",
        "rg": "436163883",
        "data_nasc": "26/02/1996",
        "sexo": "Masculino",
        "signo": "Peixes",
        "mae": "Cecília Luiza Gabriela",
        "pai": "Renan Nelson da Rosa",
        "email": "iago_darosa@mcexecutiva.com.br",
        "senha": "o4HQSdb3TP",
        "cep": "75073520",
        "endereco": "Rua 1",
        "numero": 359,
        "bairro": "Chácaras Colorado",
        "cidade": "Anápolis",
        "estado": "GO",
        "telefone_fixo": "6235050488",
        "celular": "62995672882",
        "altura": "1,90",
        "peso": 55,
        "tipo_sanguineo": "O+",
        "cor": "preto"
    },
    {
        "nome": "Amanda Malu Melissa Silva",
        "idade": 33,
        "cpf": "61001899687",
        "rg": "237698432",
        "data_nasc": "21/04/1989",
        "sexo": "Feminino",
        "signo": "Touro",
        "mae": "Sebastiana Heloisa",
        "pai": "Giovanni Marcos Silva",
        "email": "amanda.malu.silva@lnaa.com.br",
        "senha": "qnCcezHo0L",
        "cep": "49043150",
        "endereco": "Rua Sargento Antônio da Silva Vieira",
        "numero": 737,
        "bairro": "São Conrado",
        "cidade": "Aracaju",
        "estado": "SE",
        "telefone_fixo": "7938080379",
        "celular": "79983606227",
        "altura": "1,64",
        "peso": 88,
        "tipo_sanguineo": "AB-",
        "cor": "azul"
    },
    {
        "nome": "Patrícia Betina Viana",
        "idade": 39,
        "cpf": "25206888664",
        "rg": "141840419",
        "data_nasc": "17/02/1983",
        "sexo": "Feminino",
        "signo": "Aquário",
        "mae": "Mariana Luana",
        "pai": "Gabriel Kauê Lucas Viana",
        "email": "patricia.betina.viana@vemarbrasil.com.br",
        "senha": "nHrzJcDprG",
        "cep": "49048350",
        "endereco": "Rua Sílvio Fontes",
        "numero": 793,
        "bairro": "Luzia",
        "cidade": "Aracaju",
        "estado": "SE",
        "telefone_fixo": "7939399728",
        "celular": "79989367176",
        "altura": "1,79",
        "peso": 50,
        "tipo_sanguineo": "A+",
        "cor": "vermelho"
    },
    {
        "nome": "Simone Benedita Isabella da Cruz",
        "idade": 26,
        "cpf": "90026038510",
        "rg": "442973068",
        "data_nasc": "17/01/1996",
        "sexo": "Feminino",
        "signo": "Capricórnio",
        "mae": "Sophia Laura",
        "pai": "Elias Theo da Cruz",
        "email": "simone_dacruz@aprimor.com",
        "senha": "uIoDciBcjQ",
        "cep": "68901460",
        "endereco": "Rua André de Oliveira Costa",
        "numero": 222,
        "bairro": "Santa Inês",
        "cidade": "Macapá",
        "estado": "AP",
        "telefone_fixo": "9627048823",
        "celular": "96994617628",
        "altura": "1,63",
        "peso": 69,
        "tipo_sanguineo": "O-",
        "cor": "amarelo"
    },
    {
        "nome": "Alessandra Analu Valentina Ferreira",
        "idade": 31,
        "cpf": "78872493099",
        "rg": "376453564",
        "data_nasc": "03/04/1991",
        "sexo": "Feminino",
        "signo": "Áries",
        "mae": "Teresinha Mariana",
        "pai": "Gustavo Caleb Ferreira",
        "email": "alessandraanaluferreira@budsoncorporation.com",
        "senha": "phZT3sBrlt",
        "cep": "88330816",
        "endereco": "Rua 1801",
        "numero": 926,
        "bairro": "Centro",
        "cidade": "Balneário Camboriú",
        "estado": "SC",
        "telefone_fixo": "4736266519",
        "celular": "47997548737",
        "altura": "1,81",
        "peso": 86,
        "tipo_sanguineo": "B+",
        "cor": "amarelo"
    },
    {
        "nome": "José Nicolas Teixeira",
        "idade": 39,
        "cpf": "47644224254",
        "rg": "291478864",
        "data_nasc": "12/04/1983",
        "sexo": "Masculino",
        "signo": "Áries",
        "mae": "Isabella Alana Analu",
        "pai": "Lucca Francisco Emanuel Teixeira",
        "email": "jose-teixeira84@etep.edu.br",
        "senha": "4onDihgUIA",
        "cep": "69918062",
        "endereco": "Rua Carmópolis",
        "numero": 125,
        "bairro": "Abraão Alab",
        "cidade": "Rio Branco",
        "estado": "AC",
        "telefone_fixo": "6838433836",
        "celular": "68995734431",
        "altura": "1,60",
        "peso": 91,
        "tipo_sanguineo": "B+",
        "cor": "azul"
    },
    {
        "nome": "Patrícia Larissa Ribeiro",
        "idade": 20,
        "cpf": "73767994275",
        "rg": "184622281",
        "data_nasc": "08/01/2002",
        "sexo": "Feminino",
        "signo": "Capricórnio",
        "mae": "Julia Juliana",
        "pai": "Márcio Fábio Ribeiro",
        "email": "patricia_larissa_ribeiro@delboux.com.br",
        "senha": "DzxfDgSaQ6",
        "cep": "70238010",
        "endereco": "Quadra SQS 404 Bloco A",
        "numero": 112,
        "bairro": "Asa Sul",
        "cidade": "Brasília",
        "estado": "DF",
        "telefone_fixo": "6137743749",
        "celular": "61983904115",
        "altura": "1,58",
        "peso": 85,
        "tipo_sanguineo": "AB+",
        "cor": "preto"
    },
    {
        "nome": "Isabella Rebeca Brito",
        "idade": 47,
        "cpf": "70333752988",
        "rg": "289975232",
        "data_nasc": "26/01/1975",
        "sexo": "Feminino",
        "signo": "Aquário",
        "mae": "Sophia Mariana Adriana",
        "pai": "Breno Lorenzo Brito",
        "email": "isabella.rebeca.brito@akaer.com.br",
        "senha": "WLkWs2JuLd",
        "cep": "54520640",
        "endereco": "Rua Benedito Lopes da Silva",
        "numero": 863,
        "bairro": "Nossa Senhora do Rosário",
        "cidade": "Cabo de Santo Agostinho",
        "estado": "PE",
        "telefone_fixo": "8135430552",
        "celular": "81996048971",
        "altura": "1,61",
        "peso": 59,
        "tipo_sanguineo": "B-",
        "cor": "vermelho"
    },
    {
        "nome": "Milena Priscila Fátima Corte Real",
        "idade": 46,
        "cpf": "99771280228",
        "rg": "192460468",
        "data_nasc": "24/03/1976",
        "sexo": "Feminino",
        "signo": "Áries",
        "mae": "Jennifer Mariana",
        "pai": "Ian Yago Corte Real",
        "email": "milena_cortereal@plastic.com.br",
        "senha": "efSth3rcnb",
        "cep": "59617230",
        "endereco": "Rua Luiz Guilherme",
        "numero": 826,
        "bairro": "Abolição",
        "cidade": "Mossoró",
        "estado": "RN",
        "telefone_fixo": "8429283442",
        "celular": "84983172400",
        "altura": "1,81",
        "peso": 58,
        "tipo_sanguineo": "AB-",
        "cor": "verde"
    },
    {
        "nome": "Isabela Clara Barbosa",
        "idade": 60,
        "cpf": "79966430083",
        "rg": "484541791",
        "data_nasc": "08/04/1962",
        "sexo": "Feminino",
        "signo": "Áries",
        "mae": "Luciana Fátima",
        "pai": "Davi Luan Filipe Barbosa",
        "email": "isabela_clara_barbosa@audiogeni.com.br",
        "senha": "lIXETy0Oxf",
        "cep": "58057240",
        "endereco": "Rua Portuário Anésio Gomes da Silva",
        "numero": 927,
        "bairro": "Mangabeira",
        "cidade": "João Pessoa",
        "estado": "PB",
        "telefone_fixo": "8326639262",
        "celular": "83985125244",
        "altura": "1,81",
        "peso": 55,
        "tipo_sanguineo": "O-",
        "cor": "preto"
    },
    {
        "nome": "Natália Fernanda Moura",
        "idade": 18,
        "cpf": "54537385618",
        "rg": "254911559",
        "data_nasc": "07/02/2004",
        "sexo": "Feminino",
        "signo": "Aquário",
        "mae": "Evelyn Marcela Alessandra",
        "pai": "Jorge Breno Augusto Moura",
        "email": "nataliafernandamoura@msds.com.br",
        "senha": "G6ilGTJj3i",
        "cep": "49040800",
        "endereco": "Rua Pedro Lisboa",
        "numero": 435,
        "bairro": "Inácio Barbosa",
        "cidade": "Aracaju",
        "estado": "SE",
        "telefone_fixo": "7937868890",
        "celular": "79988632291",
        "altura": "1,83",
        "peso": 70,
        "tipo_sanguineo": "O-",
        "cor": "roxo"
    },
    {
        "nome": "Liz Sebastiana Gabriela Peixoto",
        "idade": 38,
        "cpf": "81576801748",
        "rg": "465479376",
        "data_nasc": "04/01/1984",
        "sexo": "Feminino",
        "signo": "Capricórnio",
        "mae": "Isabelly Carolina Sophia",
        "pai": "Alexandre Marcos Vinicius Murilo Peixoto",
        "email": "lizsebastianapeixoto@vpsa.com.br",
        "senha": "MUstRrlYQX",
        "cep": "77825782",
        "endereco": "Rua Xambioá",
        "numero": 319,
        "bairro": "Vila Norte",
        "cidade": "Araguaína",
        "estado": "TO",
        "telefone_fixo": "6336160427",
        "celular": "63998378208",
        "altura": "1,83",
        "peso": 54,
        "tipo_sanguineo": "A-",
        "cor": "roxo"
    },
    {
        "nome": "Igor Marcelo Ryan Bernardes",
        "idade": 46,
        "cpf": "41471513459",
        "rg": "277947376",
        "data_nasc": "18/04/1976",
        "sexo": "Masculino",
        "signo": "Áries",
        "mae": "Manuela Jéssica Tereza",
        "pai": "Eduardo João Cauã Bernardes",
        "email": "igor-bernardes71@kof.com.mx",
        "senha": "42drllGsB3",
        "cep": "96508190",
        "endereco": "Rua Gaspar Francisco Gonçalves",
        "numero": 460,
        "bairro": "Marques Ribeiro",
        "cidade": "Cachoeira do Sul",
        "estado": "RS",
        "telefone_fixo": "5128431943",
        "celular": "51985033840",
        "altura": "1,64",
        "peso": 101,
        "tipo_sanguineo": "A-",
        "cor": "vermelho"
    },
    {
        "nome": "Heloisa Ayla Luana Nogueira",
        "idade": 29,
        "cpf": "10518379523",
        "rg": "175638913",
        "data_nasc": "06/03/1993",
        "sexo": "Feminino",
        "signo": "Peixes",
        "mae": "Gabriela Pietra Stefany",
        "pai": "Noah Julio Nogueira",
        "email": "heloisa_nogueira@alemponte.com.br",
        "senha": "Uwh4oSEozQ",
        "cep": "69044786",
        "endereco": "Travessa Severo Gomes",
        "numero": 638,
        "bairro": "Planalto",
        "cidade": "Manaus",
        "estado": "AM",
        "telefone_fixo": "9237422454",
        "celular": "92992220253",
        "altura": "1,61",
        "peso": 57,
        "tipo_sanguineo": "AB+",
        "cor": "vermelho"
    },
    {
        "nome": "Alessandra Flávia Rafaela Fogaça",
        "idade": 28,
        "cpf": "90458710768",
        "rg": "292786967",
        "data_nasc": "13/02/1994",
        "sexo": "Feminino",
        "signo": "Aquário",
        "mae": "Mariana Carolina",
        "pai": "Benedito Pedro Marcos Fogaça",
        "email": "alessandra.flavia.fogaca@johndeere.com",
        "senha": "663NnQJnsu",
        "cep": "65901340",
        "endereco": "Rua Aquiles Lisboa",
        "numero": 950,
        "bairro": "Mercadinho",
        "cidade": "Imperatriz",
        "estado": "MA",
        "telefone_fixo": "9839551678",
        "celular": "98984593474",
        "altura": "1,54",
        "peso": 81,
        "tipo_sanguineo": "AB+",
        "cor": "vermelho"
    }
]


class DataBase():
    def __init__(self, nome='system.db'):
        self.nome = nome

    def conect_db(self):
        self.conection = sqlite3.connect(self.nome)

    def close_db(self):
        try:
            self.conection.close()
        except:
            pass

    def create_table_municipes(self):
        try:
            cursor = self.conection.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS municipes (
            NOME TEXT NOT NULL,
            RG TEXT NOT NULL,
            CPF TEXT PRIMARY KEY,
            DATA_DE_NASCIMENTO TEXT NOT NULL,
            TELEFONE TEXT NOT NULL,
            INSTITUIÇÃO TEXT NULL,
            CEP TEXT NOT NULL,
            ENDEREÇO TEXT NOT NULL,
            NUMERO TEXT NOT NULL,
            BAIRRO TEXT NOT NULL,
            CIDADE TEXT NOT NULL
            );
            ''')
        except:
            print('erro ao criar a tabela municipes')

    def create_table_users(self):
        try:
            c = self.conection.cursor()
            c.execute("""
                CREATE TABLE IF NOT EXISTS users(
                LOGIN TEXT NOT NULL,
                USER TEXT UNIQUE,
                SENHA TEXT NOT NULL,
                ACESS TEXT NOT NULL
                );""")
        except AttributeError:
            print('erro ao criar a tabela')

    def create_table_agendamentos(self):
        # try:
            cursor = self.conection.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS agendamentos(
            DATA TEXT NOT NULL,
            Horario_08h30 TEXT NULL,
            Horario_09h30 TEXT NULL,
            Horario_10h30 TEXT NULL,
            Horario_11h30 TEXT NULL,
            Horario_12h30 TEXT NULL,
            Horario_13h30 TEXT NULL,
            Horario_14h30 TEXT NULL,
            Horario_15h30 TEXT NULL,
            Horario_16h30 TEXT NULL);
            ''')
        # except:


    def check_table_municipes(self):
        cursor = self.conection
        table = cursor.execute('SELECT * FROM municipes')
        for linha in table.fetchall(): print(linha)

    def insert_municipes(self, nome, rg, cpf, data, telefone, cep, endereco, numero, bairro, cidade, instituicao=''):
        try:
            cursor = self.conection.cursor()
            cursor.execute(f'''
            INSERT INTO municipes (NOME, RG, CPF, DATA_DE_NASCIMENTO,TELEFONE, INSTITUIÇÃO, CEP, ENDEREÇO, NUMERO, BAIRRO, CIDADE) VALUES ('{nome}', '{rg}', '{cpf}', '{data}','{telefone}', '{instituicao}', '{cep}', '{endereco}','{numero}','{bairro}','{cidade}');
            ''')
            self.conection.commit()
        except:
            print('faça a conexao')

    def check_table_users(self):
        cursor = self.conection.cursor()
        cursor.execute('SELECT * FROM users;')
        for linha in cursor.fetchall(): print(linha)

    def insert_novo_usuario(self, login,user, senha, acess='user'):
        try:
            cursor = self.conection.cursor()
            cursor.execute(f'''
                INSERT INTO users(login,user, senha, acess) VALUES('{login}','{user}','{senha}','{acess}');
            ''')
            self.conection.commit()
        except AttributeError:
            print('faça a conexão')

    def delete_user(self,usuario):
         try:
            self.usuario = usuario
            cursor = self.conection.cursor()
            cursor.execute(f'Delete from users where user = "{self.usuario}"')
            self.conection.commit()
         except:
             print('faça a conexão')

    def db_check_user_admin(self, login, senha):
         try:
            cursor = self.conection.cursor()
            cursor.execute('''
            SELECT * FROM users;
            ''')
            for linha in cursor.fetchall():
                if linha[0]== login and linha[2]== senha and linha[3] == 'admin':
                    return 'admin'
                elif linha[0]== login and linha[2]== senha and linha[3] == 'user':
                    return 'user'
            return False

         except Exception:
            return False

    def check_login_exists(self,login,senha):
        try:
            cursor = self.conection.cursor()
            cursor.execute('''
           SELECT * FROM users;
           ''')
            for linha in cursor.fetchall():
                if linha[0] == login and linha[2] == senha:
                    return True
                else:
                    continue
            return False

        except Exception:
            print('faça a conexão')

    def check_user_exists(self,user):
        try:
            cursor = self.conection.cursor()
            cursor.execute('''
           SELECT * FROM users;
           ''')
            for linha in cursor.fetchall():
                if linha[1] == user:
                    return True
                else:
                    continue
            return False

        except Exception:
            print('faça a conexão')


if __name__ == '__main__':
    db = DataBase()
    db.conect_db()
    db.create_table_municipes()
    db.create_table_users()
    db.create_table_agendamentos()
    db.insert_novo_usuario('douglas', 'doug_avs', '123', 'admin')
    db.insert_novo_usuario('gabriela', 'gabs', '123', )
    print('tabela municipes')
    for x in municipes: db.insert_municipes(x['nome'],x['rg'],x['cpf'],x['data_nasc'],x['celular'],x['cep'],x['endereco'],x['numero'],x['bairro'],x['cidade'])
    db.check_table_municipes()
    print('tabela usuarios')
    db.check_table_users()
    db.close_db()
