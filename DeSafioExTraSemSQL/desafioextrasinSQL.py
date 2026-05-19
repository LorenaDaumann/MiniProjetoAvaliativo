# O estudante deverá utilizar a base de dados pública do Titanic, em formato CSV, com o
# objetivo de realizar uma Análise Exploratória de Dados (AED). A atividade consiste em
# importar, organizar e analisar o conjunto de dados, buscando compreender o
# comportamento geral das informações e identificar padrões, relações entre variáveis e
# possíveis fatores associados à sobrevivência dos passageiros. A partir desse processo,
# espera-se a obtenção de insights relevantes, como estatísticas descritivas, distribuições,
# comparações entre grupos e análises exploratórias das variáveis disponíveis.
# A base de dados pública do Titanic, em formato CSV, está disponível neste endereço
# eletrônico: https://drive.google.com/file/d/11HptTxJbUMRG16xpC39fcliba_-Z_J9d/

# tamanho máximo de 20 MB, contendo todos os arquivos
# necessários para o funcionamento do projeto, incluindo: código-fonte, conjunto de dados
# utilizado, insights extraídos e arquivo de documentação.

# A análise deverá envolver a compreensão das variáveis, a aplicação de filtros, ordenações e
# agrupamentos (GroupBy), bem como a construção de pelo menos uma visualização gráfica
# que represente a distribuição dos dados ou a relação entre variáveis relevantes, utilizando a
# linguagem Python e bibliotecas adequadas ao contexto da análise exploratória.

# Todas as informações do projeto deverão estar claramente documentadas em um arquivo
# de texto, que poderá estar nos formatos .txt, .doc, .docx, .pdf ou README.md, e que deverá
# ser incluído dentro da pasta compactada juntamente com o código da aplicação. A
# documentação deverá apresentar a descrição das etapas realizadas, as principais decisões
# tomadas durante o tratamento dos dados e os principais insights obtidos a partir da análise
# exploratória. Caso o aluno deseje, o código também poderá ser versionado no GitHub, desde
# que o arquivo compactado submetido na tarefa contenha todos os arquivos necessários para
# a avaliação



#IMPORTANDO AS BIBLIOTECAS

import pandas as pd
import matplotlib.pyplot as plt

#carregando o conjunto de dados do titanic   
df = pd.read_csv("/home/lorena/Documentos/ATIVIDADES-SCTEC/DeSafioExTraSemSQL/titanic_dataset.csv")

# try:
#     with engine.begin() as conn:
#         df.to_sql('titanic', conn, if_exists='replace', index=False)

#         query = 'SELECT "Sex", AVG("Survived") AS taxa FROM titanic GROUP BY "Sex";'
#         df_sql = pd.read_sql(query, conn)

#     print(df_sql)
# except SQLAlchemyError as err:
#     print("Erro ao acessar o banco de dados PostgreSQL:", err)
#     raise


#olhando os dados
print("Dados do Titanic(cabeça):")
print(df.head())
print("\n")
print("Informações do DataFrame:")
print(df.info())
print("\n")
print("Estatísticas Descritivas:")
print(df.describe())
print("\n")



#ORGANIZAÇÃO  DOS DADOS
print("Tratar os valores vazios/tirar-los:")
nulls = df.isnull().sum()

print("\nValores faltantes:")
print(nulls[nulls > 0])
print("\n")



#ANALISE EXPLORATÓRIA DE DADOS
print("Sobreviventes e não sobreviventes:", df['Survived'].mean())
taxa = df['Survived'].mean()
print(f"Taxa geral de sobrevivência: {taxa:.2%}")
print("\n")

print("Sobrevivência por classe:")
print(df.groupby(['Survived', 'Pclass']).size())
print("\n")


print("Sobreviventes por sexo:")
print(df.groupby(['Survived', 'Sex']).size())
mulheres = df[df['Sex'] == 'female']['Survived'].mean()

#sobrevivenciaa por idade
df['AgeGroup'] = pd.cut(df['Age'], bins=[0,12,18,35,60,100]) #bins -dividir valores numéricos em grupos/faixas.

print("Média de sobrevivência por grupo de idade:")
print(df.groupby('AgeGroup', observed=False)['Survived'].mean()) #observed=False - inclui todas as categorias, mesmo as que nao tem dados
print("\n")


#quem tinha cabine e quem nao tinha
df['HasCabin'] = df['Cabin'].notnull()

print("Tem cabine X Não tem:")
print(df.groupby('HasCabin')['Survived'].mean())
print("\n")





#VIZUALIZAÇÃO
#sobrevivente e mortos
survived_counts = df['Survived'].value_counts()

plt.figure()
plt.bar(survived_counts.index, survived_counts, color=['red', 'green'])
plt.title("Sobreviventes vs Mortos")
plt.xlabel("0 = Morto | 1 = Sobreviveu")
plt.ylabel("Quantidade")

plt.savefig("grafico_sobreviventes.png")
plt.show()
input("Pressione Enter para fechar o gráfico e continuar...")
plt.close()

#sobrevivencia por classe
class_survival = df.groupby('Pclass')['Survived'].mean()

plt.figure()
class_survival.plot(kind='bar')
plt.title("Taxa de sobrevivência por classe")
plt.xlabel("Classe")
plt.ylabel("Taxa de sobrevivência")

plt.savefig("grafico_classe.png")
plt.show()
input("Pressione Enter para fechar o gráfico e continuar...")
plt.close()

#sobrevivencia por genero
sex_survival = df.groupby('Sex')['Survived'].mean()

plt.figure()
sex_survival.plot(kind='bar', color=['skyblue', 'salmon'])
plt.title("Taxa de sobrevivência por gênero")
plt.xlabel("Sexo")
plt.ylabel("Taxa de sobrevivência")

plt.savefig("grafico_sexo.png")
plt.show()
input("Pressione Enter para fechar o gráfico e continuar...")
plt.close()

#sobrevivencia por idade
age_survival = df.groupby('AgeGroup', observed=False)['Survived'].mean()

plt.figure()
age_survival.plot(kind='bar') #define o tipo de grafico :D
plt.title("Sobrevivência por faixa etária")
plt.xlabel("Faixa de idade")
plt.ylabel("Taxa de sobrevivência")

plt.savefig("grafico_idade.png")
plt.show()
input("Pressione Enter para fechar o gráfico e continuar...")
plt.close()


#cabine e (chances de)sobrevivencia
cabin_survival = df.groupby('HasCabin')['Survived'].mean()

plt.figure()
cabin_survival.plot(kind='bar', color=['#FFA56E', '#FF6E6E'])
plt.title("Sobrevivência: Possui cabine ou não")
plt.xlabel("False = Não | True = Sim")
plt.ylabel("Taxa de sobrevivência")
 


#APRESENTAR OS GRÁFICOS E SALVAR AS IMAGENS
plt.savefig("grafico_cabine.png")
plt.show()
input("Pressione Enter para fechar o gráfico e continuar...")
plt.close()

print("\n=== INSIGHTS PRINCIPAIS ===")
print("Análise completa! Gráficos salvos: grafico_sobreviventes.png, grafico_classe.png, etc.")
print("Taxa geral de sobrevivência:", f"{taxa:.2%}")
print(f"Mulheres tiveram {mulheres:.2%} chance de sobreviver (vs homens).")
print("1ª classe: alta sobrevivência, 3ª classe: baixa.")

