# data-generator

Command line tool for generating fake data


## Sample request for generating data

```yaml
dataset: 
  name: test dataset #1
  description: Test dataset for testing Data Generator
  locale: en_US
  headers: true
  delimiter: \001
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
$ docker run -it --rm --name 'data-generator' -p 8088:5000 data-generator:latest python /data-generator/generator.py
 * Running on http://0.0.0.0:5000/
```

## Send request for new data

```sh
curl -F request=@data-request.yml http://localhost:5000/json
```
