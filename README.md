## mindsdb

### Collecting data
Iris dataset
```bash
wget -o data/iris.csv https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv
```

### Results
#### Iris dataset
**Training**
```bash
python scripts/iris.py --type train
```
**Prediction**

Example 1
```bash
python scripts/iris.py --type predict --sepal_length 5.1 --sepal_width 3.5 --petal_length 1.4 --petal_width 0.2

# The predicted species is virginica with confidence 0.5066882912471576 => incorrect
```

Example 2
```bash
python scripts/iris.py --type predict --sepal_length 5.1 --sepal_width 3.5 --petal_length 1.4 --petal_width 0.2

# The predicted species is versicolor with confidence 0.5066882912471576 => correct but low confidence
```