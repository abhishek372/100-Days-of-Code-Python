# Fix the error

# pages = 0
# words_per_page = 0
# pages = int(input("Number of pages: "))
# words_per_page == int(input("Number of words per page: "))
# total_words = pages * words_per_page
# print(total_words)


# In line 6, we are checking with words_per_page which gives False which is not of any use

# Correct code
pages = 0
words_per_page = 0
pages = int(input("Number of pages: "))
words_per_page = int(input("Number of words per page: "))
total_words = pages * words_per_page
print(total_words)