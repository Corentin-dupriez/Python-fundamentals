def create_article(title_of_article, content_of_article, comments_of_article):
    article_body = ''
    article_body += f'''
<h1> 
    {title_of_article}
</h1>
<article>
    {content_of_article}
</article>'''
    for comment in comments_of_article:
        article_body += f'''
<div>
    {comment}
</div>'''
    return article_body


title = input()
content = input()
comments = []

while True:
    comment = input()
    if comment == 'end of comments':
        break
    comments.append(comment)


print(create_article(title, content, comments))
