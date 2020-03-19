import pandas as pd
import os, glob, sys, subprocess, time, argparse, re, math, numpy

optional_biz = {'Мобильное приложение': False, 'Торговый эквайринг': False, 'Мобильный эквайринг': False,
                'Онлайн-бухгалтерия': False, 'Проверка контрагентов': False, 'Управление корпоративными картами': False,
                'Финансовая аналитика': False, 'Техподдержка клиентов 24/7': False, 'Персональный менеджер': False}
optional_fiz = {'Осуществление автоплатежей': False, 'Перевод за рубеж': False, 'Создание автоперевода': False,
                'Новости системы банка онлайн': False, 'Автострахование': False,
                'Страхование движимого имущества': False,
                'Страхование путешественников': False, 'Страхование пассажиров': False,
                'Наличие мобильного приложения': False, 'Открытие брокерского счета': False}
ranked_fiz = {'Переводы на карту': 0, 'Минимальная сумма вклада': 0, 'Процент по вкладу ': 0, 'Сумма кредита': 0,
              'Ставка кредита': 0, 'Переводы на карты по номеру телефона': 0}
ranked_biz = {'Стоимость обслуживания': 0, '% за снятие наличных': 0, '% за внесение наличных': 0,
              'Лимит перевода на карту физ.лица': 0}

ranked_fiz_less = {'Минимальная сумма вклада': ranked_fiz['Минимальная сумма вклада'],
                    'Ставка кредита': ranked_fiz['Ставка кредита']}
ranked_biz_less = {'Стоимость обслуживания': ranked_biz['Стоимость обслуживания'],
                   '% за снятие наличных':ranked_biz['% за снятие наличных'],
                   '% за внесение наличных':ranked_biz['% за внесение наличных']}


banks = []

black_list = []

def choose_necessary(kind):
    if kind == 'biz':
        colums = [x for x in list(optional_biz.keys()) if optional_fiz[x]]
        data_optional = pd.read_csv(r'biz.csv')
    else:
        colums = [x for x in list(optional_fiz.keys()) if not optional_fiz[x]]

        data_optional = pd.read_excel(r'fiz.xlsx', encoding = "utf-8")

    for i in colums:
        tmp = data_optional[i].values.tolist()
        for j in range(len(tmp)):
            name = data_optional['названия'].values.tolist()[j]
            if tmp[j] == 1:
                if (name not in banks) & (name not in black_list):
                    banks.append(name)
            else:
                if name in banks:
                    black_list.append(name)

    for i in black_list:
        if i in banks:
            banks.remove(i)




def rank_to_more(a, b):
    return a >= b

def rank_to_less(a, b):
    return a <= b


def choose_ranked(kind):

    data_ranked = pd.read_excel(r'both.xlsx', encoding="utf-8")
    if kind == 'biz':
        colums = list(ranked_biz.keys())

    else:
        colums = list(ranked_fiz.keys())

    for i in colums:
        tmp = data_ranked[i].values.tolist()
        for j in range(len(tmp)):
            name = data_ranked['названия'].values.tolist()[j]
            if (i in ranked_biz_less) | (i in ranked_fiz_less):
                logic = rank_to_less(tmp[j], ranked_fiz[i])
            else:
                logic = rank_to_more(tmp[j], ranked_fiz[i])

            if logic:
                if (name not in banks) & (name not in black_list):
                    banks.append(name)
            else:
                if name in banks:
                    black_list.append(name)

    for i in black_list:
        if i in banks:
            banks.remove(i)




def t_sort(data, column, rev):
    result = {}
    if len(banks) > 0:

        per = data[column].values.tolist()
        sort_per = list(dict(zip(banks, per)).items())

        sort_per.sort(key=lambda i: i[1], reverse=rev)
        print(sort_per)
        list_per = [x[0] for x in sort_per]
        rank = 1
        same = [list_per[0]]
        for i in range(1, len(list_per)):
            if sort_per[i][1] == sort_per[i - 1][1]:
                same.append(list_per[i])
            else:
                result[rank] = same
                rank += 1
                same = [list_per[i]]
        result[rank] = same
    return result


def special_sort(kind_of_sort):
    data = pd.read_excel(r'both.xlsx', encoding="utf-8")
    result = {}

    if kind_of_sort == 'по вкладу':
        result = t_sort(data, 'Процент по вкладу ', True)


    elif kind_of_sort == 'по кредиту':
        result = t_sort(data, 'Ставка кредита', False)

    elif kind_of_sort == 'По обслуживанию в месяц':
        result = t_sort(data, 'Стоимость обслуживания', True)

    elif kind_of_sort == 'По рейтингу':
        result = t_sort(data, 'Место в рейтинге', True)

    return result
choose_necessary('fiz')
choose_ranked('fiz')

print(special_sort('по вкладу'))


'''            
                if len(same) > 0:
                    same_with_vklad = []
                    for j in range(len(same)):
                        #контейнер имя - сорт2
                        same_with_vklad.append((same[j], dict_vk[same[j]]))
                    same_with_vklad = same_with_vklad.sort(key=lambda i: i[1])
                    sort_per[i-(len(same_with_vklad)):i] = same_with_vklad
                    same = []
'''
