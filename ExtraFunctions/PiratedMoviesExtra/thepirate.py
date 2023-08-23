from pyYify import yify

m = yify.search_movies('logan')

for i in m:
  for j in i.image_links:
    print(f'image {i.title}:', j)
    print()
  print()
  print()
  print()

