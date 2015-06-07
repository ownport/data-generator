# data-generator

Simple service for generating fake data

## Based on

- [joke2k/faker](https://github.com/joke2k/faker), the list of available [providers](http://fake-factory.readthedocs.org/en/master/providers.html)
- [Flask](http://flask.pocoo.org/)is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. 
- [YAML](http://pyyaml.org/) implementations for Python


## Sample request for generating data

```yaml
dataset: 
  name: test dataset #1
  description: Test dataset for testing Data Generator
  locale: en_US
  rows: 10

structure:

  - name: id
    type: fake.md5()

  - name: constant
    type: "10"

  - name: first_name
    type: fake.first_name()

  - name: last_name
    type: fake.last_name()

  - name: password
    type: fake.password(length=30, special_chars=True, digits=True, upper_case=True, lower_case=True)

  - name: address
    type: fake.address()
```

## Create Docker image

```
docker build -t 'data-generator' . 
```

## Run data generator in Docker

```
$ docker run -it --rm --name 'data-generator' -p 5000:5000 data-generator:latest python /data-generator/generator.py
 * Running on http://0.0.0.0:5000/
```

## Send request for new data

```sh
$ curl -F request=@data-request.yml http://localhost:8088/json
{"first_name": "Nira", "last_name": "Beahan", "constant": 10, "address": "03884 Brekke Falls\nCronamouth, CA 62399-0186", "password": "gEk3Y%uirXFyT(CgAf@XGrvdpmuz1n", "id": "9ee8c81e4c0c91fc6b6ea8f61d5464c9"}
{"first_name": "Sedrick", "last_name": "Stehr", "constant": 10, "address": "286 Sarina Greens Apt. 663\nHowellside, DE 07625-9946", "password": "3hBRxKhkXoeflT1gbe1BxFXT7EJG1y", "id": "b75f9176d35a63df01fe0466093ac332"}
{"first_name": "Gaither", "last_name": "Beatty", "constant": 10, "address": "199 Loy Corner Apt. 446\nJanechester, AS 66054-8331", "password": "z284q#wRTjJbXp5O#y!9)4TdDKls*g", "id": "90169de01c086617717cc68821968c3d"}
{"first_name": "April", "last_name": "Herman", "constant": 10, "address": "72253 Bradtke Field\nDonnellyberg, IA 36702-9808", "password": "evv6e@uEG1z0V+nlkXtyKsvhdPnsUB", "id": "c9ab3bb291d8648464430abef0e49e55"}
{"first_name": "Karlene", "last_name": "Ankunding", "constant": 10, "address": "0930 Maury Views\nNorth Jermain, DE 07224", "password": "K5odEpWlK5IgFoi_JG4y!5xHvjTFxl", "id": "037bbc9bb00d3b2b1bdde9e3511361d6"}
{"first_name": "Tamiko", "last_name": "McGlynn", "constant": 10, "address": "6385 Johnson Land\nWizamouth, CO 86544-4198", "password": "0K!vg^m4EZKzfFruO8T)0zh)q2pU_)", "id": "791ff5533e096f051b9fef9ac1c7b4fb"}
{"first_name": "Adah", "last_name": "Gutmann", "constant": 10, "address": "48725 Fadel Drive Suite 390\nNew Arnofurt, VT 86433", "password": "Q8lonLeXGrvp2Yrw&HN2yYAk(Cm%8E", "id": "f7ffaaf1877b10f27679ece782769695"}
{"first_name": "Asha", "last_name": "Fritsch", "constant": 10, "address": "58624 Trenton Locks Apt. 516\nNew Gustbury, DC 94703-7595", "password": "_%*GBqd_nn(0$OPqD&5YVJ8s7N8gXg", "id": "d81bfbcb8f004a04d941f21261593bbd"}
{"first_name": "Chelsey", "last_name": "Zieme", "constant": 10, "address": "825 Alison Island Suite 815\nHerzogland, OH 13773-1216", "password": "liRs+LhQZ$51i+GAPF*AGlKeiz^SW8", "id": "4cf1e4bbf5e8141fc4c61656467a5da6"}
{"first_name": "Carmel", "last_name": "Larkin", "constant": 10, "address": "6545 Troy Mission\nBernhardchester, VA 48754", "password": "ERejpUmE0^a1_7YuW@0PGNw8Mi3QI#", "id": "e0a73328810416f6c71244fff58e0896"}
$
```
