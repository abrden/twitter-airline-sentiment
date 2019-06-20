import csv
import subprocess
import re

bashCommand = 'java -jar fastSentimentClassifier.jar '

with open('TweetsAirlines_Test.csv', newline='') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
  dict = {}
  for row in spamreader:
    if len(row) == 3:
      airline_sentiment = row[0]
      airline = row[1]
      text = row[2].replace('"','\\"')

      if not airline in dict:
        dict[airline] = {
          'positive': 0,
          'negative': 0,
          'positive_value': float(0),
          'negative_value': float(0),
          'hits': 0,
          'misses': 0,
          'entries': 0
        }

      cmd = (bashCommand + '"' + text + '"')
      output = subprocess.check_output(['bash', '-c', cmd])
      output = output.decode('utf-8')

      polarity = re.search(r'polarity: (.*);', output).group(1)
      value = re.search(r'value=(.*)\n?', output).group(1)
      dict[airline][polarity] += 1
      dict[airline][polarity + '_value'] += float(value)
      dict[airline]['entries'] += 1
      if polarity == airline_sentiment:
        dict[airline]['hits'] += 1
      else:
        dict[airline]['misses'] += 1

  for k, v in dict.items():
    print('----------------------')
    print(k)
    print('positive: ' + str(v['positive']))
    print('negative: ' + str(v['negative']))
    print('positive value: ' + str(v['positive_value']))
    print('negative value: ' + str(v['negative_value']))
    print('entries: ' + str(v['entries']))
    print('hits: ' + str(v['hits']))
    print('misses: ' + str(v['misses']))


