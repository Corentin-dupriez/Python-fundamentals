def loading_bar(perc):
    loaded = perc // 10
    if perc < 100:
        return f'{perc}% [{"%" * loaded}{"." * (10 - loaded)}]\nStill loading...'
    else:
        return f'{perc}% Complete!\n[{"%" * loaded}]'


percentage = int(input())

print(loading_bar(percentage))
