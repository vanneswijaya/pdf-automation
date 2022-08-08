from pdf2image import convert_from_path
pages = convert_from_path('cover.pdf', 500)

count = 1
for page in pages:
    page.save(f'cover.png', 'PNG')
    count += 1