from django import template


register = template.Library()

cens = ['Конь', 'Редис', 'Пупа']

# входящая value -это строка, делишь ее сплитом,
# получаешь список слов, затем применяя к каждому слову
# ловер сравниваешь (ищешь) его в цензорном списке,
# если совпадает реплейс на звездочки
#
# получившееся склеиваешь обратно в строку и возвращаешь
@register.filter()
def censor(word):
   if isinstance(word, str):
      for i in word.split():
         if i.capitalize() in cens:
               word = word.replace(i, i[0] + '*' * len(i))
   else:
      raise ValueError(
         'custom_filters -> censor -> A string is expected, but a different data type has been entered')
   return word

# @register.filter
# def hide_forbidden(value):
#     words = value.split()
#     result = []
#     for word in words:
#         if word in forbidden_words:
#             result.append(word[0] + "*"*(len(word)-2) + word[-1])
#         else:
#             result.append(word)
#     return " ".join(result)