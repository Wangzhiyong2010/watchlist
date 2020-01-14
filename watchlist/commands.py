# -*- coding: utf-8 -*-
import click

from watchlist import app, db
from watchlist.models import User, Movie


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')

movie_list = [
        {'title':'流浪地球', 'year':'2019'},
        {'title': '调音师', 'year':'2018'},
        {'title': '疯狂的外星人', 'year':'2019'},
        {'title': '盗梦空间 ', 'year':'2010'},
        {'title': '阿凡达', 'year':'2009'},
        {'title': '窃听风暴', 'year':'2006'},
        {'title': '七宗罪', 'year':'1995'},
        {'title': '禁闭岛', 'year':'2010'},
        {'title': '死无对证', 'year':'2018'},
        {'title': '谍影重重', 'year':'2002'},
        {'title': '源代码', 'year':'2011'},
        {'title': '最佳出价', 'year':'2013'},
        {'title': '蝙蝠侠：黑暗骑士', 'year':'2008'},
        {'title': '变脸', 'year':'1997'},
        {'title': '肖申克的救赎', 'year':'1994'},
        {'title': '阿甘正传', 'year':'1994'}]


@app.cli.command()
def forge():
    """Generate fake data."""
    db.create_all()

    name = 'Grey Li'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]

    user = User(name=name)
    db.session.add(user)
    for m2 in movie_list:
        movie2 = Movie(title_zhongwen = m2['title'], year = m2['year'])
        db.session.add(movie2)
    for m in movies:
        movie = Movie(title=m['title'], year = m['year'])
        db.session.add(movie)

    db.session.commit()
    click.echo('Done.')


@app.cli.command()
@click.option('--username', prompt=True, help='The username used to login.')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='The password used to login.')
def admin(username, password):
    """Create user."""
    db.create_all()

    user = User.query.first()
    if user is not None:
        click.echo('Updating user...')
        user.username = username
        user.set_password(password)
    else:
        click.echo('Creating user...')
        user = User(username=username, name='Admin')
        user.set_password(password)
        db.session.add(user)

    db.session.commit()
    click.echo('Done.')
