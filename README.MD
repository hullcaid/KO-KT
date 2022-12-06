# Yhteenveto
Tämä on Jyväskylän Yliopiston IT-Tiedekunnan kurssille KYBS3050 Koneoppimismenetelmiä kyberturvallisuuteen tehty harjoitustyö.
Hrjoitustyön tehtävänanto:

#Ympärisön pystytys
- scikit-learn paketin asennus valmiiseen ympäristöön:
	$ conda config --add channels conda-forge
	$ conda config --set channel_priority strict
	$ conda install sciki-learn

- Vaihtoehtoisesti ympäristön pystytys suoraan:
	$ conda create -n sklearn-env -c conda-forge scikit-learn
	$ conda activate sklearn-env

# Viimeisin asennettu ympäristö
	$ conda create -n KO-scikit-learn -c conda-forge scikit-learn pandas jupyter 

#KDD-Prosessi
1. Datan lähde
2. Datavarasto
	Valmiin datasetin valinta
	Vaihtoehdot:
	1. Aposemat IoT-23 https://www.stratosphereips.org/datasets-iot23
		“Sebastian Garcia, Agustin Parmisano, & Maria Jose Erquiaga. (2020). IoT-23: A labeled dataset with malicious and benign IoT network traffic (Version 1.0.0) [Data set]. Zenodo. http://doi.org/10.5281/zenodo.4743746”
	2. Botnet dataset https://www.unb.ca/cic/datasets/botnet.html
3. Valittu data
4. Esiprosessoitu data
	Datan esiprosessointiin sovellettu yliang725 kirjoittamaa IoT23 - Data Preprocessing.ipynb: https://github.com/yliang725/Anomaly-Detection-IoT23/blob/main/Data%20Preprocessing/IoT23%20-%20Data%20Preprocessing.ipynb
		-Tiedostojen luku ja labeleiden muunto
5. Koneoppiminen, datan analysointi
6. Tulosten analysointi
7. Ymmärrys