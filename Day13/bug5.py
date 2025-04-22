word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: ")) #here added == but it check for equality, you need to assign by =
total_words = pages * word_per_page
print(total_words)
