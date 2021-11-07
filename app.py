import streamlit as st
import pickle
from datetime import datetime
startTime = datetime.now()
# import znanych nam bibliotek

filename = "model.sv"
model = pickle.load(open(filename,'rb'))
# otwieramy wcześniej wytrenowany model

sex_d = {0:"Kobieta",1:"Mężczyzna"}
pclass_d = {0:"Pierwsza",1:"Druga", 2:"Trzecia"}
embarked_d = {0:"Cherbourg", 1:"Queenstown", 2:"Southampton"}
# o ile wcześniej kodowaliśmy nasze zmienne, to teraz wprowadzamy etykiety z ich nazewnictwem
def main():

	st.set_page_config(page_title="Czy będziesz zdrowy?")
	overview = st.container()
	left, right = st.columns(2)
	prediction = st.container()

	st.image("https://png.pngtree.com/png-vector/20191022/ourmid/pngtree-health-icon-isolated-on-abstract-background-png-image_1848040.jpg")

	with overview:
		st.title("Czy będziesz zdrowy?")


	with left:
		objawy_slider = st.slider("Objawy", value=3, min_value=1, max_value=5)
		wiek_slider = st.slider( "Wiek", min_value=11, max_value=77)
		choroby_slider = st.slider( "Choroby", min_value=1, max_value=5)
		wzrost = st.slider( "Wzrost", min_value=159, max_value=200, step=1)

	data = [[objawy_slider,wiek_slider , choroby_slider , wzrost]]
	health = model.predict(data)
	s_confidence = model.predict_proba(data)

	with prediction:
		st.header("Czy dana osoba będzie zdrowa? {0}".format("Tak" if health[0] == 0 else "Nie"))
		st.subheader("Pewność predykcji {0:.2f} %".format(s_confidence[0][health][0] * 100))

if __name__ == "__main__":
    main()

## Źródło danych [https://www.kaggle.com/c/titanic/](https://www.kaggle.com/c/titanic), zastosowanie przez Adama Ramblinga