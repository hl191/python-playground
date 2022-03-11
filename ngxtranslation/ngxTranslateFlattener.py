import re

json_flatten_delimiter = '.'


def unflatten(json):
  result = {}
  for key, value in json.items():
    s = result
    # Regex Word: matches alphanumeric and underscore
    tokens = re.findall(r'[^' + json_flatten_delimiter + ']+', key)
    for count, (index, next_token) in enumerate(
      zip(tokens, tokens[1:] + [value]), 1):
      value = next_token if count == len(
        tokens) else [] if next_token.isdigit() else {}
      if isinstance(s, list):
        index = int(index)
        while index >= len(s):
          s.append(value)
      elif index not in s:
        s[index] = value
      s = s[index]
  return result


def flatten(json):
  out = {}

  def flatten(x, name=''):
    if type(x) is dict:
      for a in x:
        flatten(x[a], name + a + json_flatten_delimiter)
    elif type(x) is list:
      i = 0
      for a in x:
        flatten(a, name + str(i) + json_flatten_delimiter)
        i += 1
    else:
      out[name[:-1]] = x

  flatten(json)
  return out
